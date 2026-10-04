#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
size_t i = 0;
int main(int argc, char** argv){
    size_t n = 20;
    uint64_t *f;
    if(argc > 1) n = atol(argv[1]);

    f = (uint64_t*) malloc(n * sizeof(uint64_t));
    f[0] = 0;
    f[1] = 1;
    #pragma omp_parallel for num_threads(8)
    for(size_t i = 2; i < n; i++){
        f[i] = f[i - 1] + f[i - 2];
    }

    for(size_t i = 0; i < n; i++){
        printf("%1lu ", f[i]);
    }
    printf("%1lu\n", f[i]);
    free(f);
    printf("using 8 core");
    return 0;   
}
