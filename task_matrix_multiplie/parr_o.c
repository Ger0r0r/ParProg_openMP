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
	for (int i = 0; i < n-1; i+=2){
		int *f, *g, *h;
		double s1 = 0, s2 = 0, s3 = 0, s4 = 0;
		f = a + i * n;
		for (int j = 0; j < n-1; j+=2) {
			g = b + j;
			for (int k = 0; k < n; k++){
				s1 += f[k] * g[n*k];	
				s3 += f[k] * g[n*k+1];	
				s2 += f[n+k] * g[n*k];	
				s4 += f[n+k] * g[n*k+1];	
			}
			h = c + i * n + j;
			h[0] = s1; s1=0;
			h[n] = s2; s2=0;
			h[1] = s3; s3=0;
			h[n+1] = s4; s4=0;
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
