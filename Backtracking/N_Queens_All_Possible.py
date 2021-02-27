def isSafe(row,col,n,m):
	for i in range(col):
		if m[row][i]==1:
			return False
		i=row
		j=col
		while i>=0 and j>=0:
			if m[i][j]==1:
				return False
			i=i-1
			j=j-1

		i=row
		j=col
		while i<n and j>=0:
			if m[i][j]==1:
				return False
			i=i+1
			j=j-1

	return True


def nqueens(n,m,col):
	if col>=n:
		for g in m:
			print(g)
		print()
		return

	for i in range(n):
		if isSafe(i,col,n,m):
			m[i][col]=1
			nqueens(n,m,col+1)
			m[i][col]=0
	return


n=int(input())
m=[[0 for i in range(n)] for i in range(n)]
nqueens(n,m,0)
