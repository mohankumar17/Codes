MAX = 20
def LIP(dp, mat, n, m, x, y):
	if (dp[x][y] < 0):
		result = 0
		if (x == n - 1 and y == m - 1):
			dp[x][y] = 1
			return dp[x][y]

		if (x == n - 1 or y == m - 1):
			result = 1

		if (x + 1 < n and mat[x][y] < mat[x + 1][y]):
			result = 1 + LIP(dp, mat, n,m, x + 1, y)

		if (y + 1 < m and mat[x][y] < mat[x][y + 1]):
			result = max(result, 1 + LIP(dp, mat, n,m, x, y + 1))

		dp[x][y] = result
	return dp[x][y]

def wrapper(mat, n, m):
	dp = [[-1 for i in range(MAX)] for i in range(MAX)]
	return LIP(dp, mat, n, m, 0, 0)

mat = [[1, 2, 3, 4 ],
	   [2, 2, 3, 4 ],
	   [3, 2, 3, 4 ],
	   [4, 5, 6, 7 ]]
n = 4
m = 4
print(wrapper(mat, n, m))
