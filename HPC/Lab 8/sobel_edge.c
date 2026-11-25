#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <mpi.h>

// Save grayscale image to a standard binary PGM (P5) file
void save_pgm(const char *filename, unsigned char *img, int H, int W) {
    FILE *f = fopen(filename, "wb");
    if (!f) {
        fprintf(stderr, "Warning: Could not open %s for writing.\n", filename);
        return;
    }
    fprintf(f, "P5\n%d %d\n255\n", W, H);
    fwrite(img, sizeof(unsigned char), H * W, f);
    fclose(f);
}

// Helper to skip whitespace and comments in PGM header
static void skip_pgm_comments(FILE *f) {
    int ch;
    while ((ch = fgetc(f)) != EOF) {
        if (ch == '#') {
            // Comment line: skip until newline
            while ((ch = fgetc(f)) != EOF && ch != '\n');
        } else if (!isspace(ch)) {
            // Non-whitespace character found: put it back
            ungetc(ch, f);
            break;
        }
    }
}

// Load a binary PGM (P5) image from disk
unsigned char *load_pgm(const char *filename, int *H, int *W) {
    FILE *f = fopen(filename, "rb");
    if (!f) {
        return NULL;
    }

    char magic[3];
    if (fscanf(f, "%2s", magic) != 1 || strcmp(magic, "P5") != 0) {
        fclose(f);
        return NULL;
    }

    skip_pgm_comments(f);
    if (fscanf(f, "%d", W) != 1) {
        fclose(f);
        return NULL;
    }

    skip_pgm_comments(f);
    if (fscanf(f, "%d", H) != 1) {
        fclose(f);
        return NULL;
    }

    int max_val;
    skip_pgm_comments(f);
    if (fscanf(f, "%d", &max_val) != 1 || max_val > 255) {
        fclose(f);
        return NULL;
    }

    // Single whitespace character immediately before raw binary data
    fgetc(f);

    unsigned char *data = (unsigned char *)malloc((*H) * (*W) * sizeof(unsigned char));
    if (!data) {
        fclose(f);
        return NULL;
    }

    size_t read_bytes = fread(data, sizeof(unsigned char), (*H) * (*W), f);
    if (read_bytes != (size_t)((*H) * (*W))) {
        fprintf(stderr, "Warning: Expected %d bytes, read %zu bytes from %s.\n", (*H) * (*W), read_bytes, filename);
    }

    fclose(f);
    return data;
}

// Generate a synthetic test image with geometric features and sharp edges
void generate_synthetic_image(unsigned char *img, int H, int W) {
    for (int i = 0; i < H * W; i++) {
        img[i] = 30;
    }

    int r_start = H / 4, r_end = 3 * H / 4;
    int c_start = W / 4, c_end = 3 * W / 4;
    for (int i = r_start; i < r_end; i++) {
        for (int j = c_start; j < c_end; j++) {
            img[i * W + j] = 220;
        }
    }

    int cy = H / 2, cx = W / 2;
    int radius = H / 6;
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            int dy = i - cy;
            int dx = j - cx;
            if (dy * dy + dx * dx <= radius * radius) {
                img[i * W + j] = 90;
            }
        }
    }
}

// Sequential Sobel reference computation on full image (for verification)
void sequential_sobel(unsigned char *src, unsigned char *dst, int H, int W) {
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (i == 0 || i == H - 1 || j == 0 || j == W - 1) {
                dst[i * W + j] = 0;
            } else {
                int gx = -1 * src[(i - 1) * W + (j - 1)] + 1 * src[(i - 1) * W + (j + 1)]
                         -2 * src[i * W + (j - 1)]       + 2 * src[i * W + (j + 1)]
                         -1 * src[(i + 1) * W + (j - 1)] + 1 * src[(i + 1) * W + (j + 1)];

                int gy = -1 * src[(i - 1) * W + (j - 1)] - 2 * src[(i - 1) * W + j] - 1 * src[(i - 1) * W + (j + 1)]
                         +1 * src[(i + 1) * W + (j - 1)] + 2 * src[(i + 1) * W + j] + 1 * src[(i + 1) * W + (j + 1)];

                int mag = (int)(sqrt(gx * gx + gy * gy) + 0.5);
                if (mag > 255) mag = 255;
                dst[i * W + j] = (unsigned char)mag;
            }
        }
    }
}

