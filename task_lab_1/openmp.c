#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <omp.h>

int main(int argc, char **argv) {

	if (argc != 4) {
		printf("Usage: %s <ISIZE> <JSIZE> <NPROC>\n", argv[0]);
		return 0;
	}

	int ISIZE = atoi(argv[1]);
	int JSIZE = atoi(argv[2]);
	int NPROC = atoi(argv[3]);

	double ** a = calloc(ISIZE+1, sizeof(double *));
	for (int i = 0; i < ISIZE; i++){
		a[i] = calloc(JSIZE, sizeof(double));
	}

	int i, j, k;
	int r, c;

	for (i = 0; i < ISIZE; i++){
		for (j = 0; j < JSIZE; j++){
			a[i][j] = 10 * i + j;
		}
	}
	//начало измерения времени
 	double start_time = omp_get_wtime();

	omp_set_num_threads(NPROC);
	#pragma omp parallel for schedule(static,1) private(j,i,k,r,c)
	for (k = 0; k < 8; k++) {
		r = (int)(k / 4);
		c = (k % 4);
		// printf("(%d/%d) I start at %d\n", omp_get_thread_num(), omp_get_max_threads(), k);
		for (i = r; i < ISIZE - 4; i+=2) {
			for (j = c; j < JSIZE - 4; j+=4) {
				a[i][j] = sin(0.1 * a[i + 2][j + 4]);
			}
		}
	}
	//окончание измерения времени
    double end_time = omp_get_wtime();
	double duration = ((end_time - start_time));
	printf("Time: %lg seconds\n", duration);

	#ifdef FILE_LOG
	FILE *ff;
	ff = fopen("answer_openmp.csv","w");
	for(i = 0; i < ISIZE; i++){
		for (j = 0; j < JSIZE; j++){
			fprintf(ff, "%f;", a[i][j]);
		}
		fprintf(ff, "\n");
	}
	fclose(ff);
	#endif

	for (int i = 0; i < ISIZE; i++){
		free(a[i]);
	}
	free(a);
	return 0;
}