def countWays(mtrx, vrtx, i, dest, visited):
	if (i == dest):
		return 1

	total = 0
	for j in range(vrtx):
		if mtrx[i][j] == 1 and visited[j]==False:
			visited[j] = True;
			total += countWays(mtrx, vrtx, j, dest, visited);
			visited[j] = False;
	return total

def totalWays(mtrx, vrtx, src, dest):
	visited = [False]*vrtx
	visited[src] = True;
	return countWays(mtrx, vrtx, src, dest,visited)


vrtx = 5
'''mtrx = [
		[0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
		[ 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0 ],
		[ 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0 ],
		[ 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0 ],
		[ 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0 ],
		[ 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0 ],
		[ 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0 ],
		[ 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0 ],
		[ 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0 ],
		[ 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0 ],
		[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0 ]
	]'''
mtrx= [
        [0,1,0,1,1],
		[1,0,1,1,0],
		[0,1,0,1,0],
		[1,1,1,0,0],
		[1,0,0,0,0]
      ]
src = 0
dest = 2
print(totalWays(mtrx, vrtx, src,dest))
