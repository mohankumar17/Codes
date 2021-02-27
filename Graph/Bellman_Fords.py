#from collections import defaultdict
import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        #self.graph = [[0 for i in range(self.V)] for i in range(self.V)]
        self.graph=[]

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
        #self.graph[u][v]=w
        #self.graph[v][u]=w

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

    def BellmanFord(self):
        key=[sys.maxsize]*self.V
        key[0]=0
        parent=[None]*self.V
        parent[0]=-1

        for i in range(self.V-1):
            for u,v,w in self.graph:
                if key[u]!=sys.maxsize and key[v]>key[u]+w:
                    key[v]=key[u]+w
                    parent[v]=u

        for u,v,w in self.graph:
            if key[u]!=sys.maxsize and key[v]>key[u]+w:
                print('negative edge cycle detected')
                break

        for i in range(1,self.V):
            print(i,parent[i],key[i])

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

#g.Djisktra()
g.BellmanFord()


'''class Graph:
	def __init__(self, vertices):
		self.V = vertices # No. of vertices
		self.graph = []

	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	def printArr(self, dist):
		print("Vertex Distance from Source")
		for i in range(self.V):
			print("{0}\t\t{1}".format(i, dist[i]))

	def BellmanFord(self, src):
		# Step 1: Initialize distances from src to all other vertices as INFINITE
		dist = [float("Inf")] * self.V
		dist[src] = 0

		# Step 2: Relax all edges |V| - 1 times. A simple shortest path from src to any other vertex
		#can have at-most |V| - 1 edges

		for i in range(self.V - 1):
			# Update dist value and parent index of the adjacent vertices of the picked vertex.
			#Consider only those vertices which are still in queue
			for u, v, w in self.graph:
				if dist[u] != float("Inf") and  dist[v]>dist[u] + w:
					dist[v] = dist[u] + w

		# Step 3: check for negative-weight cycles. The above step guarantees shortest distances
		# if graph doesn't contain negative weight cycle. If we get a shorter path, then there is a cycle.

		for u, v, w in self.graph:
			if dist[u] != float("Inf") and  dist[v]>dist[u] + w:
				print("Graph contains negative weight cycle")
				return
		self.printArr(dist)

g = Graph(5)

g.addEdge(0,1,4)
g.addEdge(0,2,5)
g.addEdge(0,3,8)
g.addEdge(1,2,-3)
g.addEdge(2,4,4)
g.addEdge(3,4,2)
g.addEdge(4,3,1)

#print(g.graph)
g.BellmanFord(0)'''
#BellmanFord's Algo gives the shortest path from source to node (both positive and negative weight edges)
#time complexity: O(V*E)
#space complexity: O(V)
#graph space: O(E)
