import numpy as np
import matplotlib.pyplot as plt
import os
from subprocess import Popen, PIPE, STDOUT
import sys

names = ["10","20","50","100","200","500","600","700","800","900","1000","1100","1200","1300","1400","1500","1600","1700","1800","1900","2000","2100","2200","2300","2400","2500"]
result = names.copy()
for i in range(len(names)):
	result[i] = 0

print(result)
i = 0
med_time = 0
sum_time = 0


while med_time < 10:
	full_name = "./tests/" + names[i] + ".txt"
	test = open(full_name, "rb")
	data = test.read()
	test.close()
	print("Test ", str(i+1) + " with " + names[i])

	sum_time = 0
	med_time = 0

	for j in range(10):

		p = Popen(["./run", "TIME"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
		stdout_data = p.communicate(input=data)[0]

		data_out = stdout_data.decode('ascii')
		data_out = data_out.split(" ")
		time = float(data_out[1])

		sum_time += time
		med_time = sum_time / (j + 1)	

		print("Iteration " + str(j+1) + ", Time: " + str(time) + ", Sum: " + str(sum_time) + ", Median: " + str(med_time))
	result[i] = med_time
	i += 1
	

print("")
print("")

long_name = str(result[0])

for i in range(len(names)):
	if result[i] != 0:
		print(names[i] + "\t\t" + str(result[i]))
	if i != 0:
		long_name += "," + str(result[i])
  
print(long_name)