import random

n = int(input())

name = str(n)+".txt"

fff = open(name, "w")

fff.write(str(n))
fff.write("\n")

for i in range(n):
	for j in range (n):
		fff.write(str(int(random.random()*10)))
		fff.write(" ")
	fff.write("\n")

fff.write("\n")

for i in range(n):
	for j in range (n):
		fff.write(str(int(random.random()*10)))
		fff.write(" ")
	fff.write("\n")
	
fff.close()