import numpy as np
import matplotlib.pyplot as plt
import os
from subprocess import Popen, PIPE, STDOUT
import sys
from progress.bar import IncrementalBar

nums = np.linspace(1,8,8)

mpi_100 = np.array([0.0003273,0.0002956,0.0003296,0.0001358,0.0010776,0.0036665,0.0062456,0.0091637])
single_100 = 0.0003042

mpi_1000 = np.array([0.0424905,0.0250084,0.021567,0.0225214,0.0197578,0.0250853,0.0329943,0.0308312])
single_1000 = 0.03146825

mpi_5000 = np.array([3.4480249,1.9592028,1.4467154,1.2273983,1.5235139,1.2190271,1.3557984,1.0617509])
single_5000 =  0.7918669

xx = np.array([1,8])
yy_100 = np.array([single_100,single_100])
yy_1000 = np.array([single_1000,single_1000])
yy_5000 = np.array([single_5000,single_5000])


plt.plot(nums, mpi_100, "-b")
plt.plot(xx, yy_100, "--b")
plt.show()

plt.plot(nums, mpi_1000, "-b")
plt.plot(xx, yy_1000, "--b")
plt.show()

plt.plot(nums, mpi_5000, "-b")
plt.plot(xx, yy_5000, "--b")
plt.show()
