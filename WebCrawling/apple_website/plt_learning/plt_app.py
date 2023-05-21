import matplotlib.pyplot as plt


##### multiple line plots in a graph
plt.figure(figsize = (20, 10)) # inch
plt.plot([1,2,3], [10,20,30])
plt.plot([1,2,3], [20,40,60])
plt.plot([1,2,3], [30,60,90])
plt.show()

##### line plot : time series
plt.plot([1,2,3], [4,5,6]) # x y list
# plt.plot(df.index, df['Close'], color = 'crimson") # x y Series object
plt.xlabel('time')
plt.ylabel('price')
# plt.legend()
plt.legend(['apple'])
plt.show()

##### bar chart : few time series data & frequency of categorical data
plt.bar([1,2,3], [10,20,30]) # x y list
# plt.bar(df.index, df['Close'], color = 'crimson") # x y Series object
plt.show()

##### pie chart : ratio of only one data
plt.pie([57,35,11], labels = ['ramen', 'tuna', 'snack'])
plt.show()

##### histogram chart : distribution and mode of data
plt.hist([160, 165, 170, 171, 172, 180])
plt.show()

##### scatter chart : distribution(proportionality) of two or more than data
math = [5,8, 23, 5, 67, 34, 34, 23]
eng = [23,6, 3, 1, 5, 45, 54, 34]
plt.scatter(math, eng)
plt.show()

##### stack plot : accumulation of data
plt.stackplot([1,2,3], [10, 20, 30], [30,20,50]) # x y1 y2 y3 ...
plt.show()


##### test : label, legend, multiple line plots
# plt.plot(df1.index, df1['rolling5'])
# plt.plot(df1.index, df1['rolling20'])
# plt.plot(df1.index, df1['rolling60'])
# plt.xlabel('Time')
# plt.ylabel('Price')
# plt.legend(['rolling5', 'rolling20', 'rolling60'])
# plt.show()

##### test : bar chart using filtered data
# plt.figure(figsize = (20, 10))
# plt.bar(df1[df1['Volume'] > df1['Volume'].mean()]['Volume'].index, df1[df1['Volume'] > df1['Volume'].mean()]['Close'])
# plt.show()
