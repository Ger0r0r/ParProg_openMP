#include <stdio.h>
#include <omp.h>
#include <unistd.h>
#include <sys/types.h>

int main () {

	// omp_set_num_threads(1<<7);

	#pragma omp parallel 
	{
		printf("(%d)\tHello World!\n", omp_get_thread_num());
	}

	return 0;
}