import numpy as np
import matplotlib.pyplot as plt
import os
from subprocess import Popen, PIPE, STDOUT
import sys
from progress.bar import IncrementalBar

print(type(sys.argv))
print('The command line arguments are:')
for i in sys.argv:
    print(i)


if (len(sys.argv) != 3):
    print("Usage " + sys.argv[0],sys.argv[1],"<ISIZE> <JSIZE>")
    exit()

sum_time = 0
med_time = 0
med_time_s = 0
med_time_m = np.zeros(8)
med_time_f = np.zeros(8)
data = 0

bar_s = IncrementalBar('Done', max = 100)

for i in range(100):
	p = Popen(["./run_single_mpi", sys.argv[1], sys.argv[2]], stdout=PIPE, stdin=PIPE, stderr=PIPE)
	stdout_data = p.communicate(input=data)[0]

	data_out = stdout_data.decode('ascii')
	data_out = data_out.split(" ")
	time = float(data_out[1])

	sum_time += time
	med_time = sum_time / (i + 1)	

	# print("Iteration " + str(i+1) + ", \tTime: " + "{:.5f}".format(time) + ", \tSum: " + "{:.5f}".format(sum_time) + ", \tMedian: " + "{:.5f}".format(med_time))
	bar_s.next()
bar_s.finish()

med_time_s = med_time
sum_time = 0
med_time = 0
print("")
print("Single "+str(med_time_s))
print("")

bar_m = IncrementalBar('Done', max = 800)
for j in range(8):
	sum_time = 0
	med_time = 0
	for i in range(100):
		p = Popen(["mpirun", "-n="+str(j+1), "./run_mpi", sys.argv[1], sys.argv[2]], stdout=PIPE, stdin=PIPE, stderr=PIPE)
		stdout_data = p.communicate(input=data)[0]

		data_out = stdout_data.decode('ascii')
		data_out = data_out.split(" ")
		time = float(data_out[1])

		sum_time += time
		med_time = sum_time / (i + 1)	

		# print("Iteration " + str(i+1) + ", \tTime: " + "{:.5f}".format(time) + ", \tSum: " + "{:.5f}".format(sum_time) + ", \tMedian: " + "{:.5f}".format(med_time))
		bar_m.next()
	# print("")
	# print("")
	med_time_m[j] = med_time
bar_m.finish()

# sum_time = 0
# med_time = 0

# for j in range(8):
# 	sum_time = 0
# 	med_time = 0
# 	for i in range(100):
# 		p = Popen(["./run_openmp",sys.argv[1], sys.argv[2], str(j+1)], stdout=PIPE, stdin=PIPE, stderr=PIPE)
# 		stdout_data = p.communicate(input=data)[0]

# 		data_out = stdout_data.decode('ascii')
# 		data_out = data_out.split(" ")
# 		time = float(data_out[1])

# 		sum_time += time
# 		med_time = sum_time / (i + 1)	

# 		print("Iteration " + str(i+1) + ", \tTime: " + "{:.5f}".format(time) + ", \tSum: " + "{:.5f}".format(sum_time) + ", \tMedian: " + "{:.5f}".format(med_time))
# 	print("")
# 	print("")
# 	med_time_m[j] = med_time

print("Single "+str(med_time_s))
print("MPI "+str(med_time_m))