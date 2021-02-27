def maxSub(ar,k):
    ans=[]
    for i in range(len(ar)-k+1):
        ans.append(max(ar[i:i+k]))
    return ans

ar=[1,3,2,1,4,2,5]
k=3
ans=maxSub(ar,k)
print(ans)
#ans=[3,3,4,4,5]
