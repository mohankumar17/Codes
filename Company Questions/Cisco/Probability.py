N=8
dx=[1, 2, 2, 1, -1, -2, -2, -1]
dy=[2, 1, -1, -2, -2, -1, 1, 2]

def isSafe(x,y):
	if x>=0 and x<N and y>=0 and y<N:
		return True
	return False

def findProb(start_x,start_y,steps):
	ans=[[[0 for i in range(N)] for i in range(N)] for i in range(N)]
	for i in range(0,N):
		for j in range(0,N):
			ans[i][j][0]=1
	for s in range(1,steps+1):
		for x in range(0,N):
			for y in range(0,N):
				prob=0
				for i in range(0,8):
					nx=x+dx[i]
					ny=y+dy[i]
					if isSafe(nx,ny):
						prob=prob+(ans[nx][ny][s-1]/8)
				ans[x][y][s]=prob
	return ans[start_x][start_y][steps]

n=int(input())
print(findProb(0,0,n))
