import sys
def matMul(ar):
    n=len(ar)
    ans=[[0 for i in range(n)] for i in range(n)]
    for l in range(2,n):
        for i in range(0,n-l):
            j=i+l
            ans[i][j]=sys.maxsize
            for k in range(i+1,j):
                cost=ans[i][k]+ans[k][j]+(ar[i]*ar[k]*ar[j])
                if cost<ans[i][j]:
                    ans[i][j]=cost
    return ans[0][n-1]

ar=[2,3,6,4,5]
print(matMul(ar))

'''import sys
#Resursive approach
def matrix(arr,i,j):
    if i==j:
        return 0
    m=sys.maxsize
    for k in range(i,j):
        cost=matrix(arr,i,k)+matrix(arr,k+1,j)+(arr[i-1]*arr[k]*arr[j])
        if cost<m:
            m=cost
    return m

#Dynamic programming approach
def matrixdp(arr):
    n=len(arr)
    M=[[0 for t in range(n)] for t in range(n)]
    S=[[0 for t in range(n)] for t in range(n)]
    for d in range(1,n):
        for i in range(1,n-d+1):
            j=i+d-1
            q=sys.maxsize
            for k in range(i,j):
                cost=M[i][k]+M[k+1][j]+(arr[i-1]*arr[k]*arr[j])
                if cost<q:
                    q=cost
                    S[i][j]=k
                    M[i][j]=q
    return M[1][n-1]


######################
arr=[1,2,3,4,3]
n=len(arr)
cost=matrix(arr,1,n-1)
print(cost)

cost=matrixdp(arr)
print(cost)
'''
