

import numpy as np                              # importing numpy
import matplotlib.pyplot as plt                 # importing matplotlib for plotting

def plot_X_Y(start, stop, n =1000):
    '''   
    This function plots a graph betwwen x and square root of x for a given range
    of numbers. 
    '''
    X = np.linspace(start, stop, n)             # creating array X
    Y = np.sqrt(X)                              # getting square root of array x
    plt.figure(figsize=(9,6))                   # istantiate a figure
    plt.plot(X, Y, label = "y=√x")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
    

if __name__  == "__main__":
     plot_X_Y (0, 100)                          #calling plot_X_Y
    