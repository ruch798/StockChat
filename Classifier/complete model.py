import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
import numpy as np

## pre-processing
data = pd.read_csv('C:\\Users\\Jasdeep Singh\\PycharmProjects\\test\\Aditya Birla\\Barclays Hackathon\\data.csv')

x = np.load('C:\\Users\\Jasdeep Singh\\PycharmProjects\\test\\Aditya Birla\\Barclays Hackathon\\previous 5 data points.npy')
print(np.mean(x))
x = preprocessing.scale(x)
y = np.load('C:\\Users\\Jasdeep Singh\\PycharmProjects\\test\\Aditya Birla\\Barclays Hackathon\\previous 5 data outputs.npy')
y = y.T[:-2].T
y = preprocessing.scale(y)

model = LinearRegression()

model.fit(x,y)
s = model.score(x,y)
print(s)

print(model.coef_)
