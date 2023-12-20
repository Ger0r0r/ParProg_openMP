#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <mpi.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>	
		
// #define ISIZE 100
// #define JSIZE 100

#define BORDERS 0

int main(int argc, char **argv) {

	if (argc != 3) {
		printf("Usage: %s <ISIZE> <JSIZE>\n", argv[0]);
		return 0;
	}

	int ISIZE = atoi(argv[1]);
	int JSIZE = atoi(argv[2]);

    // const int SIZE = ISIZE*JSIZE;

	int i, j;
	int rank, size;

	double ** a = calloc(ISIZE+1, sizeof(double *));
	for (int i = 0; i < ISIZE; i++){
		a[i] = calloc(JSIZE, sizeof(double));
	}
	

	// printf("%p\n", a);

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	// printf("(%d/%d) %p\n", rank, size, a);

	// объявление буфера для передачи данных
	double * buf = calloc(1, sizeof(double));
	char * ppp = calloc(10000, sizeof(char));
	MPI_Status status;
	MPI_Request request;

	// создание начального массива
	for (i = 0; i < ISIZE; i++){
		for (j = 0; j < JSIZE; j++){
			a[i][j] = 10 * i + j;
		}
	}
	// начало измерения времени
	double start_time = MPI_Wtime();

	for (int k = rank; k < 8; k+=size) {
		for (int j = 8 + k; j < JSIZE; j+=8) {
			for (int i = 1; i < ISIZE; i++) {
				a[i][j] = sin(5 * a[i - 1][j - 8]);
			}
		}
	}

	// окончание измерения времени
	MPI_Barrier(MPI_COMM_WORLD);
	double end_time = MPI_Wtime();
	double * buffer = calloc(ISIZE, sizeof(double));

	#ifdef FILE_LOG
	
	for (int k = rank; k < 8; k+=size) {
		for (int j = 8 + k; j < JSIZE; j+=8) {
			for (int i = 1; i < ISIZE; i++) {
				buffer[i-1] = a[i][j];
				// printf("(%d/%d) send %lg\n", rank+1, size, a[i][j]);
			}
			// printf("(%d/%d) all send %d\n", rank+1, size, j);
			MPI_Isend(buffer, ISIZE - 1, MPI_DOUBLE, 0, j, MPI_COMM_WORLD, &request);
		}
	}

	if (rank == 0) {
		for (int j = 8; j < JSIZE; j++) {
			// printf("(%d/%d) wait for %d\n", rank+1, size, j);
			MPI_Recv(buffer, ISIZE - 1, MPI_DOUBLE, MPI_ANY_SOURCE, j, MPI_COMM_WORLD, &status);
			// printf("(%d/%d) get %d\n", rank+1, size, j);
			for (int i = 1; i < ISIZE; i++) {
				// bzero(ppp, 10000);
				// sprintf(ppp, "%lg ", buffer[i]);
				a[i][j] = buffer[i-1];
				// printf("(%d/%d) save %lg\n", rank+1, size, buffer[i-1]);
			}
		}
	}
	

	FILE *ff;
	if (rank == 0) {
		ff = fopen("result_mpi.csv", "w");
		for (i = 0; i < ISIZE; i++) {
			for (j = 0; j < JSIZE; j++) {
				fprintf(ff, "%f\t;", a[i][j]);
			}
			fprintf(ff, "\n");
		}
		fclose(ff);

	}
	#endif

	if (rank == 0) {
		printf("Time: %f seconds\n", end_time - start_time);
	}

	MPI_Finalize();


	free(buf);
	free(ppp);
	for (int i = 0; i < ISIZE; i++){
		free(a[i]);
	}
	free(a);

	return 0;
}