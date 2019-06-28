from nsepy import get_history
from datetime import date
import matplotlib.pyplot as plt
import pandas as pd

tickers  = ['TATAMOTORS','ONGC','NGHC','SRIRAM','BOI','SUD','TECHM','BAJAJ-AUTO','TATAMOTORS','TATASTEEL']
total = get_history(symbol="SBIN", start=date(2018,1,1), end=date(2019,6,1))

for i in tickers:
    data = get_history(symbol=i, start=date(2018,6,27), end=date(2019,6,27))
    total = pd.concat([total, data])
    print(i)

total.to_csv('C:\\Users\\Jasdeep Singh\\PycharmProjects\\test\\Aditya Birla\\Barclays Hackathon\\data_final_NSE.csv')


