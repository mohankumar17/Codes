import sys
class Graph:
	def __init__(self,V):
		self.V = V
		self.graph=[[0 for i in range(V)] for i in range(V)]

	def floydWarshall(self):
		dist=self.graph
		#path=[]
		for k in range(self.V):
			for i in range(self.V):
				for j in range(self.V):
					if dist[i][j] > dist[i][k]+ dist[k][j]:
						dist[i][j] = dist[i][k]+ dist[k][j]
						#path[i][j] = path[j][k]

		for i in dist:
			for j in i:
				if j!=sys.maxsize:
					print(j,end=' ')
				else:
					print('*',end=' ')
			print()
		

INF=sys.maxsize
g=Graph(4)
g.graph= [	[0,  5,   INF, 10],
			[INF,0,   3,   INF],
			[INF,INF, 0,   1],
			[INF,INF, INF, 0]
		 ]

g.floydWarshall();
# Solves all pair shortest path via Floyd Warshall Algorithm
"""
		  10
	(0)--------->(3)
	|		    ^
 5  |		    |
	|		    | 1
	|		    |
    ↓           |
	(1)------->(2)
		  3

"""
