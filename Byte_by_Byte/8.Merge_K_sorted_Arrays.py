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

def merge_k(ar):
    ans=ar[0]
    i=1
    while i<len(ar):
        ans=merge_arrays(ans,ar[i])
        i=i+1
    return ans

ar=[[1,4,7],[2,5,8],[3,6,9]]
res=merge_k(ar)
print(res)
