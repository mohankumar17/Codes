from collections import defaultdict
class Graph:
    def __init__(self):
        self.d = defaultdict(list)

    def addEdge(self, u, v):
        self.d[u].append(v)
        self.d[v].append(u)

    def display(self):
        print(self.d)

    def BFS(self, root):
        q = []
        q.append(root)
        visited = [False] * len(self.d)
        visited[root] = True
        while len(q):
            x = q.pop(0)
            print(x, end=' ')
            for i in self.d[x]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True

    def func(self, root, visited):
        print(root, end=' ')
        visited[root] = True
        for i in self.d[root]:
            if not visited[i]:
                self.func(i, visited)

    def DFS(self, root):
        visited = [False] * len(self.d)
        self.func(root, visited)


ob = Graph()

ob.addEdge(0, 1)
ob.addEdge(0, 3)
ob.addEdge(0, 4)
ob.addEdge(1, 2)
ob.addEdge(1, 3)
ob.addEdge(2, 3)
ob.addEdge(3, 4)

ob.display()
root = 0
print('BFS : ', end=' ')
ob.BFS(root)  # Level-Order-Traversal
print()
print('DFS : ', end=' ')
ob.DFS(root)
