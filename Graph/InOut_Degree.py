from collections import defaultdict
class Graph:
	def __init__(self,V):
		self.V=V
		self.g=defaultdict(list)
	def addEdge(self,u,v):
		self.g[u].append(v)
		#self.g[v].append(u)
	def BFS(self):
		visited=[False]*self.V
		root=0
		visited[root]=True
		q=[root]
		while len(q):
			root=q.pop(0)
			print(root,end=' ')
			for i in self.g[root]:
				if visited[i]==False:
					q.append(i)
					visited[i]=True
	def DFSUtil(self,root):
		if self.visited[root]==True:
			return
		print(root,end=' ')
		self.visited[root]=True
		for i in self.g[root]:
			if self.visited[i]==False:
				self.DFSUtil(i)
	def DFS(self):
		self.visited=[False]*self.V
		root=0
		self.DFSUtil(root)

def degreesInOut(g,V):
	out=[0]*V
	In=[0]*V
	for i in range(V):
		#print(i,len(g[i]))
		out[i]=len(g[i])
		for j in g[i]:
			In[j]=In[j]+1

	print('Out-Degree:',out)
	print('In-Degree:',In)

ob=Graph(5)
ob.addEdge(0,1)
ob.addEdge(0,3)
ob.addEdge(1,2)
ob.addEdge(2,4)
ob.addEdge(3,2)
ob.addEdge(3,4)

degreesInOut(ob.g,ob.V)
#ob.BFS()
#print()
#ob.DFS()
