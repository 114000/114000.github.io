import numpy as np
import matplotlib.pylab as plt

step = lambda x: np.array(x > 0, dtype = np.int)
sigmoid = lambda x: 1 / (1 + np.exp(-x))


x1 = np.arange(-5.0, 5.0, 0.1)
y1 = step(x1)

# x2 = np.array([-1.0, 1.0, 2.0])
y2 = sigmoid(x1)

plt.plot(x1, y2)
plt.ylim(-0.1, 1.1)
plt.show()