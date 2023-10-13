#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <omp.h>
#include <unistd.h>
#include <sys/types.h>

#define NNN printf("\n");

int main () {

	int max_i = 65;

	omp_set_num_threads(1<<2);

	char out[256] = {0};
	char buf[256] = {0};

	#pragma omp parallel for 
		for (int i = 0; i < max_i; ++i) {
			sprintf(buf, "%d ", i);
			strcat(out, buf);
			printf("(%d) %d\n", omp_get_thread_num(), i);
		}
	NNN
	#pragma omp parallel 
	{
		printf("(%d) %s\n", omp_get_thread_num(), out);
	}

	return 0;
}