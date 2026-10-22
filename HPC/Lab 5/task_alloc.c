#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <omp.h>
#include <string.h>

#define INF 999999

/* -------------------------------------------------------------
 * Problem Structure & Cost Evaluation
 * ------------------------------------------------------------- */
typedef struct {
    int M;              // Number of tasks
    int P;              // Number of processors
    int *exec_cost;     // Flattened M x P matrix: exec_cost[i * P + p]
    int *comm_cost;     // Flattened M x M matrix: comm_cost[i * M + j]
} Problem;

// Calculate total cost = execution costs + cross-processor communication costs
long long calculate_cost(const int assignment[], const Problem *prob) {
    long long exec = 0;
    int M = prob->M;
    int P = prob->P;

    // 1. Task Execution Cost
    for (int i = 0; i < M; i++) {
        int node = assignment[i];
        exec += prob->exec_cost[i * P + node];
    }

    // 2. Inter-task Communication Cost (incurred only when scheduled on different nodes)
    long long comm = 0;
    for (int i = 0; i < M; i++) {
        int node_i = assignment[i];
        for (int j = i + 1; j < M; j++) {
            if (node_i != assignment[j]) {
                int c = prob->comm_cost[i * M + j];
                if (c > 0) {
                    comm += c;
                }
            }
        }
    }

    return exec + comm;
}

// Thread-safe fast Linear Congruential Generator (LCG)
static inline unsigned int lcg_rand(unsigned int *seed) {
    *seed = *seed * 1103515245 + 12345;
    return (*seed / 65536) % 32768;
}

static inline double lcg_rand_double(unsigned int *seed) {
    return (double)lcg_rand(seed) / 32767.0;
}

/* -------------------------------------------------------------
 * Dynamic Instance Generator for Large M and P (P << M)
 * ------------------------------------------------------------- */
Problem* generate_problem(int M, int P, unsigned int seed) {
    Problem *prob = (Problem*)malloc(sizeof(Problem));
    prob->M = M;
    prob->P = P;
    prob->exec_cost = (int*)malloc(M * P * sizeof(int));
    prob->comm_cost = (int*)malloc(M * M * sizeof(int));

    memset(prob->comm_cost, 0, M * M * sizeof(int));

    // Fill execution costs: random between 10 and 100
    for (int i = 0; i < M; i++) {
        for (int p = 0; p < P; p++) {
            prob->exec_cost[i * P + p] = 10 + (lcg_rand(&seed) % 91);
        }
    }

    // Fill symmetric communication costs: ~15% edge density, cost 5 to 50
    for (int i = 0; i < M; i++) {
        for (int j = i + 1; j < M; j++) {
            if (lcg_rand_double(&seed) < 0.15) {
                int c = 5 + (lcg_rand(&seed) % 46);
                prob->comm_cost[i * M + j] = c;
                prob->comm_cost[j * M + i] = c;
            }
        }
    }

    return prob;
}

void free_problem(Problem *prob) {
    if (prob) {
        free(prob->exec_cost);
        free(prob->comm_cost);
        free(prob);
    }
}

/* -------------------------------------------------------------
 * Verification against sample problem from specification image
 * ------------------------------------------------------------- */
int verify_sample_problem() {
    printf("============================================================\n");
    printf("VERIFICATION: Sample 6-Task, 2-Node Distributed Topology\n");
    printf("============================================================\n");

    int M = 6;
    int P = 2;
    Problem prob;
    prob.M = M;
    prob.P = P;

    int exec[6][2] = {
        {5, 10},
        {2, INF},
        {4, 4},
        {6, 3},
        {5, 2},
        {INF, 4}
    };

    int comm[6][6] = {
        {0,  6,  4,  0,  0, 12},
        {6,  0,  8, 12,  3,  0},
        {4,  8,  0,  0, 11,  0},
        {0, 12,  0,  0,  5,  0},
        {0,  3, 11,  5,  0,  0},
        {12, 0,  0,  0,  0,  0}
    };

    prob.exec_cost = (int*)malloc(M * P * sizeof(int));
    prob.comm_cost = (int*)malloc(M * M * sizeof(int));

    for (int i = 0; i < M; i++) {
        for (int p = 0; p < P; p++) {
            prob.exec_cost[i * P + p] = exec[i][p];
        }
        for (int j = 0; j < M; j++) {
            prob.comm_cost[i * M + j] = comm[i][j];
        }
    }

    // Serial assignment (c): t1..t3 -> n1 (node 0), t4..t6 -> n2 (node 1)
    int serial_assignment[6] = {0, 0, 0, 1, 1, 1};
    long long serial_cost = calculate_cost(serial_assignment, &prob);

    // Optimal assignment (d): t1..t5 -> n1 (node 0), t6 -> n2 (node 1)
    int optimal_assignment[6] = {0, 0, 0, 0, 0, 1};
    long long optimal_cost = calculate_cost(optimal_assignment, &prob);

    printf("Serial Assignment Cost   : Calculated = %lld | Expected = 58 -> %s\n",
           serial_cost, (serial_cost == 58) ? "PASSED" : "FAILED");
    printf("Optimal Assignment Cost  : Calculated = %lld | Expected = 38 -> %s\n",
           optimal_cost, (optimal_cost == 38) ? "PASSED" : "FAILED");

    free(prob.exec_cost);
    free(prob.comm_cost);

    return (serial_cost == 58 && optimal_cost == 38);
}

