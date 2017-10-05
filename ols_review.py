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

#Example 2 with ScikitLearn
import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model

X_train = np.c_[.5, 1].T
y_train = [.5, 1]
X_test = np.c_[0, 2].T

np.random.seed(0)

classifiers = dict(ols=linear_model.LinearRegression(),
                   ridge=linear_model.Ridge(alpha=.1))

fignum = 1
for name, clf in classifiers.items():
    fig = plt.figure(fignum, figsize=(4, 3))
    plt.clf()
    plt.title(name)
    ax = plt.axes([.12, .12, .8, .8])

    for _ in range(6):
        this_X = .1 * np.random.normal(size=(2, 1)) + X_train
        clf.fit(this_X, y_train)

        ax.plot(X_test, clf.predict(X_test), color='.5')
        ax.scatter(this_X, y_train, s=3, c='.5', marker='o', zorder=10)

    clf.fit(X_train, y_train)
    ax.plot(X_test, clf.predict(X_test), linewidth=2, color='blue')
    ax.scatter(X_train, y_train, s=30, c='r', marker='+', zorder=10)

    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_ylim((0, 1.6))
    ax.set_xlabel('X')
    ax.set_ylabel('y')
    ax.set_xlim(0, 2)
    fignum += 1

plt.show()
