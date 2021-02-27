
import sys
def Coins(coins, m, V):
	ans = [0 for i in range(V + 1)]
	ans[0] = 0

	for i in range(1, V + 1):
		ans[i] = sys.maxsize
	for i in range(1, V + 1):
		for j in range(m):
			if (coins[j] <= i):
				sub_res = ans[i - coins[j]]
				if (sub_res != sys.maxsize and sub_res + 1 < ans[i]):
					ans[i] = sub_res + 1
	return ans[V]


t=int(input())
while t>0:
    V=int(input())
    coins = [i for i in range(V+1)]
    m = V
    print(Coins(coins, m, V))
    t-=1