/* -------------------------------------------------------------
 * Genetic Algorithm (GA): Sequential and Parallel (OpenMP)
 * ------------------------------------------------------------- */
#define GA_POP_SIZE 120
#define GA_GENERATIONS 200
#define GA_MUTATION_RATE 0.05
#define GA_TOURNAMENT_SIZE 3

typedef struct {
    long long best_cost;
    int *best_assignment;
    double elapsed_time;
} Result;

// Sequential Genetic Algorithm
Result run_ga_sequential(const Problem *prob) {
    int M = prob->M;
    int P = prob->P;
    unsigned int seed = 42;

    int *population = (int*)malloc(GA_POP_SIZE * M * sizeof(int));
    int *new_population = (int*)malloc(GA_POP_SIZE * M * sizeof(int));
    long long *fitness = (long long*)malloc(GA_POP_SIZE * sizeof(long long));

    // Initialize population
    for (int i = 0; i < GA_POP_SIZE; i++) {
        for (int j = 0; j < M; j++) {
            population[i * M + j] = lcg_rand(&seed) % P;
        }
    }

    double t_start = omp_get_wtime();

    // Evaluate initial population
    int best_idx = 0;
    for (int i = 0; i < GA_POP_SIZE; i++) {
        fitness[i] = calculate_cost(&population[i * M], prob);
        if (fitness[i] < fitness[best_idx]) {
            best_idx = i;
        }
    }

    long long global_best_cost = fitness[best_idx];
    int *global_best = (int*)malloc(M * sizeof(int));
    memcpy(global_best, &population[best_idx * M], M * sizeof(int));

    // Generation loop
    for (int gen = 0; gen < GA_GENERATIONS; gen++) {
        // Elitism: Preserve the best individual directly
        memcpy(&new_population[0], global_best, M * sizeof(int));

        // Generate rest of population
        for (int i = 1; i < GA_POP_SIZE; i++) {
            // Tournament selection parent 1
            int p1 = lcg_rand(&seed) % GA_POP_SIZE;
            for (int t = 1; t < GA_TOURNAMENT_SIZE; t++) {
                int cand = lcg_rand(&seed) % GA_POP_SIZE;
                if (fitness[cand] < fitness[p1]) p1 = cand;
            }

            // Tournament selection parent 2
            int p2 = lcg_rand(&seed) % GA_POP_SIZE;
            for (int t = 1; t < GA_TOURNAMENT_SIZE; t++) {
                int cand = lcg_rand(&seed) % GA_POP_SIZE;
                if (fitness[cand] < fitness[p2]) p2 = cand;
            }

            // Single-point Crossover
            int point = lcg_rand(&seed) % M;
            for (int j = 0; j < M; j++) {
                if (j < point)
                    new_population[i * M + j] = population[p1 * M + j];
                else
                    new_population[i * M + j] = population[p2 * M + j];
            }

            // Mutation
            for (int j = 0; j < M; j++) {
                if (lcg_rand_double(&seed) < GA_MUTATION_RATE) {
                    new_population[i * M + j] = lcg_rand(&seed) % P;
                }
            }
        }

        // Copy new population to current population
        memcpy(population, new_population, GA_POP_SIZE * M * sizeof(int));

        // Evaluate fitness
        for (int i = 0; i < GA_POP_SIZE; i++) {
            fitness[i] = calculate_cost(&population[i * M], prob);
            if (fitness[i] < global_best_cost) {
                global_best_cost = fitness[i];
                memcpy(global_best, &population[i * M], M * sizeof(int));
            }
        }
    }

    double t_end = omp_get_wtime();

    free(population);
    free(new_population);
    free(fitness);

    Result res;
    res.best_cost = global_best_cost;
    res.best_assignment = global_best;
    res.elapsed_time = t_end - t_start;
    return res;
}

