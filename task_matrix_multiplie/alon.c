#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>

int main (int argc, char ** argv) {

	int n;

	scanf("%d", &n);

	int * a = calloc(n * n, sizeof(int));
	int * b = calloc(n * n, sizeof(int));
	int * c = calloc(n * n, sizeof(int));

	int i, j, k;

	for (i = 0; i < n*n; i++) scanf("%d", a + i);
	for (i = 0; i < n*n; i++) scanf("%d", b + i);

	
	clock_t begin = clock();

	for (i = 0; i < n; i++){
		for (j = 0; j < n; j++){
			for (k = 0; k < n; k++){
				c[i*n+j] += a[i*n+k] * b[k*n+j];
			}
		}
	}

	clock_t end = clock();
	double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;

	if (argc != 1) {
		printf("time: %0.6lg\n", time_spent);
	} else {
		for (i = 0; i < n; i++){
			for (j = 0; j < n; j++){
				printf("%d ", c[i*n+j]);
			}	printf("\n");
		}
	}

	return 0;
}
