from collections import defaultdict
class Graph:
    def __init__(self,V):
        self.V=V
        #self.g=defaultdict(list)
        self.g=[]

    def addEdge(self,u,v):
        self.g.append([u,v])
        #self.g[u].append(v)
        #self.g[v].append(u)

    def find(self,n,parent):
        if parent[n]==n:
            return n
        return self.find(parent[n],parent)

    def Union(self,x,y,parent,rank):
        xset=self.find(x,parent)
        yset=self.find(y,parent)
        if rank[xset]<rank[yset]:
            parent[xset]=yset
        elif rank[xset]>rank[yset]:
            parent[yset]=xset
        else:
            rank[xset]+=1
            parent[yset]=xset

    def isCyclic(self):
        rank=[0 for i in range(self.V)]
        parent=[]
        for i in range(self.V):
            parent.append(i)

        for u,v in self.g:
            x=self.find(u,parent)
            y=self.find(v,parent)

            if x==y:
                return True
            else:
                self.Union(u,v,parent,rank)

        return False

    def Util(self,v,visited,parent):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                if self.Util(i,visited,v):
                    return True
            elif parent!=i:
                return True
        return False

    def isCyclic_DFS(self):
        visited=[False]*self.V
        self.graph=defaultdict(list)
        for u,v in self.g:
            self.graph[u].append(v)
            self.graph[v].append(u)

        for v in self.graph:
            if visited[v]==False:
                if self.Util(v,visited,-1):
                    return True
        return False


ob=Graph(5)
ob.addEdge(0,1)
ob.addEdge(0,3)
ob.addEdge(0,4)
ob.addEdge(1,2)
#ob.addEdge(2,3)
#ob.addEdge(1,3)
#ob.addEdge(2,3)
#ob.addEdge(3,4)
#print(ob.g)
#print(ob.isCyclic())
print(ob.isCyclic_DFS())
