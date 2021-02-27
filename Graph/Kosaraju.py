#kosarajus algorithm for Strongly Connected Components(SCC)
#If each vertex can be reached from other vertices forms a SCC

#kosarajus Algo:
#   1. DFS and store vertices in stack
#   2. Reverse the graph ,perform DFS again,pop out from the stack

#Time complexity: O(V+E)
#Space complexity: O(V)

from collections import defaultdict
class Graph:
    def __init__(self,V):
        self.V=V
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFS(self,v,visited):
        visited[v]=True
        print(v,end=' ')  #Print SCC
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFS(i,visited)
        #print()

    def DFS_stackFill(self,v,visited,s):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                self.DFS_stackFill(i,visited,s)
        s.append(v)

    def getRev(self):
        rev=defaultdict(list)
        for u in self.graph:
            for v in self.graph[u]:
                rev[v].append(u)
        return rev

    def SCC(self):
        s=[]
        visited=[False]*self.V
        for i in range(self.V):
            if visited[i]==False:
                self.DFS_stackFill(i,visited,s)

        reversed=self.getRev()
        #print(reversed)
        visited=[False]*self.V

        while len(s):
            x=s.pop()
            if visited[x]==False:
                self.DFS(x,visited)
                print('')


g=Graph(7)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(5, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(6, 5)

#print(g.graph)
g.SCC()
