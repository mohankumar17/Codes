from collections import defaultdict
import sys

class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph=defaultdict(list)
		self.Time=0
	def addEdge(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def APUtil(self,u,visited,parent,lowTime,visitedTime,ans):
		visited[u]=True
		children=0
		lowTime[u]=self.Time
		visitedTime[u]=self.Time
		self.Time+=1

		for v in self.graph[u]:
			if visited[v]==False:
				children+=1
				parent[v]=u
				self.APUtil(v,visited,parent,lowTime,visitedTime,ans)
				lowTime[u]=min(lowTime[u],lowTime[v])
				if parent[u]==-1 and children>1:
					ans[u]=True
				if parent[u]!=-1 and visitedTime[u]<=lowTime[v]:
					ans[u]=True

			elif v!=parent[u]:
				lowTime[u]=min(lowTime[u],lowTime[v])

	def AP(self):
		visited=[False]*self.V
		ans=[False]*self.V
		parent=[None]*self.V
		parent[0]=-1
		lowTime=[sys.maxsize]*self.V
		visitedTime=[sys.maxsize]*self.V

		for i in range(self.V):
			if visited[i]==False:
				self.APUtil(i,visited,parent,lowTime,visitedTime,ans)

		for i in range(self.V):
			if ans[i]==True:
				print(i,end=' ')


	def BridgeUtil(self,u,parent,visited,lowTime,visitedTime,ans):
		visited[u]=True
		lowTime[u]=self.Time
		visitedTime[u]=self.Time
		self.Time+=1

		for v in self.graph[u]:
			if visited[v]==False:
				parent[v]=u
				self.BridgeUtil(v,parent,visited,lowTime,visitedTime,ans)
				lowTime[u]=min(lowTime[u],lowTime[v])

				if visitedTime[u]<lowTime[v]:
					ans.append([u,v])

			elif v!=parent[u]:
				lowTime[u]=min(lowTime[u],lowTime[v])

	def Bridge(self):
		visited=[False]*self.V
		ans=[]
		lowTime=[sys.maxsize]*self.V
		visitedTime=[sys.maxsize]*self.V
		parent=[None]*self.V
		parent[0]=-1

		for i in range(self.V):
			if visited[i]==False:
				self.BridgeUtil(i,parent,visited,lowTime,visitedTime,ans)

		for i in ans:
			print(i)

###########################
g=Graph(7)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,5)
#g.addEdge(3,5)
g.addEdge(5,6)
g.addEdge(6,4)

g.AP()
print()
g.Bridge()
