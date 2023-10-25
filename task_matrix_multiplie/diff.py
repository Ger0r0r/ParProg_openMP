import numpy as np
import matplotlib.pyplot as plt

x = np.array([10,20,50,100,200,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500])
xx = np.log(x)

w_simple = [9e-06,5.71e-05,0.0007896,0.0075638,0.05990060000000001,1.314613,2.392723,4.074334,6.292433000000001,9.81136,15.661350000000002]
w_simple = np.array(w_simple)
print(w_simple)
w_simple_log = np.log(w_simple)
print(w_simple_log)

w_simple_o = [2.9e-06,9.100000000000001e-06,0.00011360000000000001,0.0011009000000000001,0.0076139,0.18829980000000002,0.41383400000000004,0.8560139,0.961815,1.8494890000000002,2.261353,3.7424560000000007,3.9895199999999997,8.036528,9.689328,17.19031]
w_simple_o = np.array(w_simple_o)
print(w_simple_o)
w_simple_o_log = np.log(w_simple_o)
print(w_simple_o_log)

w_simple_parr = [0.0051107800000000005,0.0035002099999999993,0.0027001699999999996,0.006266290000000001,0.02641669,0.4067852,0.7150097,1.139526,1.6998559999999998,2.7542169999999997,4.507630000000001,6.4653079999999985,8.739087999999999,12.01181]
w_simple_parr = np.array(w_simple_parr)
print(w_simple_parr)
w_simple_parr_log = np.log(w_simple_parr)
print(w_simple_parr_log)

w_simple_parr_o = [0.0038419599999999997,0.00238276,0.00045541,0.004142290000000001,0.00693509,0.10293807000000002,0.183506,0.3077423,0.4784821999999999,0.8279185000000002,1.4816289999999999,2.6266949999999993,3.0731289999999998,5.022247,6.158098,9.090214,11.278490000000001]
w_simple_parr_o = np.array(w_simple_parr_o)
print(w_simple_parr_o)
w_simple_parr_o_log = np.log(w_simple_parr_o)
print(w_simple_parr_o_log)

w_better = [5.3e-06,3.25e-05,0.00038920000000000003,0.0032503,0.030189100000000003,0.5251335999999999,0.9900585,1.5953130000000002,2.643735,4.171722000000001,6.630795999999999,9.428253999999999,13.21215]
w_better = np.array(w_better)
print(w_better)
w_better_log = np.log(w_better)
print(w_better_log)

w_better_o = [3.4e-06,1.1099999999999999e-05,0.0001176,0.0011815,0.0098757,0.1616188,0.3223808,0.5828131000000002,0.7896281,1.288331,1.7953689999999998,2.575402,3.0856869999999996,4.990259,6.199337999999999,8.261609,12.924520000000001]
w_better_o = np.array(w_better_o)
print(w_better_o)
w_better_o_log = np.log(w_better_o)
print(w_better_o_log)

w_better_parr = [0.00402918,0.00160741,0.0016166,0.0052429700000000004,0.013635239999999998,0.1822,0.3550595,0.5920004999999999,0.9088338,1.3823150000000004,2.101044,3.179882,4.319379,5.903742000000001,7.892417,9.888434,12.03191]
w_better_parr = np.array(w_better_parr)
print(w_better_parr)
w_better_parr_log = np.log(w_better_parr)
print(w_better_parr_log)

w_better_parr_o = [0.00040947999999999994,0.0004017099999999999,0.00043152999999999996,0.00062277,0.00650014,0.04035574000000001,0.07206657000000001,0.113201,0.17971589999999998,0.3198312,0.5197776999999999,0.7386853999999999,0.9581227999999999,1.4622490000000001,1.9101839999999999,2.6506920000000003,3.63786,4.4322539999999995,5.540208,6.68785,6.725174,8.615374,10.298583]
w_better_parr_o = np.array(w_better_parr_o)
print(w_better_parr_o)
w_better_parr_o_log = np.log(w_better_parr_o)
print(w_better_parr_o_log)

plt.figure(figsize=[12,7])
plt.plot(xx[0:11], w_simple_log, '-', ms = 1)
plt.plot(xx[0:16], w_simple_o_log, '-', ms = 1)
plt.plot(xx[0:14], w_simple_parr_log, '-', ms = 1)
plt.plot(xx[0:17], w_simple_parr_o_log, '-', ms = 1)
plt.plot(xx[0:13], w_better_log, '-', ms = 1)
plt.plot(xx[0:17], w_better_o_log, '-', ms = 1)
plt.plot(xx[0:17], w_better_parr_log, '-', ms = 1)
plt.plot(xx[0:23], w_better_parr_o_log, '-', ms = 1)
plt.legend (('Простой', 'Простой О', 'Простой Пар', 'Простой Пар О', 'Улучшенный', 'Улучшенный О', 'Улучшенный Пар', 'Улучшенный Пар О'))
plt.show()

plt.figure(figsize=[12,7])
plt.plot(x[0:11], w_simple, '-', ms = 1)
plt.plot(x[0:16], w_simple_o, '-', ms = 1)
plt.plot(x[0:14], w_simple_parr, '-', ms = 1)
plt.plot(x[0:17], w_simple_parr_o, '-', ms = 1)
plt.plot(x[0:13], w_better, '-', ms = 1)
plt.plot(x[0:17], w_better_o, '-', ms = 1)
plt.plot(x[0:17], w_better_parr, '-', ms = 1)
plt.plot(x[0:23], w_better_parr_o, '-', ms = 1)
plt.legend (('Простой', 'Простой О', 'Простой Пар', 'Простой Пар О', 'Улучшенный', 'Улучшенный О', 'Улучшенный Пар', 'Улучшенный Пар О'))
plt.show()