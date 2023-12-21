import numpy as np
import matplotlib.pyplot as plt
import os
from subprocess import Popen, PIPE, STDOUT
import sys
from progress.bar import IncrementalBar

nums = np.linspace(1,8,8)

omp_100 = np.array([0.00037453,0.00036932,0.00033629,0.00035788,0.00058392,0.00065376,0.00163874,0.00136897])
single_100 = 0.00030295000000000007

omp_1000 = np.array([0.04694306,0.02794962,0.02088652,0.01766937,0.01687343,0.01611557,0.01693899,0.0175699])
single_1000 = 0.029913719999999998

omp_5000 = np.array([1.0740784,0.6671451,0.50475,0.4489869,0.4413938,0.4115116,0.4034633,0.3990168])
single_5000 =  0.7573515000000001

xx = np.array([1,8])

omp_100 = single_100 / omp_100
omp_1000 = single_1000 / omp_1000
omp_5000 = single_5000 / omp_5000

yy_100 = omp_100 / nums
yy_1000 = omp_1000 / nums
yy_5000 = omp_5000 / nums

plt.plot(nums, omp_100, "-b")
plt.xlabel('n')
plt.ylabel('S(n)')
plt.title('Ускорение S(n) 100')
plt.show()
plt.plot(nums, yy_100, "-b")
plt.xlabel('n')
plt.ylabel('E(n)')
plt.title('Эффективность E(n) 100')
plt.show()

plt.plot(nums, omp_1000, "-b")
plt.xlabel('n')
plt.ylabel('S(n)')
plt.title('Ускорение S(n) 1000')
plt.show()
plt.plot(nums, yy_1000, "-b")
plt.xlabel('n')
plt.ylabel('E(n)')
plt.title('Эффективность E(n) 1000')
plt.show()

plt.plot(nums, omp_5000, "-b")
plt.xlabel('n')
plt.ylabel('S(n)')
plt.title('Ускорение S(n) 5000')
plt.show()
plt.plot(nums, yy_5000, "-b")
plt.xlabel('n')
plt.ylabel('E(n)')
plt.title('Эффективность E(n) 5000')
plt.show()
