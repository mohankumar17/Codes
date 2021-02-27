
def countways(a, n):
	cnt = [0 for i in range(n)]
	s = 0;s = sum(a)
	if (s % 3 != 0):
		return 0
	s = s//3
	ss = 0
	# If the sum of elements from i-th to n-th equals to sum of part
	# putting 1 in cnt array otherwise 0.
	for i in range(n - 1, -1, -1):
		ss += a[i]
		if (ss == s):
			cnt[i] = 1
	# Calculating the cumulative sum of the array cnt from the last index.
	for i in range(n - 2, -1, -1):
		cnt[i] += cnt[i + 1]
	ans = 0
	ss = 0
	# Calculating answer using original and cnt array.
	for i in range(0, n - 2):
		ss += a[i]
		if (ss == s):
			ans += cnt[i + 2]
	return ans

def countwaysNew(a,n):
    c=[0 for i in range(n)]
    s=sum(a)
    if s%3!=0:
        return 0
    s=s//3
    t=0
    for i in range(n-1,-1,-1):
        t=t+a[i]
        if t==s:
            c[i]=1
    for i in range(n-2,-1,-1):
        c[i]=c[i]+c[i+1]
    t=0
    ans=0
    for i in range(0,n-2):
        t=t+a[i]
        if t==s:
            ans=ans+c[i+2]
    return ans

n = 5
a = [1, 2, 3, 0, 3]
print(countways(a, n))
print(countwaysNew(a, n))
