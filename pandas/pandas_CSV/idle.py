import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv(r"D:\2022\Python\pandas_CSV\idle_stop.csv", skiprows= [0])
data = data.apply(lambda x : x.str.split(","))
data[['idx','IdleTime', 'StopTime']] = pd.DataFrame(data["0,0.0,0"].tolist(), index= data.index)
data = data.drop('0,0.0,0', axis = 1)
data['IdleTime'] = data['IdleTime'].astype('float32')
data['StopTime'] = data['StopTime'].astype('float32')
print(data.describe())
# data.boxplot()
data['IdleTime'].hist()
print(data[data['IdleTime'] > 60].shape)
plt.show()
print(data.head())

# data.boxplot()
# plt.show()