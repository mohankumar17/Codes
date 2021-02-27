def merge_arrays(A,B):
    i=0
    j=0
    m=len(A)
    n=len(B)
    ans=[]
    while i<m and j<n:
        if A[i]<B[j]:
            ans.append(A[i])
            i=i+1
        elif A[i]>B[j]:
            ans.append(B[j])
            j=j+1
    while i<m:
        ans.append(A[i])
        i=i+1
    while j<n:
        ans.append(B[j])
        j=j+1
    return ans

A=[1,4,7]
B=[2,5,8]
ans=merge_arrays(A,B)
print(ans)
