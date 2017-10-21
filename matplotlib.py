#1
import matplotlib.pyplot as plt
import numpy as np

x = np.linespace(0, 10, 100)

plt.plot(x, np.sin(x))

plt.plot(x, np.cos(x))

plt.show()

#What would be a good example for this problem? 


#2

import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
x = np.linspace(0, 100, 2500)
y = np.sin(x)
ax.plot(x, y, 'r-', linewidth=4, label='sine function', alpha=0.6)
ax.legend()
plt.show()
