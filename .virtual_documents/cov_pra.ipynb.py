import numpy as np
import matplotlib.pyplot as plt


mean = np.array([0,0])


cov = np.array([
  [1,0.1],
  [0.1,1]
])


a = np.random.multivariate_normal(mean, cov, 5000)
a


a.T


x,y = a.T


plt.plot(x,y,"x")


a = np.array([[10, 5, 2, 4, 9, 3, 2],
              [10, 2, 8, 3, 7, 4, 1]
             ])
np.cov(a)


c = np.array([3, 2, 1, 5, 7, 2, 1])
np.cov(a,c)