int main(int argc, char *argv[]) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int H = 0, W = 0;
    unsigned char *full_image = NULL;
    char image_source[256] = "";

    if (rank == 0) {
        // Check for specified file or default to "lena.pgm"
        const char *filename = (argc > 1 && argv[1][0] != '-') ? argv[1] : "lena.pgm";
        full_image = load_pgm(filename, &H, &W);

        if (full_image) {
            snprintf(image_source, sizeof(image_source), "PGM file '%s'", filename);
        } else {
            // Fallback to synthetic image with user-specified or default dimensions
            H = (argc >= 2 && atoi(argv[1]) > 0) ? atoi(argv[1]) : 512;
            W = (argc >= 3 && atoi(argv[2]) > 0) ? atoi(argv[2]) : H;
            full_image = (unsigned char *)malloc(H * W * sizeof(unsigned char));
            generate_synthetic_image(full_image, H, W);
            snprintf(image_source, sizeof(image_source), "Synthetic test pattern (%dx%d)", W, H);
        }
    }

    // Broadcast dimensions (H, W) to all processes
    int dims[2];
    if (rank == 0) {
        dims[0] = H;
        dims[1] = W;
    }
    MPI_Bcast(dims, 2, MPI_INT, 0, MPI_COMM_WORLD);
    H = dims[0];
    W = dims[1];

    // Validate that image height is divisible by process count
    if (H % size != 0) {
        if (rank == 0) {
            fprintf(stderr, "Error: Image height (%d) must be divisible by process count (%d).\n", H, size);
            if (full_image) free(full_image);
        }
        MPI_Abort(MPI_COMM_WORLD, 1);
    }

    int H_local = H / size;

    if (rank == 0) {
        printf("=====================================================\n");
        printf(" Parallel Sobel Edge Detection (OpenMPI with Halo)  \n");
        printf("=====================================================\n");
        printf("Input source     : %s\n", image_source);
        printf("Image dimensions : %d x %d\n", W, H);
        printf("MPI processes    : %d\n", size);
        printf("Rows per process : %d\n", H_local);
        printf("-----------------------------------------------------\n");
    }

    // Master output memory allocations
    unsigned char *parallel_output = NULL;
    unsigned char *seq_output = NULL;
    if (rank == 0) {
        parallel_output = (unsigned char *)malloc(H * W * sizeof(unsigned char));
        seq_output = (unsigned char *)malloc(H * W * sizeof(unsigned char));
    }

    // Local buffer has (H_local + 2) rows:
    // Row 0             : Top halo row
    // Rows 1 to H_local : Local image data
    // Row H_local + 1   : Bottom halo row
    unsigned char *local_buf = (unsigned char *)malloc((H_local + 2) * W * sizeof(unsigned char));
    unsigned char *local_out = (unsigned char *)malloc(H_local * W * sizeof(unsigned char));

    MPI_Barrier(MPI_COMM_WORLD);
    double t_start = MPI_Wtime();

    // 1. Scatter image chunks to rows 1..H_local of local_buf
    MPI_Scatter(full_image, H_local * W, MPI_UNSIGNED_CHAR,
                &local_buf[1 * W], H_local * W, MPI_UNSIGNED_CHAR,
                0, MPI_COMM_WORLD);

    // 2. Halo Exchange with top and bottom neighbors
    int top_neighbor = (rank == 0) ? MPI_PROC_NULL : rank - 1;
    int bottom_neighbor = (rank == size - 1) ? MPI_PROC_NULL : rank + 1;

    // Send local row 1 (top active row) to top neighbor,
    // receive bottom halo from bottom neighbor into row (H_local + 1)
    MPI_Sendrecv(&local_buf[1 * W], W, MPI_UNSIGNED_CHAR, top_neighbor, 0,
                 &local_buf[(H_local + 1) * W], W, MPI_UNSIGNED_CHAR, bottom_neighbor, 0,
                 MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    // Send local row H_local (bottom active row) to bottom neighbor,
    // receive top halo from top neighbor into row 0
    MPI_Sendrecv(&local_buf[H_local * W], W, MPI_UNSIGNED_CHAR, bottom_neighbor, 1,
                 &local_buf[0 * W], W, MPI_UNSIGNED_CHAR, top_neighbor, 1,
                 MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    // Set zero-padding for global outer image boundaries
    if (rank == 0) {
        memset(&local_buf[0 * W], 0, W);
    }
    if (rank == size - 1) {
        memset(&local_buf[(H_local + 1) * W], 0, W);
    }

    // 3. Compute Sobel filter using the halo region
    for (int i = 1; i <= H_local; i++) {
        int global_row = rank * H_local + (i - 1);

        for (int j = 0; j < W; j++) {
            // Left, right, and global top/bottom borders are 0
            if (global_row == 0 || global_row == H - 1 || j == 0 || j == W - 1) {
                local_out[(i - 1) * W + j] = 0;
            } else {
                int gx = -1 * local_buf[(i - 1) * W + (j - 1)] + 1 * local_buf[(i - 1) * W + (j + 1)]
                         -2 * local_buf[i * W + (j - 1)]       + 2 * local_buf[i * W + (j + 1)]
                         -1 * local_buf[(i + 1) * W + (j - 1)] + 1 * local_buf[(i + 1) * W + (j + 1)];

                int gy = -1 * local_buf[(i - 1) * W + (j - 1)] - 2 * local_buf[(i - 1) * W + j] - 1 * local_buf[(i - 1) * W + (j + 1)]
                         +1 * local_buf[(i + 1) * W + (j - 1)] + 2 * local_buf[(i + 1) * W + j] + 1 * local_buf[(i + 1) * W + (j + 1)];

                int mag = (int)(sqrt(gx * gx + gy * gy) + 0.5);
                if (mag > 255) mag = 255;
                local_out[(i - 1) * W + j] = (unsigned char)mag;
            }
        }
    }

    // 4. Gather computed edge rows back to master process
    MPI_Gather(local_out, H_local * W, MPI_UNSIGNED_CHAR,
               parallel_output, H_local * W, MPI_UNSIGNED_CHAR,
               0, MPI_COMM_WORLD);

    MPI_Barrier(MPI_COMM_WORLD);
    double t_end = MPI_Wtime();

    // 5. Master verification and reporting
    if (rank == 0) {
        double elapsed_time = t_end - t_start;
        printf("Parallel execution time   : %.6f seconds\n", elapsed_time);

        // Compute sequential baseline
        double seq_start = MPI_Wtime();
        sequential_sobel(full_image, seq_output, H, W);
        double seq_end = MPI_Wtime();
        printf("Sequential reference time : %.6f seconds\n", seq_end - seq_start);

        // Element-by-element verification
        int mismatches = 0;
        for (int i = 0; i < H * W; i++) {
            if (parallel_output[i] != seq_output[i]) {
                mismatches++;
            }
        }

        if (mismatches == 0) {
            printf("\n[VERIFICATION PASSED] Parallel output with Halo Exchange matches sequential result 100%%!\n");
        } else {
            printf("\n[VERIFICATION FAILED] Found %d mismatched pixels out of %d!\n", mismatches, H * W);
        }

        // Save edge output image
        save_pgm("output_edges.pgm", parallel_output, H, W);
        printf("Output saved to output_edges.pgm (PGM P5 format)\n");
        printf("=====================================================\n");

        free(full_image);
        free(parallel_output);
        free(seq_output);
    }

    free(local_buf);
    free(local_out);

    MPI_Finalize();
    return 0;
}
