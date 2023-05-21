import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

##### sklearn
# height = np.array([170, 180,160,165,158,176,182,172]).reshape((-1,1)) # x
# weight = [75,81,59,70,55,78,84,72]
# # ordinary least squares : minimum of error
# model = LinearRegression().fit(height, weight)
# ## Regression
# print(model.score(height, weight)) # R2
# print(model.intercept_) # b
# print(model.coef_) # ax
# ## predict
# print(model.predict([[170]]))
# print(model.predict([[170], [180]]))
# print(model.predict(height))
# ## plot and chart
# plt.scatter(height, weight)
# plt.plot(height, model.predict(height))
# plt.show()
#########################

###### statsmodels
height = np.array([170, 180,160,165,158,176,182,172]).reshape((-1,1)) # x
weight = np.array([75,81,59,70,55,78,84,72])
model = sm.OLS(weight, height).fit() # y x
print(model.summary())
# R-squared (uncentered):                   0.993 best 1
# Prob (F-statistic):                    1.03e-08 prob. of a == 0, x == y
# AIC:                                      53.99 best 0
#  P>|t|                                    0.000 best 0(0.05)
# [0.025      0.975]                        coef  0.390 ~ 0.455
#                  coef    std err          t      P>|t|      [0.025      0.975]
# x1             0.4228      0.014     30.603      0.000       0.390       0.455