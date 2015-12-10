import numpy as np
import random
import math


class SMA:

    def __init__(self, distances, inittemp=1000, finaltemp=1, equilibrium=100, cooling='geo',coolingparam=0.7, neighbor='2opt'):
        self.distances = distances
        self.it = inittemp
        self.ft = finaltemp
        self.eq = equilibrium
        self.clng = cooling
        self.clngprm = coolingparam
        self.neigh = neighbor

    def geometric(self,t):
        return t * self.clngprm


    def linear(self,t,i):
        return t- i*self.clngprm

    def logaritcmic(self,t,i):
        return t/(math.log10(i))






class NearestNeighbor:

    def __init__(self, distances):
        self.distances = distances
        self.visited = np.zeros(distances.shape[0],dtype=int)
        self.route = np.ones(distances.shape[0],dtype=int)
        self.totaldist = 0

    def solve(self):
        #gets problem dimension from distance matrix
        dimension = self.distances.shape[0]
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

    def findnearest(self, frm):
        mind = 10000
        index = -1
        for i in range(len(self.distances)):
            if i != frm and self.visited[i] != 1:
                temp1 = self.finddistance(frm, i)
                if mind > temp1:
                    mind = temp1
                    index = i

        return index, mind

    #finds euclidian distance between two points and returns
    def finddistance(self, frm, to):
        return math.sqrt(math.pow((self.distances[frm][0]-self.distances[to][0]),2)+math.pow((self.distances[frm][1]-self.distances[to][1]),2))







