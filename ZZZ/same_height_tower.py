# Python 3 program to minimize the cost of
# operation to bring all towers to same height.
import sys

# Returns the cost of entire operation in
# bringing the height of all towers to
# equal height eq_h
def costOfOperation(n, h,cost, eq_h):

	# Initialize initial cost to 0
	c = 0

	# Adding cost for each tower
	for i in range(0, n, 1):
		c += abs(h[i] - eq_h) * cost[i]

	return c

# Return the minimum possible cost of
# operation to bring all the towers of
# different height in height[0..n-1]
# to same height.
def Bsearch(n, h, cost):
	max_h = h[0]
	for i in range(len(h)):
		if(h[i] > max_h):
			max_h = h[i]
	ans = sys.maxsize

	# Do binary search for minimum cost
	high = 1 + max_h
	low = 0
	while (high > low):
		mid = (low + high) >> 1

		# Cost below mid
		if(mid > 0):
			bm = costOfOperation(n, h, cost, mid - 1)

		else:
			bm = sys.maxsize

		# Cost at mid
		m = costOfOperation(n, h, cost, mid)

		# Cost above mid
		am = costOfOperation(n, h, cost, mid + 1)

		# Break if the answer becomes equal
		# to minimum cost m
		if (ans == m):
			break

		# ans should hold the minimum cost
		# of operation
		ans = min(ans, m)

		# Search lower cost
		if (bm <= m):
			high = mid

		# Search higher cost
		elif(am <= m):
			low = mid + 1

		# If am > m and bm > m
		# then ans is m
		else :
			return m;

	return ans

# Driver code
if __name__ == '__main__':
	h = [1, 2, 3]
	cost = [10, 100, 1000]
	n = len(h)
	print(Bsearch(n, h, cost))
