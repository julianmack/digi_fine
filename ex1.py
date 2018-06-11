"""Exercise 1 – Create a list of random integers (5-10 integers). Assign each number with a probability.
Then randomly generate 100 numbers from the list given the probability distribution you just
generated. Finally, plot a histogram to show the results (i.e. number of times each number from the
list is generated)."""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


np.random.seed(32)
data = np.random.randn(3,100)


sns.set()  # sets look of hist to nicely designed seaborn package
_ = plt.hist(data, bins=10)
#always label axes

plt.show()
