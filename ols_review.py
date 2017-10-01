#Example 1
import numpy as np
import statsmodels.api as sm
from pandas.core import datetools
import statsmodels.formula.api as smf
dat = sm.datasets.get_rdataset("Guerry", "HistData").data
results = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=dat).fit()
print(results.summary())


#Results are in ols_review.txt
#Source: Seabold, Skipper, and Josef Perktold. “Statsmodels: Econometric and statistical modeling with python.” Proceedings of the 9th Python in Science Conference. 2010.


#Example 2

import numpy as np
import pandas as pd

#Explain

# load statsmodels as alias ``sm``
import statsmodels.api as sm

#Explain 

# load a dataset into a pandas data frame - first column (year) used as row labels
df = pd.read_csv('url of dataset', index_col=0)
df.head()

#Explain
y = df.Employed  # response
X = df.GNP  # predictor
X = sm.add_constant(X)  # Adds a constant term to the predictor
X.head()


#Example 2
import numpy as np
import statsmodels.api as sm

Y = [6,8,3,2,4,1,3,2]
X = range(2,16)
X = sm.add_constant(X)

model = sm.OLS(Y,X)
results = model.fit()
results.params

#tvalues
results.tvalues

#print
print(results.t_test([1, 0]))

#print
#replace x with an integer
print(results.f_test(np.identity(x)))

