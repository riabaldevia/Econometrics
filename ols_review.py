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

# load statsmodels as alias ``sm``
import statsmodels.api as sm

# load a dataset into a pandas data frame - first column (year) used as row labels
df = pd.read_csv('url of dataset', index_col=0)
df.head()
