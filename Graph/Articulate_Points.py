import sys
from collections import defaultdict
class Graph:
	def __init__(self,V):
		self.V=V
		self.graph=defaultdict(list)
		self.Time=0
	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def APUtil(self,u,visited,ans,parent,lowTime,visitedTime):
		visitedTime[u]=self.Time
		lowTime[u]=self.Time
		self.Time+=1

		visited[u]=True
		neighbours=0

		for v in self.graph[u]:
			if visited[v]==False:
				parent[v]=u
				neighbours+=1
				self.APUtil(v,visited,ans,parent,lowTime,visitedTime)  #DFS
				lowTime[u]=min(lowTime[u],lowTime[v])

				#1. u is root and hase 2 or more neighbours
				if parent[u]==-1 and neighbours>1:
					ans[u]=True

				#2. u is not root and visitedTime[v]<=lowTime[u]
				if parent[u]!=-1 and visitedTime[u]<=lowTime[v]:
					ans[u]=True

			elif v!=parent[u]:
				lowTime[u]=min(lowTime[u],lowTime[v])


	def ArtPoint(self):
		visited=[False]*self.V
		ans=[False]*self.V
		parent=[-1]*self.V
		visitedTime=[sys.maxsize]*self.V
		lowTime=[sys.maxsize]*self.V

		for i in range(self.V):
			if visited[i]==False:
				self.APUtil(i,visited,ans,parent,lowTime,visitedTime)

		#print articulate points
		for i in range(self.V):
			if ans[i]==True:
				print(i,end=' ')

###############################
g=Graph(7)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5)
#g.addEdge(3,5)
g.addEdge(5,6)
g.ArtPoint()
