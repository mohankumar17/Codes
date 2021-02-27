class Graph:
	def __init__(self, vertices):
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
		self.V = vertices

	def isSafe(self, v, pos, path):
		if self.graph[ self.path[pos-1] ][v] == 0:
			return False
		for vertex in self.path:
			if vertex == v:
				return False
		return True

	def hamCycleUtil(self, path, pos):
		if pos == self.V:
			if self.graph[ self.path[pos-1] ][ self.path[0] ] == 1:
				return True
			else:
				return False

		for v in range(1,self.V):
			if self.isSafe(v, pos, self.path) == True:
				self.path[pos] = v
				if self.hamCycleUtil(self.path, pos+1) == True:
					return True
				self.path[pos] = -1

		return False

	def hamCycle(self):
		self.path = [-1] * self.V
		self.path[0] = 0    #source node is 0

		if self.hamCycleUtil(self.path,1) == False:
			print ("Solution does not exist\n")
			return False

		for vertex in self.path:
			print (vertex, end = " ")
		print (self.path[0])
		return True


g1 = Graph(5)
g1.graph = [ [0, 1, 0, 1, 0],
			 [1, 0, 1, 1, 1],
			 [0, 1, 0, 0, 1],
			 [1, 1, 0, 0, 1],
			 [0, 1, 1, 1, 0], ]

g1.hamCycle();

'''g2 = Graph(5)
g2.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
		[0, 1, 0, 0, 1,], [1, 1, 0, 0, 0],
		[0, 1, 1, 0, 0], ]
g2.hamCycle();
'''
