from collections import defaultdict
class Graph:
	def __init__(self,V):
		self.g=defaultdict(list)
		self.V=V

	def addEdge(self,u,v):
		self.g[u].append(v)

	def topUtil(self,v,visited,s):
		visited[v]=True
		for i in self.g[v]:
			if visited[i]==False:
				self.topUtil(i,visited,s)

		s.insert(0,v)

	def topSort(self):
		visited=[False]*self.V
		s=[]
		for i in range(self.V):
			if visited[i]==False:
				self.topUtil(i,visited,s)

		print(s)

g= Graph(6)
g.addEdge(5, 2);
g.addEdge(2, 3);
g.addEdge(3, 1);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(5, 0);

g.topSort()
