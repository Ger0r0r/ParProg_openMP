import numpy as np
import matplotlib.pyplot as plt
import os
from subprocess import Popen, PIPE, STDOUT
import sys
from progress.bar import IncrementalBar

nums = np.linspace(1,8,8)

mpi_100 = np.array([0.0003273,0.0002956,0.0003296,0.0001358,0.0010776,0.0036665,0.0062456,0.0091637])
single_100 = 0.0003042

mpi_1000 = np.array([0.0404491,0.0286043,0.0207443,0.0217642,0.0185118,0.0205726,0.0213544,0.0211399])
single_1000 = 0.03146825

mpi_5000 = np.array([3.27719,2.0216729,1.6095829,1.3380802,1.4821131,1.6788025,1.6863472,1.1498402])
single_5000 =  0.7918669

xx = np.array([1,8])

mpi_100 = single_100 / mpi_100
mpi_1000 = single_1000 / mpi_1000
mpi_5000 = single_5000 / mpi_5000

yy_100 = mpi_100 / nums
yy_1000 = mpi_1000 / nums
yy_5000 = mpi_5000 / nums

plt.plot(nums, mpi_100, "-b")
plt.xlabel('n')
plt.ylabel('S(n)')
plt.title('Ускорение S(n) 100')
plt.show()
plt.plot(nums, yy_100, "-b")
plt.xlabel('n')
plt.ylabel('E(n)')
plt.title('Эффективность E(n) 100')
plt.show()

plt.plot(nums, mpi_1000, "-b")
plt.xlabel('n')
plt.ylabel('S(n)')
plt.title('Ускорение S(n) 1000')
plt.show()
plt.plot(nums, yy_1000, "-b")
plt.xlabel('n')
plt.ylabel('E(n)')
plt.title('Эффективность E(n) 1000')
plt.show()

plt.plot(nums, mpi_5000, "-b")
plt.xlabel('n')
plt.ylabel('S(n)')
plt.title('Ускорение S(n) 5000')
plt.show()
plt.plot(nums, yy_5000, "-b")
plt.xlabel('n')
plt.ylabel('E(n)')
plt.title('Эффективность E(n) 5000')
plt.show()
