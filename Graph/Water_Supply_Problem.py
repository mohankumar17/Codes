# Python3 program to solve water
# supply problem using BFS

# Function to perform BFS
def bfsUtil(v, vis, adj, src):

	# Mark current source visited
	vis[src] = True

	# Queue for BFS
	q = []

	# Push src to queue
	q.append(src)

	count = 0
	while (len(q) != 0):
		p = q[0]

		for i in range(len(adj[p])):

			# When the adjacent city not visited and
			# not blocked, push city in the queue.
			if (vis[adj[p][i]] == False and v[adj[p][i]] == 0):
				count += 1
				vis[adj[p][i]] = True
				q.push(adj[p][i])

			# when the adjacent city is not visited
			# but blocked so the blocked city is
			# not pushed in queue
			elif(vis[adj[p][i]] == False and v[adj[p][i]] == 1):
				count += 1
		q.remove(q[0])

	return count + 1

# Utility function to perform BFS
def bfs(N, v, adj):
	vis = [ 0 for i in range(N + 1)]
	mx = 1

	# marking visited array false
	for i in range(1, N + 1, 1):
		vis[i] = False

	# Check for each and every city
	for i in range(1, N + 1, 1):

		# Checks that city is not blocked
		# and not visited.
		if (v[i] == 0 and vis[i] == False):
			res = bfsUtil(v, vis, adj, i)
			if (res > mx):
				mx = res

	return mx

# Driver Code
if __name__ == '__main__':
	N = 4

	# Denotes the number of cities
	adj = [[] for i in range(N + 1)]
	v = [0 for i in range(N + 1)]

	# Adjacency list denoting road
	# between city u and v
	adj[1].append(2)
	adj[2].append(1)
	adj[2].append(3)
	adj[3].append(2)
	adj[3].append(4)
	adj[4].append(3)

	# array for storing whether ith
	# city is blocked or not
	v[1] = 0
	v[2] = 1
	v[3] = 1
	v[4] = 0

	print(bfs(N, v, adj))

# This code is contributed by Bhupendra_Singh
