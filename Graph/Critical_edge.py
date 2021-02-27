from collections import defaultdict

class Graph:
	def __init__(self,vertices):
		self.V= vertices
		self.graph = defaultdict(list)
		self.Time = 0

	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	'''A recursive function that finds and prints bridges using DFS traversal
	u --> The vertex to be visited next
	visited[] --> keeps tract of visited vertices
	disc[] --> Stores discovery times of visited vertices
	parent[] --> Stores parent vertices in DFS tree'''

	def bridgeUtil(self,u, visited, parent, low, disc):
		visited[u]= True
		disc[u] = self.Time
		low[u] = self.Time
		self.Time += 1

		for v in self.graph[u]:
			if visited[v] == False :
				parent[v] = u
				self.bridgeUtil(v, visited, parent, low, disc)
				# Check if the subtree rooted with v has a connection to one of the ancestors of u
				low[u] = min(low[u], low[v])

				#If the lowest vertex reachable from subtree under v is below u in DFS tree, then u-v is a bridge
				if low[v] > disc[u]:
					print (u,v)

			elif v != parent[u]: # Update low value of u for parent function calls.
				low[u] = min(low[u], disc[v])


	def bridge(self):
		visited = [False] * (self.V)
		disc = [float("Inf")] * (self.V)
		low = [float("Inf")] * (self.V)
		parent = [-1] * (self.V)

		for i in range(self.V):
			if visited[i] == False:
				self.bridgeUtil(i, visited, parent, low, disc)

g1 = Graph(5)
g1.addEdge(0, 1)
g1.addEdge(0, 4)
g1.addEdge(3, 4)
g1.addEdge(1, 3)
g1.addEdge(1, 2)

g1.bridge()
