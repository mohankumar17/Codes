from collections import defaultdict
class Graph:
    def __init__(self,V):
        self.V=V
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def shortPath(self,x,y):
        pass

ob=Graph(5)
ob.addEdge(1,2)
ob.addEdge(1,3)
ob.addEdge(2,5)
ob.addEdge(4,1)
ob.addEdge(4,3)
ob.addEdge(5,3)
ob.addEdge(5,4)

#print(ob.graph)
print(shortPath(2,3))
