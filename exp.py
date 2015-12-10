import numpy as np
import random
import TSP


N = 100
b = np.random.random_integers(50, 100, size=(N, N))

data = (b + b.T)/2

#print(TSP.NearestNeighbor(data).solve())

#print(TSP.SMA(data).wrapper(100,20))

def geometric(t,c):
    return t * c

def linear(t,i,c):
    return t- i*c

def logaritcmic(t,i):
    return t/(math.log10(i))


def wrapper(func, t, i):
    return func(t,i)

print(wrapper(geometric,100,2))