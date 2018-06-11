"""SPEC: Create a list of random integers (5-10 integers). Assign each number with a probability.
Then randomly generate 100 numbers from the list given the probability distribution you just
generated. Finally, plot a histogram to show the results (i.e. number of times each number from the
list is generated).

Assumptions
Use probability distribution of form P(X=x)=k*x^2, where k is a constant
require x (possible values) in range 0 < x < 21
require n (number of values) in range 5 <= n <= 10

USAGE: python3 ex1.py n
where n is an int in 5<=n<=10

"""
import sys

import numpy as np
from random import choices
import matplotlib.pyplot as plt
import seaborn as sns

#global - range of x values
RANGE_x = 20

def main():
    #check valid input:
    n = check_input_args()

    #generate n random ints, x in range 0 < x < 21
    xs_set = set()
    while len(xs_set) <= n:
        xs_set.add(np.random.randint(1, RANGE_x + 1))

    #convert to ordered list
    xs = list(xs_set)

    #assign each number with probability P(X=x)=k*x^2
    weights = []    #values of P(X=x)
    total = 0       #running total - for normalisation
    for x in xs:
        square = x**2
        weights.append(square)
        total += square

    #normalise
    for index in range(len(xs)):
        weights[index] = weights[index] / total

    #use P(X=x) to generate 100 values of X
    data = choices(xs, weights, k=100)

    #plot histogram
    plot_hist(data)


def check_input_args():
    #check input args
    if len(sys.argv) != 2:
        print("USAGE: python3 ex1.py n,\n")
        sys.exit(1)

    #get n
    try:
        n = int(sys.argv[1])
    except:
        print("USAGE: python3 ex1.py n,\n \
       n is an int where 5 <= n <= 10")
        sys.exit(1)

    #check 5<=n<=10
    if (n < 5) or (n > 10):
        print("USAGE: python3 ex1.py n,\n\
       n is an int where 5 <= n <= 10")
        sys.exit(1)

    return n

def plot_hist(data):
    sns.set()  # use seaborn package for design
    _ = plt.hist(data, bins=100)

    plt.ylabel("Frequency")

    plt.xticks(range(0, RANGE_x + 1))

    plt.show()
    return None

if __name__ == "__main__":
    main()
