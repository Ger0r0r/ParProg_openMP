#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <unistd.h>
#include <sys/types.h>

int main (int argc, char * argv[]) {

	if (argc != 2) {
		printf("Usage: %s <number>\n", argv[0]);
		return 0;
	}

	int N = atoi(argv[1]);
	double sum = 0;

	double * own_sum = calloc(omp_get_max_threads(), sizeof(double));

	#pragma omp parallel for schedule(dynamic,1) 
		for (int i = 1; i < N; ++i) {
			own_sum[omp_get_thread_num()] += 1/(double)i;
			printf("(%d)\tSUM: %lg\n", omp_get_thread_num(), own_sum[omp_get_thread_num()]);
		}

	for (int i = 0; i < omp_get_max_threads(); ++i){
		sum += own_sum[i];
		printf("(%d)\tResult: %lg\n", i, own_sum[i]);
	}

	printf("Total result %lg\n", sum);
	free(own_sum);
	return 0;
}