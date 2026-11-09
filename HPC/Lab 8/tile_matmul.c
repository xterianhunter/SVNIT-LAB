#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <mpi.h>

// Multiply two b x b tiles and accumulate into C_tile: C += A * B
void multiply_tile(int b, double *A, double *B, double *C) {
    for (int i = 0; i < b; i++) {
        for (int k = 0; k < b; k++) {
            for (int j = 0; j < b; j++) {
                C[i * b + j] += A[i * b + k] * B[k * b + j];
            }
        }
    }
}

// Print an N x N matrix
void print_matrix(const char *name, double *mat, int N) {
    printf("%s (%dx%d):\n", name, N, N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%7.2f ", mat[i * N + j]);
        }
        printf("\n");
    }
    printf("\n");
}

int main(int argc, char *argv[]) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    // Matrix dimension N (default 4)
    int N = 4;
    if (argc > 1) {
        N = atoi(argv[1]);
    }

    // Check if process count P is a perfect square: P = q * q
    int q = (int)sqrt(size);
    if (q * q != size) {
        if (rank == 0) {
            fprintf(stderr, "Error: Number of processes (%d) must be a perfect square (e.g., 1, 4, 9, 16).\n", size);
        }
        MPI_Abort(MPI_COMM_WORLD, 1);
    }

    // Check if matrix dimension N is divisible by grid dimension q
    if (N % q != 0) {
        if (rank == 0) {
            fprintf(stderr, "Error: Matrix dimension N (%d) must be divisible by grid dimension q (%d).\n", N, q);
        }
        MPI_Abort(MPI_COMM_WORLD, 1);
    }

    int b = N / q; // tile size (b x b)
    int tile_size = b * b;

    // Create 2D Cartesian Grid Topology
    int dims[2] = {q, q};
    int periods[2] = {1, 1}; // periodic/circular boundaries in both dimensions
    MPI_Comm cart_comm;
    MPI_Cart_create(MPI_COMM_WORLD, 2, dims, periods, 1, &cart_comm);

    int coords[2];
    MPI_Cart_coords(cart_comm, rank, 2, coords);
    int row = coords[0];
    int col = coords[1];

    // Allocate memory for local tiles
    double *A_tile = (double *)malloc(tile_size * sizeof(double));
    double *B_tile = (double *)malloc(tile_size * sizeof(double));
    double *C_tile = (double *)calloc(tile_size, sizeof(double));

    // Global matrices on rank 0
    double *A_global = NULL;
    double *B_global = NULL;
    double *C_global = NULL;

    if (rank == 0) {
        A_global = (double *)malloc(N * N * sizeof(double));
        B_global = (double *)malloc(N * N * sizeof(double));
        C_global = (double *)malloc(N * N * sizeof(double));

        // Initialize sample matrices
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                A_global[i * N + j] = i + j + 1.0;
                B_global[i * N + j] = (i == j) ? 2.0 : 1.0;
            }
        }

        if (N <= 8) {
            print_matrix("Matrix A", A_global, N);
            print_matrix("Matrix B", B_global, N);
        }

        // Distribute tiles to each process
        for (int p = 0; p < size; p++) {
            int p_coords[2];
            MPI_Cart_coords(cart_comm, p, 2, p_coords);
            int pr = p_coords[0];
            int pc = p_coords[1];

            double temp_A[tile_size];
            double temp_B[tile_size];

            for (int i = 0; i < b; i++) {
                for (int j = 0; j < b; j++) {
                    int g_idx = (pr * b + i) * N + (pc * b + j);
                    temp_A[i * b + j] = A_global[g_idx];
                    temp_B[i * b + j] = B_global[g_idx];
                }
            }

            if (p == 0) {
                for (int k = 0; k < tile_size; k++) {
                    A_tile[k] = temp_A[k];
                    B_tile[k] = temp_B[k];
                }
            } else {
                MPI_Send(temp_A, tile_size, MPI_DOUBLE, p, 0, cart_comm);
                MPI_Send(temp_B, tile_size, MPI_DOUBLE, p, 1, cart_comm);
            }
        }
    } else {
        MPI_Recv(A_tile, tile_size, MPI_DOUBLE, 0, 0, cart_comm, MPI_STATUS_IGNORE);
        MPI_Recv(B_tile, tile_size, MPI_DOUBLE, 0, 1, cart_comm, MPI_STATUS_IGNORE);
    }

    // Barrier and Start Timer
    MPI_Barrier(cart_comm);
    double start_time = MPI_Wtime();

    // Cannon's Algorithm - Phase 1: Initial Alignment (Skewing)
    // Shift A_tile left circularly by row positions (dimension 1)
    if (row > 0) {
        int src_A, dst_A;
        MPI_Cart_shift(cart_comm, 1, -row, &src_A, &dst_A);
        MPI_Sendrecv_replace(A_tile, tile_size, MPI_DOUBLE, dst_A, 10, src_A, 10, cart_comm, MPI_STATUS_IGNORE);
    }

    // Shift B_tile up circularly by col positions (dimension 0)
    if (col > 0) {
        int src_B, dst_B;
        MPI_Cart_shift(cart_comm, 0, -col, &src_B, &dst_B);
        MPI_Sendrecv_replace(B_tile, tile_size, MPI_DOUBLE, dst_B, 20, src_B, 20, cart_comm, MPI_STATUS_IGNORE);
    }

    // Cannon's Algorithm - Phase 2: Compute and Shift (q steps)
    int src_A_step, dst_A_step;
    int src_B_step, dst_B_step;
    MPI_Cart_shift(cart_comm, 1, -1, &src_A_step, &dst_A_step); // left shift by 1
    MPI_Cart_shift(cart_comm, 0, -1, &src_B_step, &dst_B_step); // up shift by 1

    for (int step = 0; step < q; step++) {
        // Multiply current local tiles
        multiply_tile(b, A_tile, B_tile, C_tile);

        // Circularly shift A left by 1 and B up by 1 (except after last step)
        if (step < q - 1) {
            MPI_Sendrecv_replace(A_tile, tile_size, MPI_DOUBLE, dst_A_step, 30, src_A_step, 30, cart_comm, MPI_STATUS_IGNORE);
            MPI_Sendrecv_replace(B_tile, tile_size, MPI_DOUBLE, dst_B_step, 40, src_B_step, 40, cart_comm, MPI_STATUS_IGNORE);
        }
    }

    // Barrier and Stop Timer
    MPI_Barrier(cart_comm);
    double end_time = MPI_Wtime();
    double elapsed_time = end_time - start_time;

    // Collect result tiles on rank 0
    if (rank == 0) {
        for (int p = 0; p < size; p++) {
            double temp_C[tile_size];
            if (p == 0) {
                for (int k = 0; k < tile_size; k++) {
                    temp_C[k] = C_tile[k];
                }
            } else {
                MPI_Recv(temp_C, tile_size, MPI_DOUBLE, p, 50, cart_comm, MPI_STATUS_IGNORE);
            }

            int p_coords[2];
            MPI_Cart_coords(cart_comm, p, 2, p_coords);
            int pr = p_coords[0];
            int pc = p_coords[1];

            for (int i = 0; i < b; i++) {
                for (int j = 0; j < b; j++) {
                    C_global[(pr * b + i) * N + (pc * b + j)] = temp_C[i * b + j];
                }
            }
        }
    } else {
        MPI_Send(C_tile, tile_size, MPI_DOUBLE, 0, 50, cart_comm);
    }

    // Verification and Report on rank 0
    if (rank == 0) {
        if (N <= 8) {
            print_matrix("Result Matrix C (Parallel)", C_global, N);
        }

        // Sequential reference computation
        double *C_seq = (double *)calloc(N * N, sizeof(double));
        for (int i = 0; i < N; i++) {
            for (int k = 0; k < N; k++) {
                for (int j = 0; j < N; j++) {
                    C_seq[i * N + j] += A_global[i * N + k] * B_global[k * N + j];
                }
            }
        }

        // Verify correctness
        int correct = 1;
        for (int i = 0; i < N * N; i++) {
            if (fabs(C_global[i] - C_seq[i]) > 1e-5) {
                correct = 0;
                break;
            }
        }

        printf("==================================================\n");
        printf("Parallel Tile Matrix Multiplication (Cannon's Algorithm)\n");
        printf("Processes: %d (Grid: %dx%d)\n", size, q, q);
        printf("Matrix Dimension: %dx%d (Tile Size: %dx%d)\n", N, N, b, b);
        printf("Elapsed Time: %f seconds\n", elapsed_time);
        printf("Verification: %s\n", correct ? "PASSED" : "FAILED");
        printf("==================================================\n");

        free(A_global);
        free(B_global);
        free(C_global);
        free(C_seq);
    }

    // Clean up local allocations
    free(A_tile);
    free(B_tile);
    free(C_tile);
    MPI_Comm_free(&cart_comm);

    MPI_Finalize();
    return 0;
}
