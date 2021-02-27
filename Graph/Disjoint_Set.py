class DisjSet:
	def __init__(self, n):
		self.rank = [0] * n
		self.parent = [i for i in range(n)]

	def find(self, n):
		if (self.parent[n] != n):
			self.parent[n] = self.find(self.parent[n])
		return self.parent[n]

	def Union(self, x, y):
		xset = self.find(x)
		yset = self.find(y)

		if xset == yset:
			return
		if self.rank[xset] < self.rank[yset]:
			self.parent[xset] = yset
		elif self.rank[xset] > self.rank[yset]:
			self.parent[yset] = xset
		else:
			self.parent[yset] = xset
			self.rank[xset] = self.rank[xset] + 1

obj = DisjSet(5)
obj.Union(0, 2)
obj.Union(4, 2)
obj.Union(3, 1)
obj.Union(2, 3)

print(obj.rank)
print(obj.parent)

if obj.find(4) == obj.find(0):
	print('Yes')
else:
	print('No')
if obj.find(1) == obj.find(0):
	print('Yes')
else:
	print('No')
