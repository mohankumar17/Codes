def minSwaps(arr):
	n = len(arr)
	arrpos = [(i,arr[i]) for i in range(0,len(arr))]
	arrpos.sort(key = lambda x:x[1])
	vis = [False for k in range(n)]
	ans = 0

	for i in range(n):
		if vis[i] or arrpos[i][0] == i:
			continue
		# find number of nodes in this cycle and add it to ans
		cycle_size = 0
		j = i
		while not vis[j]:
			vis[j] = True
			# move to next node
			j = arrpos[j][0]
			cycle_size += 1
		# update answer by adding
		# current cycle
		if cycle_size > 0:
			ans += (cycle_size - 1)
	return ans
arr = [7,1,3,2,4,5,6]
print(minSwaps(arr))
