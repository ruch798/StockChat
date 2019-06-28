from copy import deepcopy
import pickle
import numpy as np


filename="Classifier/Predictor MLP TECHM"
ptechm=pickle.load(open(filename,"rb"))

filename="Classifier/Predictor MLP SBIN"
psbin=pickle.load(open(filename,"rb"))

filename="Classifier/Predictor MLP BAJAJ-AUTO"
pbajaj=pickle.load(open(filename,"rb"))

filename="Classifier/Predictor MLP ONGC"
pongc=pickle.load(open(filename,"rb"))

filename="Classifier/Predictor MLP TATAMOTORS"
ptatamotors=pickle.load(open(filename,"rb"))

filename="Classifier/Predictor MLP TATASTEEL"
ptatasteel=pickle.load(open(filename,"rb"))



techm=np.load("Classifier/inputs TECHM.npy")
bajaj=np.load("Classifier/inputs BAJAJ-AUTO.npy")
ongc=np.load("Classifier/inputs ONGC.npy")
sbin=np.load("Classifier/inputs SBIN.npy")
tatamotors=np.load("Classifier/inputs TATAMOTORS.npy")
tatasteel=np.load("Classifier/inputs TATASTEEL.npy")

def prediction(model,xs,name):
    output_series = []
    pos=-1
    curr = deepcopy(xs[pos])
    name=name.upper()
    # print(curr.shape)
    for j in range(10):
        # print(curr)
        #print(curr.shape)
        y = model.predict([curr])
        #print(y)
        curr = np.hstack((curr[3:],y[0].T))
        output_series.append(y)
    output_series = np.array(output_series)
    return output_series

def predict1(name):
    d={"techm":techm,"bajaj":bajaj,"ongc":ongc,"sbin":sbin,"tatamotors":tatamotors,"tatasteel":tatasteel}
    pd={"techm":ptechm,"bajaj":pbajaj,"ongc":pongc,"sbin":psbin,"tatamotors":ptatamotors,"tatasteel":ptatasteel}
    return prediction(pd[name],d[name],name)
    
    

#p=prediction(ptechm,techm)
#print(p)
