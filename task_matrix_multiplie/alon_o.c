#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NNN printf("\n");

int main (int argc, char ** argv) {

	int n,i,j,k;

	scanf("%d", &n);

	int * a = calloc(n * n, sizeof(int));
	int * b = calloc(n * n, sizeof(int));
	int * c = calloc(n * n, sizeof(int));

	for (i = 0; i < n*n; i++) scanf("%d", a + i);
	for (i = 0; i < n*n; i++) scanf("%d", b + i);
	
	clock_t begin = clock();
	int *f, *g, *h;
	double s1 = 0, s2 = 0, s3 = 0, s4 = 0;

	for (i = 0; i < n-1; i+=2){
		f = a + i * n;
		for (j = 0; j < n-1; j+=2) {
			g = b + j;
			for (k = 0; k < n; k++){
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

	clock_t end = clock();
	double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;

	if (argc != 1) {
		printf("time: %lg\n", time_spent);
	} else {
		for (i = 0; i < n; i++){
			for (j = 0; j < n; j++){
				printf("%d ", c[i*n+j]);
			}	printf("\n");
		}
	}

	return 0;
}
