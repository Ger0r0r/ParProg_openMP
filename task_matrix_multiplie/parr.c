#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

#define NNN printf("\n");

int main (int argc, char ** argv) {

	int n;

	scanf("%d", &n);

	int * a = calloc(n * n, sizeof(int));
	int * b = calloc(n * n, sizeof(int));
	int * c = calloc(n * n, sizeof(int));

	for (int i = 0; i < n*n; i++) scanf("%d", a + i);
	for (int i = 0; i < n*n; i++) scanf("%d", b + i);

	
	double begin = omp_get_wtime();

	#pragma omp parallel for schedule(dynamic,1)
	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			for (int k = 0; k < n; k++){
				c[i*n+j] += a[i*n+k] * b[k*n+j];
			}
		}
	}

	double end = omp_get_wtime();
	double time_spent = (end - begin);

	if (argc != 1) {
		printf("time: %lg\n", time_spent);
	} else {
		for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++){
				printf("%d ", c[i*n+j]);
			}	printf("\n");
		}
	}

	return 0;
}
