def possibleBST(n):
    ans=[0 for i in range(n+1)]
    ans[0]=1
    ans[1]=1
    for j in range(2,n+1):
        s=0
        for i in range(0,n):
            s=s+ans[j-i-1]*ans[i]
        ans[j]=s

    #print(ans)
    return ans[n]

n=5
print(possibleBST(n))
