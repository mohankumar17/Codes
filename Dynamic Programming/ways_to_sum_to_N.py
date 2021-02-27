def func(arr,n,s):
	if s==0:
		return 1
	if s<0:
		return 0
	ans=0
	for i in range(0,n):
		ans=ans+func(arr,n,s-arr[i])
	return ans

def countWays(arr, m, N):
	count = [0 for i in range(N + 1)]
	count[0] = 1
	for i in range(1, N + 1):
		for j in range(m):
			if (i >= arr[j]):
				count[i] += count[i - arr[j]]
	return count[N]

#arr = [1,10]
arr = [1, 3, 5]
m = len(arr)
N = 7
#print(countWays(arr, m, N))
print(countWays(arr, m, N))
#print(func(arr, m, N))
