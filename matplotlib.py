#1
import matplotlib.pyplot as plt
import numpy as np

x = np.linespace(0, 10, 100)

plt.plot(x, np.sin(x))

plt.plot(x, np.cos(x))

plt.show()
