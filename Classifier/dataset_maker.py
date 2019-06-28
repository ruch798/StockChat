import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from random import randint
from copy import deepcopy
import pickle

data = pd.read_csv('C:\\Users\\Jasdeep Singh\\PycharmProjects\\test\\Aditya Birla\\Barclays Hackathon\\final_normalized_data.csv')

# data = data.drop(['Date','Series','Close','High','Low','Close','Prev Close','Volume','Turnover','Trades','VWAP','Deliverable Volume',data.keys()[-1]],axis=1)
# print(data.keys())

N = int(input('Enter the history period'))

xs = dict()
ys = dict()

for name in data['Symbol'].unique():
    xs[name] = []
    part = data[data['Symbol']==name]
    for i in range(N,part.shape[0]):
        row = []
        for j in range(i-N,i):
            for k in range(2,len(part.keys())):
                row.append(part.iloc[j,k])
        xs[name].append(row)


for name in data['Symbol'].unique():
    ys[name] = []
    part = data[data['Symbol']==name]
    for i in range(N,part.shape[0]):
        rows = []
        for j in range(2,len(part.keys())):
            rows.append(part.iloc[i,j])
        ys[name].append(rows)

for x in xs.keys():
    xs[x] = np.array(xs[x])
    #print(x)
    #print(xs[x][:10])
    #print(xs[x].shape)

for y in ys.keys():
    ys[y] = np.array(ys[y])
    #print(y)
    #print(ys[y][:5])
    #print(ys[y].shape)

models = dict()
for i in xs.keys():
    models[i] = MLPRegressor(hidden_layer_sizes=[10],solver='lbfgs',max_iter=10000,learning_rate_init=0.1)
    #models[i] = LinearRegression()
    # models[i] = SVR(verbose=True)
    models[i].fit(xs[i],ys[i])
    # print(i)
    # print(models[i].score(xs[i],ys[i].T[0].T))

# print(models['SBIN'])

# plotting
# for i in xs.keys():
#     y = models[i].predict(xs[i])
#     plt.plot([_ for _ in range(len(xs[i]))], y)
#     plt.plot([_ for _ in range(len(xs[i]))], ys[i].T[0].T)
#     plt.show()

# practical testing
pos = randint(0,xs[i].shape[0])
# print(xs[i][pos])

for i in xs.keys():
    pickle.dump(models[i],open('C:\\Users\\Jasdeep Singh\\PycharmProjects\\test\\Aditya Birla\\Barclays Hackathon\\'+'Predictor MLP '+i,'wb'))

for i in xs.keys():
    output_series = []
    curr = deepcopy(xs[i][pos])
    # print(curr.shape)
    for j in range(10):
        # print(curr)
        print(curr.shape)
        y = models[i].predict([curr])
        print(y)
        curr = np.hstack((curr[3:],y[0].T))
        output_series.append(y)
    output_series = np.array(output_series)
    plt.plot([_ for _ in range(len(ys[i][pos:pos+11]))],ys[i][pos:pos+11].T[0].T)
    plt.plot([m for m in range(len(output_series))],output_series.T[0].T)
    plt.show()