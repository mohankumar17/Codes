def Spiral(arr):
    k=0
    l=0
    m=len(arr)
    n=len(arr[0])
    ans=[]
    while k<m and l<n:
        for i in range(l,n):
            ans.append(arr[k][i])
        k=k+1

        for i in range(k,m):
            ans.append(arr[i][n-1])
        n=n-1

        if k<m:
            i=n-1
            while i>=l:
                ans.append(arr[m-1][i])
                i=i-1
            m=m-1

        if l<n:
            i=m-1
            while i>=k:
                ans.append(arr[i][l])
                i=i-1
            l=l+1

    return ans

arr=[[11,12,13,22],
     [14,15,16,24],
     [17,18,19,27],
     [10,25,26,28]]
res=Spiral(arr)
print(res)
