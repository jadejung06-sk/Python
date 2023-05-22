##### legend error
## plt.legend('apple')
## >>> a
'''
plt.legend(['apple'])
>>> apple
'''
##### pip install
# pip install sklearn
# >>> https://scribblinganything.tistory.com/651
'''
pip install scikit-learn
'''

##### ValueError: Expected 2D array, got 1D array instead:
# height = [170, 180,160,165,158,176,182,172] # 1D 
# > height = [[170], [180],[160],[165],[158],[176],[182],[172]] # 2D x
# > height = [[170, year], [180, ],[160, ],[165, ],[158, ],[176, ],[182, ],[172, ]] # 2D x including height, year & ...
'''
import numpy as np
height = np.array([170, 180,160,165,158,176,182,172]).reshape((-1,1)) # # > height = [[170], [180],[160],[165],[158],[176],[182],[172]]
'''

##### pip install statsmodels.api
# >>> https://www.statsmodels.org/stable/install.html
'''
pip install statsmodels
'''

##### statsmodels.api as sm
'''
height = np.array([170, 180,160,165,158,176,182,172]).reshape((-1,1)) # x
weight = np.array([75,81,59,70,55,78,84,72])
model = sm.OLS(weight, height).fit() # y x
print(model.summary())
'''

## ValueError 
# : all the input array dimensions except for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 79 and the array at index 2 has size 78
# x = np.column_stack([df['age'], df['age']**2, np.ones(78)])
'''
x = np.column_stack([df['age'], df['age']**2, np.ones(79)])
'''