## When working with econometrics, you'll use lots of plots (or some other visualization).

### Example 1
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linespace(0, 10, 100)

plt.plot(x, np.sin(x))

plt.plot(x, np.cos(x))

plt.show()
```

![](https://github.com/riabaldevia/Econometrics/blob/master/figures/figure_1.png)
