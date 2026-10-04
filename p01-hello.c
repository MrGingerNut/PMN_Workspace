#include <omp.h>
#include <stdio.h>

int main(int argc, char** argv){
    #pragma omp parallel    
    printf("hello world, this is thread % 2lu of %lu\n", omp_get_thread_num(), omp_get_num_threads());
    return 0;
}

