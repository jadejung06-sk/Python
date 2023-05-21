import matplotlib.pyplot as plt


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