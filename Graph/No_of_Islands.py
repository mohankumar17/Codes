class Island:
    def __init__(self,m,r,c):
        self.m=m
        self.r=r
        self.c=c

    def check_visited(self,m,i,j,cd):
        if i<0 or i>=self.r or j<0 or j>=self.c or self.m[i][j]!=1:
            return
        self.m[i][j]=2
        cd[0]=cd[0]+1
        self.check_visited(self.m,i+1,j,cd)
        self.check_visited(self.m,i,j+1,cd)
        self.check_visited(self.m,i-1,j,cd)
        self.check_visited(self.m,i,j-1,cd)

    def countIslands(self):
        count=0
        ans=-1
        for x in range(0,self.r):
            for y in range(0,self.c):
                if self.m[x][y]==1:
                    cd=[0]
                    self.check_visited(self.m,x,y,cd)
                    ans=max(ans,cd[0])
                    count=count+1
        return [count,ans]

    def display(self):
        return self.m


m=[[1,1,0,0,0],
   [0,1,0,0,1],
   [1,1,1,1,1],
   [0,0,0,0,0],
   [1,0,1,0,1]]


r=len(m)
c=len(m[0])
ob=Island(m,r,c)

islands=ob.countIslands()
print(islands)



'''
def isSafe(ar,i,j,m,n):
	if i<0 or i>=m or j<0 or j>=n or ar[i][j]!=1:
		return False
	ar[i][j]=2
	isSafe(ar,i+1,j,m,n)
	isSafe(ar,i-1,j,m,n)
	isSafe(ar,i,j-1,m,n)
	isSafe(ar,i,j+1,m,n)
	return True

def noofIslands(ar,m,n):
	c=0
	for i in range(m):
		for j in range(n):
			if isSafe(ar,i,j,m,n):
				c=c+1
	return c

ar=[[1,1,1,0],
	[0,1,1,0],
	[0,1,0,0],
	[0,1,1,0]]

m=len(ar)
n=len(ar[0])
print(noofIslands(ar,m,n))

'''
