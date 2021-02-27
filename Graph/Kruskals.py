from collections import defaultdict
class Graph:
	def __init__(self,vertices):
		self.V= vertices
		self.graph = []
	def addEdge(self,u,v,w):
		self.graph.append([u,v,w])

	# A utility function to find set of an element i (uses path compression technique)
	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])

	# A function that does union of two sets of x and y (uses union by rank)
	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)
		# Attach smaller rank tree under root of high rank tree (Union by Rank)
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot
		# If ranks are same, then make one as root and increment its rank by one
		else :
			parent[yroot] = xroot
			rank[xroot] += 1

	# The main function to construct MST using Kruskal's algorithm
	def KruskalMST(self):
		result =[]
		i = 0 # An index variable, used for sorted edges
		e = 0 # An index variable, used for result[]
		# Step 1: Sort all the edges in increasing order of their weights
		self.graph = sorted(self.graph,key=lambda item: item[2])
		parent = []
		rank = []
		# Create V disjoint sets with single elements
		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		# Number of edges to be taken is equal to V-1
		'''while e < self.V -1 :
			# Step 2: Pick the smallest edge and increment the index for next iteration
			u,v,w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent ,v)

			# If including this edge does't cause cycle, include it in result and increment the index
			# of result for next edge
			if x != y:
				e = e + 1
				result.append([u,v,w])
				self.union(parent, rank, x, y)
			# Else discard the edge'''
		for u,v,w in self.graph:
			x=self.find(parent,u)
			y=self.find(parent,v)
			if x!=y:
				result.append([u,v,w])
				self.union(parent,rank,u,v)

		print(result)

		min_weight=0
		for u,v,weight in result:
			#print(str(u) + " -- " + str(v) + " == " + str(weight))
			min_weight+=weight
			print ("%d -- %d == %d" % (u,v,weight))
		print('Overall Minimum Weight : ',min_weight)


g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
'''g=Graph(3)
g.addEdge(0,1,10)
g.addEdge(1,2,5)
g.addEdge(0,2,9)
'''
g.KruskalMST()

#time complexity: O(Elog(E)+E)
#space complexity: O(E+V)