// Parallel Genetic Algorithm with OpenMP
Result run_ga_parallel(const Problem *prob) {
    int M = prob->M;
    int P = prob->P;

    int *population = (int*)malloc(GA_POP_SIZE * M * sizeof(int));
    int *new_population = (int*)malloc(GA_POP_SIZE * M * sizeof(int));
    long long *fitness = (long long*)malloc(GA_POP_SIZE * sizeof(long long));
    int *global_best = (int*)malloc(M * sizeof(int));
    long long global_best_cost = LLONG_MAX;

    double t_start = omp_get_wtime();

    #pragma omp parallel
    {
        int tid = omp_get_thread_num();
        unsigned int seed = 42 + tid * 10007;

        // 1. Parallel Initialization
        #pragma omp for schedule(static)
        for (int i = 0; i < GA_POP_SIZE; i++) {
            for (int j = 0; j < M; j++) {
                population[i * M + j] = lcg_rand(&seed) % P;
            }
        }

        // 2. Initial Fitness Evaluation
        #pragma omp for schedule(static)
        for (int i = 0; i < GA_POP_SIZE; i++) {
            fitness[i] = calculate_cost(&population[i * M], prob);
        }

        #pragma omp single
        {
            int best_idx = 0;
            for (int i = 1; i < GA_POP_SIZE; i++) {
                if (fitness[i] < fitness[best_idx]) {
                    best_idx = i;
                }
            }
            global_best_cost = fitness[best_idx];
            memcpy(global_best, &population[best_idx * M], M * sizeof(int));
        }

        // 3. Persistent Parallel Generations (Zero fork/join overhead)
        for (int gen = 0; gen < GA_GENERATIONS; gen++) {
            #pragma omp single
            {
                // Elitism: Preserve global best at index 0
                memcpy(&new_population[0], global_best, M * sizeof(int));
            }

            #pragma omp for schedule(static)
            for (int i = 1; i < GA_POP_SIZE; i++) {
                // Tournament selection parent 1
                int p1 = lcg_rand(&seed) % GA_POP_SIZE;
                for (int t = 1; t < GA_TOURNAMENT_SIZE; t++) {
                    int cand = lcg_rand(&seed) % GA_POP_SIZE;
                    if (fitness[cand] < fitness[p1]) p1 = cand;
                }

                // Tournament selection parent 2
                int p2 = lcg_rand(&seed) % GA_POP_SIZE;
                for (int t = 1; t < GA_TOURNAMENT_SIZE; t++) {
                    int cand = lcg_rand(&seed) % GA_POP_SIZE;
                    if (fitness[cand] < fitness[p2]) p2 = cand;
                }

                // Crossover
                int point = lcg_rand(&seed) % M;
                for (int j = 0; j < M; j++) {
                    if (j < point)
                        new_population[i * M + j] = population[p1 * M + j];
                    else
                        new_population[i * M + j] = population[p2 * M + j];
                }

                // Mutation
                for (int j = 0; j < M; j++) {
                    if (lcg_rand_double(&seed) < GA_MUTATION_RATE) {
                        new_population[i * M + j] = lcg_rand(&seed) % P;
                    }
                }
            }

            // Copy to active population in parallel
            #pragma omp for schedule(static)
            for (int i = 0; i < GA_POP_SIZE; i++) {
                memcpy(&population[i * M], &new_population[i * M], M * sizeof(int));
            }

            // Parallel fitness evaluation (Dominant O(M^2) bottleneck)
            #pragma omp for schedule(static)
            for (int i = 0; i < GA_POP_SIZE; i++) {
                fitness[i] = calculate_cost(&population[i * M], prob);
            }

            #pragma omp single
            {
                for (int i = 0; i < GA_POP_SIZE; i++) {
                    if (fitness[i] < global_best_cost) {
                        global_best_cost = fitness[i];
                        memcpy(global_best, &population[i * M], M * sizeof(int));
                    }
                }
            }
        }
    }

    double t_end = omp_get_wtime();

    free(population);
    free(new_population);
    free(fitness);

    Result res;
    res.best_cost = global_best_cost;
    res.best_assignment = global_best;
    res.elapsed_time = t_end - t_start;
    return res;
}

