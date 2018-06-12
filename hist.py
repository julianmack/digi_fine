"""Plots a histogram of randomly generated
random numbers using seaborn"""


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


#print(np.random.randn(3,100))
data = np.random.normal(0, 0.1, 100000)


sns.set()  # sets look of hist to nicely designed seaborn package
_ = plt.hist(data, bins=100)
#always label axes

plt.show()
