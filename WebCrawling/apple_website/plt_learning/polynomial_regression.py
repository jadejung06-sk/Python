import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import statsmodels.api as sm


##### scipy.optimize
# df = pd.read_table(r"D:\2022\Python\WebCrawling\apple_website\plt_learning\income.txt")
# df = df.dropna()
# plt.scatter(df.age, df.income)
# def func(x, a, b, c):
#     return a*x + b*x**2 + c #  
# # def func(x, a, b, c, d):
# #     return a*x + b*x**2 + c*x**3 + d #  
# opt, cuv = curve_fit(func, df.age, df.income) # func, x, y
# # x = [1,2,3,4,5,6] # TypeError: can't multiply sequence by non-int of type 'numpy.float64'
# x = np.array([1,2,3,4,5,6])
# plt.plot(x, func(x, opt[0], opt[1], opt[2]), color = 'crimson')
# plt.show()


##### statsmodel.api
df = pd.read_table(r"D:\2022\Python\WebCrawling\apple_website\plt_learning\income.txt")
df = df.dropna()
plt.scatter(df.age, df.income)

x = np.column_stack([df['age'], df['age']**2, np.ones(79)]) # ax + bx^2 + 1
model = sm.OLS(df["income"], x).fit()
print(model.summary())
plt.show()

#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# x1            73.2448      5.195     14.100      0.000      62.899      83.591
# x2            -8.4267      0.731    -11.531      0.000      -9.882      -6.971
# const         -7.0077      9.126     -0.768      0.445(bad)     -25.184      11.169

# x2 = np.column_stack([df['age'], df['age']**2, np.ones(79)]) # ax + bx^2 + 1 [[ 4. 16.  1.]]
x2 = np.column_stack([df['age'], df['age']**2]) # ax + bx^2  [[ 4. 16.]]
print(x2)
model2 = sm.OLS(df["income"], x2).fit()
print(model2.summary())
plt.show()
## overfitting : no prediction only for train dataset