/* -------------------------------------------------------------
 * Particle Swarm Optimization (PSO): Sequential and Parallel
 * ------------------------------------------------------------- */
#define PSO_SWARM_SIZE 120
#define PSO_ITERATIONS 200
#define PSO_W 0.7       // Inertia weight
#define PSO_C1 1.5      // Cognitive parameter
#define PSO_C2 1.5      // Social parameter
#define V_MAX 3.0

// Sequential PSO
Result run_pso_sequential(const Problem *prob) {
    int M = prob->M;
    int P = prob->P;
    unsigned int seed = 777;

    int *pos = (int*)malloc(PSO_SWARM_SIZE * M * sizeof(int));
    double *vel = (double*)malloc(PSO_SWARM_SIZE * M * sizeof(double));
    int *pbest_pos = (int*)malloc(PSO_SWARM_SIZE * M * sizeof(int));
    long long *pbest_cost = (long long*)malloc(PSO_SWARM_SIZE * sizeof(long long));

    int *gbest_pos = (int*)malloc(M * sizeof(int));
    long long gbest_cost = LLONG_MAX;

    // Initialize swarm
    for (int i = 0; i < PSO_SWARM_SIZE; i++) {
        for (int j = 0; j < M; j++) {
            pos[i * M + j] = lcg_rand(&seed) % P;
            vel[i * M + j] = (lcg_rand_double(&seed) * 2.0 - 1.0) * V_MAX;
            pbest_pos[i * M + j] = pos[i * M + j];
        }
        pbest_cost[i] = calculate_cost(&pos[i * M], prob);
        if (pbest_cost[i] < gbest_cost) {
            gbest_cost = pbest_cost[i];
            memcpy(gbest_pos, &pos[i * M], M * sizeof(int));
        }
    }

    double t_start = omp_get_wtime();

    // Iteration loop
    for (int iter = 0; iter < PSO_ITERATIONS; iter++) {
        for (int i = 0; i < PSO_SWARM_SIZE; i++) {
            for (int j = 0; j < M; j++) {
                double r1 = lcg_rand_double(&seed);
                double r2 = lcg_rand_double(&seed);

                // Velocity update
                vel[i * M + j] = PSO_W * vel[i * M + j]
                               + PSO_C1 * r1 * (pbest_pos[i * M + j] - pos[i * M + j])
                               + PSO_C2 * r2 * (gbest_pos[j] - pos[i * M + j]);

                if (vel[i * M + j] > V_MAX) vel[i * M + j] = V_MAX;
                if (vel[i * M + j] < -V_MAX) vel[i * M + j] = -V_MAX;

                // Position update with clamping to valid processors [0, P-1]
                int new_p = (int)round(pos[i * M + j] + vel[i * M + j]);
                if (new_p < 0) new_p = 0;
                if (new_p >= P) new_p = P - 1;
                pos[i * M + j] = new_p;
            }

            // Fitness evaluation
            long long current_cost = calculate_cost(&pos[i * M], prob);
            if (current_cost < pbest_cost[i]) {
                pbest_cost[i] = current_cost;
                memcpy(&pbest_pos[i * M], &pos[i * M], M * sizeof(int));
                if (current_cost < gbest_cost) {
                    gbest_cost = current_cost;
                    memcpy(gbest_pos, &pos[i * M], M * sizeof(int));
                }
            }
        }
    }

    double t_end = omp_get_wtime();

    free(pos);
    free(vel);
    free(pbest_pos);
    free(pbest_cost);

    Result res;
    res.best_cost = gbest_cost;
    res.best_assignment = gbest_pos;
    res.elapsed_time = t_end - t_start;
    return res;
}

