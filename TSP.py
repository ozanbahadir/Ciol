import numpy as np
import random
import math


"""
    Notes: data.shape[0] faster than len(data[0])
"""
class SMA:

    def __init__(self, distances, inittemp=1000, finaltemp=1, equilibrium=100, cooling='geometric',coolingparam=0.7, neighbor='2opt'):
        self.distances = distances
        self.dimension = distances.shape[0]
        self.it = inittemp
        self.ft = finaltemp
        self.eq = equilibrium
        self.clng = cooling
        self.clngprm = coolingparam
        self.neigh = neighbor
        self.route=np.zeros(self.distances.shape[0])

    #geometric cooling
    def geometric(self, *args):
        return args[0] * self.clngprm

    #linear cooling
    def linear(self, *args):
        return args[0] - args[1] * self.clngprm

    #logaritmic cooling
    def logaritmic(self, *args):
        return args[0] /math.log(args[1])

    #calculates objective function iteratively
    def iterativeobj(self):
        obj = self.distances[self.route[0]][self.dimension]
        for i in range(self.distances.shape[0]):
            obj += self.distances[self.route[i]][self.route[i+1]]
        return obj
    #calculates objective function incrementaly
    def incrementalobj(self):
        return  -1

    def swap(self):
        #copy route
        rt = self.route
        # creates 2 different random int in range(dimension)
        rnd = random.sample(range(self.dimension),2)
        #swap
        temp = rt[rnd[0]]
        rt[rnd[0]]= rt[rnd[1]]
        rt[rnd[1]] = temp
        return rt ,rnd

    def twoopt(self):
        return  2

    def kopt(self):
        return  3

    def solve(self):
         #gets the right function for given cooling attr.
        cf = getattr(self, self.clng)
         #gets the right function for given neighbor attr.
        ng = getattr(self,self.neigh)

        dimension = self.distances.shape[0]
         #random solution
        self.route = random.sample(range(dimension), dimension)
        #calc. objective function
        obj = self.iterativeobj()

        t = self.it
        while t < self.ft:
            for i in range(self.eq):
                #generate a random neigh. for given neighbor parameter
                #calculate objective function
                #calculate delta new-old

            #update temp.
            t = cf(t,i)


class NearestNeighbor:

    def __init__(self, distances):
        self.distances = distances
        self.visited = np.zeros(distances.shape[0],dtype=int)
        self.route = np.ones(distances.shape[0],dtype=int)
        self.totaldist = 0

    def solve(self):
        #gets problem dimension from distance matrix
        dimension = len(self.distances[0])
        #generate a random integer as a start point
        start = random.randint(0, dimension-1)
        #init. first point
        self.visited[start] = 1
        self.route[0] = start
        for i in range(dimension-1):
            temp = self.findnearest(self.route[i])
            self.route[i+1] = temp[0]
            self.visited[temp[0]] = 1
            self.totaldist += temp[1]
        return self.route, self.totaldist

    #finds nearest city for given index
    def findnearest(self, frm):
        mind = 10000
        index = -1
        for i in range(len(self.distances)):
            if i != frm and self.visited[i] != 1:
                #DUZELT !!!!!!!!! zaten uzaklık matrisi var elimizde
                temp1 = self.finddistance(frm, i)
                if mind > temp1:
                    mind = temp1
                    index = i

        return index, mind

    #finds euclidian distance between two points and returns
    def finddistance(self, frm, to):
        return math.sqrt(math.pow((self.distances[frm][0]-self.distances[to][0]),2)+math.pow((self.distances[frm][1]-self.distances[to][1]),2))







