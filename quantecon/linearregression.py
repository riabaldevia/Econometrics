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

#Other examples that can be utilized for econometrics; related to income and education levels.


#Example 2

import numpy as np
a = 6;b = 1 # parameters to estimate
x = np.linspace(0,1,100)
y = a*x + np.random.randn(len(x))+b
p,var_=np.polyfit(x,y,1,cov=True) # fit data to line
y_ = np.polyval(p,x) # estimated by linear regression