// Parallel PSO with OpenMP
Result run_pso_parallel(const Problem *prob) {
    int M = prob->M;
    int P = prob->P;

    int *pos = (int*)malloc(PSO_SWARM_SIZE * M * sizeof(int));
    double *vel = (double*)malloc(PSO_SWARM_SIZE * M * sizeof(double));
    int *pbest_pos = (int*)malloc(PSO_SWARM_SIZE * M * sizeof(int));
    long long *pbest_cost = (long long*)malloc(PSO_SWARM_SIZE * sizeof(long long));

    int *gbest_pos = (int*)malloc(M * sizeof(int));
    long long gbest_cost = LLONG_MAX;

    double t_start = omp_get_wtime();

    #pragma omp parallel
    {
        int tid = omp_get_thread_num();
        unsigned int seed = 777 + tid * 54321;

        // Parallel initialization
        #pragma omp for schedule(static)
        for (int i = 0; i < PSO_SWARM_SIZE; i++) {
            for (int j = 0; j < M; j++) {
                pos[i * M + j] = lcg_rand(&seed) % P;
                vel[i * M + j] = (lcg_rand_double(&seed) * 2.0 - 1.0) * V_MAX;
                pbest_pos[i * M + j] = pos[i * M + j];
            }
            pbest_cost[i] = calculate_cost(&pos[i * M], prob);
        }

        #pragma omp single
        {
            for (int i = 0; i < PSO_SWARM_SIZE; i++) {
                if (pbest_cost[i] < gbest_cost) {
                    gbest_cost = pbest_cost[i];
                    memcpy(gbest_pos, &pos[i * M], M * sizeof(int));
                }
            }
        }

        // Persistent Parallel Iterations
        for (int iter = 0; iter < PSO_ITERATIONS; iter++) {
            #pragma omp for schedule(static)
            for (int i = 0; i < PSO_SWARM_SIZE; i++) {
                for (int j = 0; j < M; j++) {
                    double r1 = lcg_rand_double(&seed);
                    double r2 = lcg_rand_double(&seed);

                    vel[i * M + j] = PSO_W * vel[i * M + j]
                                   + PSO_C1 * r1 * (pbest_pos[i * M + j] - pos[i * M + j])
                                   + PSO_C2 * r2 * (gbest_pos[j] - pos[i * M + j]);

                    if (vel[i * M + j] > V_MAX) vel[i * M + j] = V_MAX;
                    if (vel[i * M + j] < -V_MAX) vel[i * M + j] = -V_MAX;

                    int new_p = (int)round(pos[i * M + j] + vel[i * M + j]);
                    if (new_p < 0) new_p = 0;
                    if (new_p >= P) new_p = P - 1;
                    pos[i * M + j] = new_p;
                }

                // Fitness evaluation (O(M^2) per particle)
                long long current_cost = calculate_cost(&pos[i * M], prob);
                if (current_cost < pbest_cost[i]) {
                    pbest_cost[i] = current_cost;
                    memcpy(&pbest_pos[i * M], &pos[i * M], M * sizeof(int));
                }
            }

            // Update gbest across swarm
            #pragma omp single
            {
                for (int i = 0; i < PSO_SWARM_SIZE; i++) {
                    if (pbest_cost[i] < gbest_cost) {
                        gbest_cost = pbest_cost[i];
                        memcpy(gbest_pos, &pbest_pos[i * M], M * sizeof(int));
                    }
                }
            }
        }
    }

    double t_end = omp_get_wtime();

    free(pos);
    free(vel);
    free(pbest_pos);
    free(pbest_cost);

    Result res;
    res.best_cost = gbest_cost;
    res.best_assignment = gbest_pos;
    res.elapsed_time = t_end - t_start;
    return res;
}

/* -------------------------------------------------------------
 * Main Driver: Verification & Comparative Benchmarks
 * ------------------------------------------------------------- */
