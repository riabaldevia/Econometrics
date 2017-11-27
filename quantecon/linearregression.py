#Source: https://lectures.quantecon.org/py/ols.html

import pandas as pd
df1 = pd.read_stata('https://github.com/QuantEcon/QuantEcon.lectures.code/raw/master/ols/maketable1.dta')
df1.head()

#Output

 shortnam   euro1900  excolony    avexpr  logpgp95  cons1  cons90  democ00a  \
0      AFG   0.000000         1       NaN       NaN      1       2         1   
1      AGO   8.000000         1  5.363636  7.770645      3       3         0   
2      ARE   0.000000         1  7.181818  9.804219    NaN     NaN       NaN   
3      ARG  60.000004         1  6.386364  9.133459      1       6         3   
4      ARM   0.000000         0       NaN  7.682482    NaN     NaN       NaN   

   cons00a    extmort4    logem4  loghjypl  baseco  
0        1   93.699997  4.540098       NaN     NaN  
1        1  280.000000  5.634789 -3.411248       1  
2      NaN         NaN       NaN       NaN     NaN  
3        3   68.900002  4.232656 -0.872274       1  
4      NaN         NaN       NaN       NaN     NaN  

To visualize this:

import matplotlib.pyplot as plt
plt.style.use('seaborn')
df1.plot(x='avexpr', y='logpgp95', kind='scatter')
plt.show()

#Other examples that can be utilized for econometrics; related to income and education levels.


#Example 2

import numpy as np
a = 6;b = 1 # parameters to estimate
x = np.linspace(0,1,100)
y = a*x + np.random.randn(len(x))+b
p,var_=np.polyfit(x,y,1,cov=True) # fit data to line
y_ = np.polyval(p,x) # estimated by linear regression


#Example 3
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# x from 0 to 100
x = 100 * np.random.random((10, 1))

# y = a*x + b with noise
y = 0.25 * x + 2.0 + np.random.normal(size=x.shape)

# create a linear regression model
model = LinearRegression()
model.fit(x, y)

# predict y from the data
x_new = np.linspace(0, 100, 100)
y_new = model.predict(x_new[:, np.newaxis])

# plot the results
plt.figure(figsize=(4, 3))
ax = plt.axes()
ax.scatter(x, y)
ax.plot(x_new, y_new)

ax.set_xlabel('x')
ax.set_ylabel('y')

ax.axis('tight')


plt.show()


#Example 4
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# x from 0 to 100
x = 100 * np.random.random((10, 1))

# y = a*x + b with noise
y = 0.25 * x + 2.0 + np.random.normal(size=x.shape)

# create a linear regression model
model = LinearRegression()
model.fit(x, y)

# predict y from the data
x_new = np.linspace(0, 1000, 150)
y_new = model.predict(x_new[:, np.newaxis])

# plot the results
plt.figure(figsize=(4, 3))
ax = plt.axes()
ax.scatter(x, y)
ax.plot(x_new, y_new)

ax.set_xlabel('x')
ax.set_ylabel('y')

ax.axis('tight')


plt.show()

#Linear regression between stocks SPY and TSLA
import numpy as np
from statsmodels import regression
import statsmodels.api as sm
import matplotlib.pyplot as plt
import math

def linreg(X,Y):
    # Running the linear regression
    X = sm.add_constant(X)
    model = regression.linear_model.OLS(Y, X).fit()
    a = model.params[0]
    b = model.params[1]
    X = X[:, 1]

    # Return summary of the regression and plot results
    X2 = np.linspace(X.min(), X.max(), 100)
    Y_hat = X2 * b + a
    plt.scatter(X, Y, alpha=0.3) # Plot the raw data
    plt.plot(X2, Y_hat, 'r', alpha=0.9);  # Add the regression line, colored in red
    plt.xlabel('X Value')
    plt.ylabel('Y Value')
    return model.summary()
   
start = '2014-01-01'
end = '2015-01-01'
asset = get_pricing('TSLA', fields='price', start_date=start, end_date=end)
benchmark = get_pricing('SPY', fields='price', start_date=start, end_date=end)

# We have to take the percent changes to get to returns
# Get rid of the first (0th) element because it is NAN
r_a = asset.pct_change()[1:]
r_b = benchmark.pct_change()[1:]

linreg(r_b.values, r_a.values)

#Try to do some linear regression problem sets between a cryptocurrency and a non-cryptocurrency.

