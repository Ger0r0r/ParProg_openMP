import numpy as np
import matplotlib.pyplot as plt

x = np.array([10,20,50,100,200,500,600,700,800,900,1000])
xx = np.log(x)

w_simple = [9e-6,5.6e-5,0.00058,0.007675,0.080344,1.57246,2.52487,3.97132,5.49496,8.85036,14.4699]
w_simple = np.array(w_simple)
print(w_simple)
w_simple_log = np.log(w_simple)
print(w_simple_log)

w_simple_o = [3e-6,1e-5,0.000125,0.001015,0.001015,0.207425,0.412525,0.854021,1.01371,1.92233,2.2786]
w_simple_o = np.array(w_simple_o)
print(w_simple_o)
w_simple_o_log = np.log(w_simple_o)
print(w_simple_o_log)

w_simple_parr = [0.0038555,0.0041267,0.0006088,0.0071884,0.0183195,0.487267,0.709426,1.05374,1.69649,2.60074,4.11385]
w_simple_parr = np.array(w_simple_parr)
print(w_simple_parr)
w_simple_parr_log = np.log(w_simple_parr)
print(w_simple_parr_log)

w_simple_parr_o = [0.0041732,0.0004143,0.0004744,0.0007531,0.0078908,0.127339,0.165534,0.316075,0.517608,0.818813,1.39156]
w_simple_parr_o = np.array(w_simple_parr_o)
print(w_simple_parr_o)
w_simple_parr_o_log = np.log(w_simple_parr_o)
print(w_simple_parr_o_log)

w_better = [4e-6,3.1e-5,0.000491,0.003435,0.033765,0.610108,1.08735,1.72855,2.72812,3.83966,6.27407]
w_better = np.array(w_better)
print(w_better)
w_better_log = np.log(w_better)
print(w_better_log)

w_better_o = [3e-6,1.1e-5,0.000121,0.001121,0.010612,0.187829,0.360038,0.51488,0.852031,1.32245,2.02537]
w_better_o = np.array(w_better_o)
print(w_better_o)
w_better_o_log = np.log(w_better_o)
print(w_better_o_log)

w_better_parr = [0.0022056,0.0003677,0.0007118,0.0026937,0.0096797,0.202584,0.34949,0.522918,0.944582,1.42615,2.17491]
w_better_parr = np.array(w_better_parr)
print(w_better_parr)
w_better_parr_log = np.log(w_better_parr)
print(w_better_parr_log)

w_better_parr_o = [0.0003987,0.0004191,0.0044865,0.0053042,0.0018887,0.0399776,0.0672856,0.0983281,0.170317,0.305683,0.561775]
w_better_parr_o = np.array(w_better_parr_o)
print(w_better_parr_o)
w_better_parr_o_log = np.log(w_better_parr_o)
print(w_better_parr_o_log)

plt.figure(figsize=[12,7])
plt.plot(xx, w_simple_log, '-', ms = 1)
plt.plot(xx, w_simple_o_log, '-', ms = 1)
plt.plot(xx, w_simple_parr_log, '-', ms = 1)
plt.plot(xx, w_simple_parr_o_log, '-', ms = 1)
plt.plot(xx, w_better_log, '-', ms = 1)
plt.plot(xx, w_better_o_log, '-', ms = 1)
plt.plot(xx, w_better_parr_log, '-', ms = 1)
plt.plot(xx, w_better_parr_o_log, '-', ms = 1)
plt.show()

plt.figure(figsize=[12,7])
plt.plot(x, w_simple, '-', ms = 1)
plt.plot(x, w_simple_o, '-', ms = 1)
plt.plot(x, w_simple_parr, '-', ms = 1)
plt.plot(x, w_simple_parr_o, '-', ms = 1)
plt.plot(x, w_better, '-', ms = 1)
plt.plot(x, w_better_o, '-', ms = 1)
plt.plot(x, w_better_parr, '-', ms = 1)
plt.plot(x, w_better_parr_o, '-', ms = 1)
plt.show()