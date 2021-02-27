#from collections import defaultdict
import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for i in range(self.V)] for i in range(self.V)]

    def addEdge(self,u,v,w):
        #self.graph.append([u,v,w])
        self.graph[u][v]=w
        self.graph[v][u]=w

    def minKey(self,key,mstSet):
        min=sys.maxsize
        for v in range(self.V):
            if key[v]<min and mstSet[v]==False:
                min=key[v]
                min_index=v
        return min_index

    def Djisktra(self):
        key=[sys.maxsize]*self.V
        #parent=[None]*self.V
        #parent[0]=-1
        key[0]=0 #src=0
        mstSet=[False]*self.V
        for i in range(self.V):
            u=self.minKey(key,mstSet)
            mstSet[u]=True
            for v in range(self.V):
                if self.graph[u][v]>0 and mstSet[v]==False and key[v]>key[u]+self.graph[u][v]:
                    key[v]=self.graph[u][v]+key[u]
                    #parent[v]=u

        #################################

        for i in range(1,self.V):
            print(0,i,key[i])
            #print(0,i,self.graph[parent[i]][i]+key[parent[i]])


####################################
g = Graph(5)
g.addEdge(0,1,4)
g.addEdge(0,2,5)
g.addEdge(0,3,8)
g.addEdge(1,2,-3)
g.addEdge(2,4,4)
g.addEdge(3,4,2)
g.addEdge(4,3,1)


'''g.addEdge(0,1,2)
g.addEdge(0,3,6)
g.addEdge(1,2,3)
g.addEdge(1,3,1)
g.addEdge(1,4,5)
g.addEdge(2,4,1)'''

g.Djisktra()

#time complexity: O(Vlog(E))
#space complexity: O(V)
#graph space: O(V^2)
