// philosophers.c
// Dijkstra's dining philosophers problem with OpenMP
// Compile: gcc -fopenmp philosophers.c -o philosophers
// Run:     ./philosophers [n]

// ni idea de como se hacia. lo hizo claude

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <omp.h>

#define EATING   0
#define HUNGRY   1
#define THINKING 2

#define RUN_TIME 15.0   // seconds, replaces sleep(15) in main

int n = 5;
int *states;            // state of each philosopher
omp_lock_t *forks;      // forks

int left(int p)  { return (p + n - 1) % n; }
int right(int p) { return (p + 1) % n; }

// random sleep between 500 and 1500 ms (rand_r is thread-safe)
void random_sleep(unsigned int *seed) {
    usleep(1000 * (500 + rand_r(seed) % 1001));
}

void take_fork(int p, int f) {
    printf("Philosopher %d tries to take fork %d\n", p, f);
    omp_set_lock(&forks[f]);
    printf("Philosopher %d takes fork %d\n", p, f);
}

void put_fork(int p, int f) {
    omp_unset_lock(&forks[f]);
    printf("Philosopher %d puts fork %d down\n", p, f);
}

void think(int p, unsigned int *seed) {
    states[p] = THINKING;
    printf("Philosopher %d is thinking\n", p);
    random_sleep(seed);
    printf("Philosopher %d is now hungry\n", p);
    states[p] = HUNGRY;
}

void eat(int p, unsigned int *seed) {
    printf("Philosopher %d is eating\n", p);
    states[p] = EATING;
    random_sleep(seed);
}

void philosopher(int p, double t0) {
    unsigned int seed = (unsigned int) (p + 1) * 2654435761u; // per-thread seed
    int left_fork = p, right_fork = right(p);
    if (p == n - 1) {   // the last philosopher takes the right fork first
        int tmp = left_fork;
        left_fork = right_fork;
        right_fork = tmp;
    }
    while (omp_get_wtime() - t0 < RUN_TIME) {
        take_fork(p, left_fork);
        take_fork(p, right_fork);
        eat(p, &seed);
        put_fork(p, right_fork);
        put_fork(p, left_fork);
        think(p, &seed);
    }
}

int main(int argc, char *argv[]) {
    if (argc > 1 && atoi(argv[1]) > 5)
        n = atoi(argv[1]);

    states = malloc(n * sizeof(int));
    forks  = malloc(n * sizeof(omp_lock_t));
    for (int i = 0; i < n; i++) {
        states[i] = HUNGRY;         // philosophers are initially hungry
        omp_init_lock(&forks[i]);   // creates free fork
    }

    omp_set_dynamic(0);             // do not let the runtime change the thread count
    double t0 = omp_get_wtime();

    #pragma omp parallel num_threads(n)
    {
        philosopher(omp_get_thread_num(), t0);
    }   // implicit barrier: waits for all philosophers

    for (int i = 0; i < n; i++)
        omp_destroy_lock(&forks[i]);
    free(states);
    free(forks);
    return 0;
}