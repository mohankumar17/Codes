from collections import defaultdict
class Graph:
	def __init__(self,V):
		self.graph = defaultdict(list)
		self.V = V

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def isCyclicUtil(self, v, visited, recStack):
		visited[v] = True
		recStack[v] = True
		for i in self.graph[v]:
			if visited[i] == False:
				if self.isCyclicUtil(i, visited, recStack) == True:
					return True
			elif recStack[i] == True:
				return True

		recStack[v] = False
		return False

	def isCyclic(self):
		visited = [False] * self.V
		recStack = [False] * self.V
		#for v in range(self.V):
		for v in range(self.V):
			if visited[v] == False:
				if self.isCyclicUtil(v,visited,recStack) == True:
					return True
		return False

ob=Graph(5)
ob.addEdge(0,1)
ob.addEdge(0,4)
ob.addEdge(1,3)
ob.addEdge(3,2)
#ob.addEdge(2,3)
ob.addEdge(2,1)
print(ob.graph)

print(ob.isCyclic())
