from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model as lm
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import max_error

data = pd.read_csv('data_C02_emission.csv')

input_variables = ['Fuel Type','Engine Size (L)','Cylinders','Fuel Consumption City (L/100km)','Fuel Consumption Hwy (L/100km)','Fuel Consumption Comb (L/100km)','Fuel Consumption Comb (mpg)','CO2 Emissions (g/km)']
output = 'CO2 Emissions (g/km)'

X = data[input_variables]
y = data[output]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state=1)

ohe = OneHotEncoder()
X_encoded_train = ohe.fit_transform(X_train[['Fuel Type']]).toarray()
X_encoded_test = ohe.fit_transform(X_test[['Fuel Type']]).toarray()

linearModel = lm.LinearRegression()
linearModel.fit(X_encoded_train, y_train)

y_test_p = linearModel.predict(X_encoded_test)

ME = max_error(y_test, y_test_p)
print(f"Max Error: {ME}")