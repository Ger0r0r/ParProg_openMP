#include <stdio.h>
#include <omp.h>
#include <unistd.h>
#include <sys/types.h>

int main () {

	// omp_set_num_threads(1<<7);
	omp_set_nested(1);
	omp_set_num_threads(2);

	#pragma omp parallel 
	{	
		printf("AAAA\t(%d) of (%d) \tMy level - %d\tmy parent thread - %d\n", omp_get_thread_num(), omp_get_max_threads(), omp_get_level(),omp_get_ancestor_thread_num(omp_get_level()-1));
		omp_set_num_threads(3);
		#pragma omp parallel
		{
			printf("BBBB\t(%d) of (%d) \tMy level - %d\tmy parent thread - %d\n", omp_get_thread_num(), omp_get_max_threads(), omp_get_level(),omp_get_ancestor_thread_num(omp_get_level()-1));
			omp_set_num_threads(4);
			#pragma omp parallel
			{
				printf("CCCC\t(%d) of (%d) \tMy level - %d\tmy parent thread - %d\n", omp_get_thread_num(), omp_get_max_threads(), omp_get_level(),omp_get_ancestor_thread_num(omp_get_level()-1));
			}
		}
	}

	return 0;
}