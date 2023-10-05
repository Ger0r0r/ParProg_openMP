#include <stdio.h>
#include <omp.h>
#include <unistd.h>
#include <sys/types.h>

#define NNN printf("\n");

int sum_1 = 0;
#pragma omp threadprivate(sum_1)

int main () {

	// omp_set_num_threads(1<<7);

	#pragma omp parallel copyin(sum_1)
	{
		#pragma omp master
		{
			sum_1 = 99;
		}
 
		#pragma omp barrier
 
		printf("(%d) sum_1 = %d\n", omp_get_thread_num(), sum_1);
	}
	NNN
 
	#pragma omp parallel copyin(sum_1)
	{
		printf("(%d) sum_1 = %d\n", omp_get_thread_num(), sum_1);
	}
	NNN NNN

	int sum_2 = 123;
 
	#pragma omp parallel default(none) firstprivate(sum_2)
	{
		printf("(%d) sum_2 = %d\n", omp_get_thread_num(), sum_2);
 
		#pragma omp barrier
 
		#pragma omp single copyprivate(sum_2)
		{	
			NNN
			sum_2 = 456;
			printf("(%d) change sum_2 = %d\n", omp_get_thread_num(), sum_2);
			NNN
		}
		printf("(%d) sum_2 = %d\n", omp_get_thread_num(), sum_2);
	}

	return 0;
}