from numpy import *
import matplotlib.pyplot as plt

# t1 = np.arange(0.0, 4.0, 0.2)
# print('t1 = ', t1)
# t2 = np.arange(0.0, 4.0, 0.01)
# print('t2 = ', t2)
# fig = plt.figure()
# ax1 = fig.add_subplot(221)  # 3行1 列，第一位置（左到右，上到下数）， 各个add_subplot独立
# line1, = plt.plot(t1, np.sin(2 * np.pi * t1), '--s')  # 有s的话有标点
# plt.title('sine function demo')
# plt.xlabel('time(s)')
# plt.ylabel('votage(mV)')
# plt.xlim([0.0, 5.0])
# plt.ylim([-1.2, 1.2])
# plt.grid('on')
# plt.show()

bt = arange(-4.0, 4.0, 0.2)
print(bt)
fig = plt.figure()
ax = fig.add_subplot(111)
t2 = log(e, (1 - bt) / bt) / 2
line1, = plt.plot(bt, t2, '--s')
plt.title('adabost alpha test')
plt.xlim([-5.0, 5.0])
# plt.ylim([0.25,0.75])
plt.grid('on')
plt.show()
