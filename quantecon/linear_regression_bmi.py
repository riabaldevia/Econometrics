import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#read data
dataframe = pd.read_csv('quantecon_data/bmi.csv')
x_values = dataframe[['BMI']] 
y_values = dataframe[['Life expectancy']]

#train data
model = LinearRegression()
model.fit(x_values, y_values)

#visualize the data
plt.scatter(x_values, y_values)
plt.plot(x_values, model.predict(x_values))
