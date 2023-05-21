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
