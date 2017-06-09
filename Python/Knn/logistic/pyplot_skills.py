import matplotlib.pyplot as plt
from mpmath import linspace, sin
import numpy as np

t1 = np.arange(0.0, 4.0, 0.2)
print('t1 = ', t1)
t2 = np.arange(0.0, 4.0, 0.01)
print('t2 = ', t2)
fig = plt.figure()
ax1 = fig.add_subplot(221) # 3行1 列，第一位置（左到右，上到下数）， 各个add_subplot独立
line1, = plt.plot(t1, np.sin(2 * np.pi * t1), '--s')  # 有s的话有标点
plt.title('sine function demo')
plt.xlabel('time(s)')
plt.ylabel('votage(mV)')
plt.xlim([0.0, 5.0])
plt.ylim([-1.2, 1.2])
plt.grid('on')

# 面向对象
plt.setp(line1, lw=1.5, c='g')  # 设置line1属性
line1.set_antialiased(False)  # 通过set×设置line1 的属性
plt.text(3.7, 0.1, '$mu=100,\sigma=15$')  # 添加text,也可接收LaTeX
# 第二图
ax2 = fig.add_subplot(223)  # 如果还是211,会画在同一图表内，
plt.plot(t2, np.exp(-t2), ':r')
plt.hold('on')
plt.plot(t2, np.cos(2 * np.pi * t2), '--b')
plt.xlabel('time')
plt.ylabel('amplitude')

# sigmoid
t1 = np.arange(-20.0, 20.0, 0.2)
t2 = 1.0 / (1.0 + np.exp(-t1))
ax3 = fig.add_subplot(1,2,2)
line3, = plt.plot(t1, t2, '--b')
plt.setp(line3, lw=1.6, c='b')
line3.set_antialiased(True)
plt.grid('on')
plt.text(2.0, 0.5, '$\sigma=1/(1+exp(-x))$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('sigmoid function')


#sigmoid事件发生比p/(1-p) = e^(g(x))
# t2 = np.exp()
# ax4 = fig.add_subplot(133)

plt.show()
