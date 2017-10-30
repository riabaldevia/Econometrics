import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

dataframe = pd.read_csv('data/bmi_and_life_expectancy.csv')
x_values = dataframe[['BMI']] 
y_values = dataframe[['Life expectancy']]

model = LinearRegression()
model.fit(x_values, y_values)


plt.scatter(x_values, y_values)
plt.plot(x_values, model.predict(x_values))
