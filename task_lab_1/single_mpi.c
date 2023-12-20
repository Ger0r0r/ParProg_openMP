#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <omp.h>

// #define ISIZE 100
// #define JSIZE 100

#define BORDERS 1

int main(int argc, char **argv) {

	if (argc != 3) {
		printf("Usage: %s <ISIZE> <JSIZE>\n", argv[0]);
		return 0;
	}

	int ISIZE = atoi(argv[1]);
	int JSIZE = atoi(argv[2]);

	double ** a = calloc(ISIZE+1, sizeof(double *));
	for (int i = 0; i < ISIZE; i++){
		a[i] = calloc(JSIZE, sizeof(double));
	}

	int i, j;

	for (i = 0; i < ISIZE; i++){
		for (j = 0; j < JSIZE; j++){
			a[i][j] = 10 * i + j;
		}
	}
	//начало измерения времени
 	double start_time = omp_get_wtime();

	for (i = 1; i < ISIZE; i++){
		for (j = 8; j < JSIZE; j++){
			a[i][j] = sin(5 * a[i - 1][j - 8]);
		}
	}

	//окончание измерения времени
    double end_time = omp_get_wtime();
	double duration = ((end_time - start_time));
	printf("Time: %lg seconds\n", duration);

	#ifdef FILE_LOG
	FILE *ff;
	ff = fopen("answer.csv","w");
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