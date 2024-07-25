import matplotlib.pyplot as  plt
import numpy as np

x=np.arange(-10,10)

plt.subplot(2,3,1)
plt.plot(x, x**2)
plt.plot([0,0,0],[-10,0,100])

plt.subplot(2,3,2)
plt.plot(x, 2*x)
plt.plot([0,0,0],[-10,0,100])

plt.subplot(2,3,3)
plt.plot(x, x**2 + 2*x)
plt.plot([0,0,0],[-10,0,100])

plt.subplot(2,3,4)
plt.plot(x, np.cos(x))
plt.plot([0,0,0],[-10,0,100])


plt.show()