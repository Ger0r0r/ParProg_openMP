#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <unistd.h>
#include <sys/types.h>

int main () {

	int value = 0;

	#pragma omp parallel for ordered
		for (int i = 0; i < 8; ++i) {
			#pragma omp ordered
			value += 10;
			printf("(%d)\t%d\n", omp_get_thread_num(), value);
		}

	return 0;
}