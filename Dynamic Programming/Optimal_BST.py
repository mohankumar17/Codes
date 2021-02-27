import sys
def getSum(cost,i,j):
    #print(sum(cost[i:j+1]))
    return sum(cost[i:j+1])

def optimalBST(ar,cost):
    n=len(ar)
    ans=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        ans[i][i]=cost[i]

    for l in range(2,n+1):
        for i in range(0,n-l+1):
            j=i+l-1
            s=getSum(cost,i,j)
            ans[i][j]=sys.maxsize
            for k in range(i,j+1):
                m=s
                #if k-1>=i:
                m=m+ans[i][k-1] if k-1>=i else m
                #if k+1<=j:
                m=m+ans[k+1][j] if k+1<=j else m

                if m<ans[i][j]:
                    ans[i][j]=m

    for i in ans:
        print(i)

    return ans[0][n-1]


keys=[10,12,16,21]
cost=[4,2,6,3]
print(optimalBST(keys,cost))
