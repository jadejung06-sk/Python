import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


height = np.array([170, 180,160,165,158,176,182,172]).reshape((-1,1)) # x
weight = [75,81,59,70,55,78,84,72]
# ordinary least squares : minimum of error
model = LinearRegression().fit(height, weight)
##### Regression
print(model.score(height, weight)) # R2
print(model.intercept_) # b
print(model.coef_) # ax

##### predict
print(model.predict([[170]]))
print(model.predict([[170], [180]]))
print(model.predict(height))


##### plot and chart
plt.scatter(height, weight)
plt.plot(height, model.predict(height))
plt.show()
