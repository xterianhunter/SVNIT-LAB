#include<stdio.h>
#include <stdlib.h>
#include <time.h>

#define TASKS 20
#define PROCESSORS 4
#define POP_SIZE 50
#define GENERATIONS 200
#define MUTATION_RATE 0.1

int task_time[TASKS] = {
    10, 20, 15, 30, 25, 12, 18, 22, 35, 14,
    16, 28, 11, 24, 19, 13, 31, 17, 21, 26
};

int comm[TASKS][TASKS] = {0};

int population[POP_SIZE][TASKS];
int new_population[POP_SIZE][TASKS];

int fitness(int chromosome[])
{
    int load[PROCESSORS] = {0};

    for(int i = 0;i<TASKS; i++)
        load[chromosome[i]] += task_time[i];

    for(int i = 0; i<TASKS; i++)
    {
        for(int j = i+1; j<TASKS; j++)
        {
            if (comm[i][j] > 0 && chromosome[i] != chromosome[j])
            {
                load[chromosome[i]] += comm[i][j];
            }
        }
    }

    int max_load = load[0];

    for(int i = 1; i<PROCESSORS; i++)
        if (load[i] > max_load)
            max_load = load[i];

    return max_load;
}


void initialize()
{
    for (int i = 0; i<POP_SIZE; i++)
        for (int j = 0; j<TASKS; j++)
            population[i][j] = rand() % PROCESSORS;
}

int select_parent()
{
    int a = rand() % POP_SIZE;
    int b = rand() % POP_SIZE;

    if (fitness(population[a]) < fitness(population[b]))
        return a;

    return b;
}

void crossover(int p1[], int p2[], int child[])
{
    int point = rand() % TASKS;

    for (int i = 0; i<TASKS; i++)
    {
        if (i<point)
            child[i] = p1[i];
        else
            child[i] = p2[i];
    }
}

void mutate(int chromosome[])
{
    for (int i=0; i<TASKS; i++)
    {
        if((double)rand() / RAND_MAX < MUTATION_RATE)
            chromosome[i] = rand() % PROCESSORS;
    }
}

int main()
{
    srand(time(NULL));

    comm[0][1] = 5;
    comm[1][2] = 8;
    comm[2][3] = 6;
    comm[4][5] = 10;
    comm[6][7] = 4;
    comm[8][9] = 7;
    comm[10][11] = 9;

    initialize();

    for (int gen = 0; gen < GENERATIONS; gen++)
    {
        for(int i =0; i<POP_SIZE; i++)
        {
            int p1 = select_parent();
            int p2 = select_parent();

            crossover(population[p1], population[p2], new_population[i]);
            mutate(new_population[i]);
        }
        
        for(int i = 0; i < POP_SIZE; i++)
            for(int j = 0; j< TASKS; j++)
                population[i][j] = new_population[i][j];
    }

    int best = 0;
    for(int i = 1;i<POP_SIZE; i++)
        if (fitness(population[i]) < fitness(population[best]))
            best = i;
    printf("Task Assigment: \n");
    for(int i = 0; i<TASKS; i++)
        printf("Task %d -> Processor %d\n", i+1, population[best][i] + 1);

    printf("\nFitness (Makespan) : %d\n", fitness(population[best]));

    return 0;
}
        

    