int main(int argc, char *argv[]) {
    // 1. Run Verification against sample topology
    if (!verify_sample_problem()) {
        printf("Verification failed! Exiting...\n");
        return 1;
    }
    printf("\n");

    // 2. Setup Large Scale Problem (M >> P)
    int M = 300;   // 300 Tasks
    int P = 16;    // 16 Processors

    if (argc >= 3) {
        M = atoi(argv[1]);
        P = atoi(argv[2]);
    }

    int num_threads = omp_get_max_threads();
    printf("============================================================\n");
    printf("TASK ALLOCATION PROBLEM (TAP) BENCHMARK\n");
    printf("Dimensions: M = %d Tasks, P = %d Processors (P << M)\n", M, P);
    printf("OpenMP Threads Available: %d\n", num_threads);
    printf("============================================================\n");

    printf("Generating synthetic problem instance (Exec Cost: 10-100, Comm Density: 15%%)...\n");
    Problem *prob = generate_problem(M, P, 12345);

    // Initial random assignment baseline cost
    int *rand_assign = (int*)malloc(M * sizeof(int));
    unsigned int rseed = 999;
    for (int i = 0; i < M; i++) rand_assign[i] = lcg_rand(&rseed) % P;
    long long baseline_cost = calculate_cost(rand_assign, prob);
    printf("Random Baseline Allocation Total Cost: %lld\n\n", baseline_cost);
    free(rand_assign);

    // 3. Genetic Algorithm Benchmarking
    printf("--- Running Genetic Algorithm (Pop: %d, Gens: %d) ---\n", GA_POP_SIZE, GA_GENERATIONS);
    printf("Running Sequential GA...\n");
    Result seq_ga = run_ga_sequential(prob);
    printf("  Sequential GA Best Cost : %lld | Time: %.4f s\n", seq_ga.best_cost, seq_ga.elapsed_time);

    printf("Running Parallel OpenMP GA (%d threads)...\n", num_threads);
    Result par_ga = run_ga_parallel(prob);
    double speedup_ga = seq_ga.elapsed_time / par_ga.elapsed_time;
    printf("  Parallel GA Best Cost   : %lld | Time: %.4f s | Speedup: %.2fx\n\n",
           par_ga.best_cost, par_ga.elapsed_time, speedup_ga);

    // 4. Particle Swarm Optimization Benchmarking
    printf("--- Running Particle Swarm Optimization (Swarm: %d, Iters: %d) ---\n", PSO_SWARM_SIZE, PSO_ITERATIONS);
    printf("Running Sequential PSO...\n");
    Result seq_pso = run_pso_sequential(prob);
    printf("  Sequential PSO Best Cost: %lld | Time: %.4f s\n", seq_pso.best_cost, seq_pso.elapsed_time);

    printf("Running Parallel OpenMP PSO (%d threads)...\n", num_threads);
    Result par_pso = run_pso_parallel(prob);
    double speedup_pso = seq_pso.elapsed_time / par_pso.elapsed_time;
    printf("  Parallel PSO Best Cost  : %lld | Time: %.4f s | Speedup: %.2fx\n\n",
           par_pso.best_cost, par_pso.elapsed_time, speedup_pso);

    // 5. Summary Table
    printf("========================================================================================\n");
    printf("%-20s | %-12s | %-12s | %-10s | %-15s\n", "Algorithm", "Time (sec)", "Speedup", "Best Cost", "Cost Reduction");
    printf("========================================================================================\n");
    printf("%-20s | %10.4f s | %12s | %10lld | %13.2f%%\n",
           "Sequential GA", seq_ga.elapsed_time, "1.00x (base)", seq_ga.best_cost,
           100.0 * (1.0 - (double)seq_ga.best_cost / baseline_cost));
    printf("%-20s | %10.4f s | %11.2fx | %10lld | %13.2f%%\n",
           "Parallel GA (OpenMP)", par_ga.elapsed_time, speedup_ga, par_ga.best_cost,
           100.0 * (1.0 - (double)par_ga.best_cost / baseline_cost));
    printf("%-20s | %10.4f s | %12s | %10lld | %13.2f%%\n",
           "Sequential PSO", seq_pso.elapsed_time, "1.00x (base)", seq_pso.best_cost,
           100.0 * (1.0 - (double)seq_pso.best_cost / baseline_cost));
    printf("%-20s | %10.4f s | %11.2fx | %10lld | %13.2f%%\n",
           "Parallel PSO (OpenMP)", par_pso.elapsed_time, speedup_pso, par_pso.best_cost,
           100.0 * (1.0 - (double)par_pso.best_cost / baseline_cost));
    printf("========================================================================================\n");

    // Print sample allocation from best overall solution
    Result *best_overall = (par_ga.best_cost < par_pso.best_cost) ? &par_ga : &par_pso;
    const char *best_name = (par_ga.best_cost < par_pso.best_cost) ? "Parallel GA" : "Parallel PSO";
    printf("\nSample Task-to-Processor Mapping (First 20 Tasks from %s, Total Cost = %lld):\n", best_name, best_overall->best_cost);
    for (int i = 0; i < ((M < 20) ? M : 20); i++) {
        printf("  Task %3d -> Processor %2d\n", i + 1, best_overall->best_assignment[i] + 1);
    }
    if (M > 20) printf("  ... [%d more tasks mapped]\n", M - 20);

    // Free resources
    free(seq_ga.best_assignment);
    free(par_ga.best_assignment);
    free(seq_pso.best_assignment);
    free(par_pso.best_assignment);
    free_problem(prob);

    return 0;
}
