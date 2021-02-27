def LIS(ar):
    n=len(ar)
    res=[1]*n
    for i in range(1,n):
        for j in range(0,i):
            if ar[i]>ar[j] and res[j]+1>res[i]:
                res[i]=res[j]+1
    return res

def biotonic(ar):
    n=len(ar)
    LIS_left=LIS(ar)
    for i in range(n//2):
        ar[i],ar[n-i-1]=ar[n-i-1],ar[i]

    LIS_right=LIS(ar)
    ans=[0]*n
    for i in range(n):
        ans[i]=LIS_left[i]+LIS_right[n-i-1]-1

    print(ans)
    return max(ans)

ar=[2,-1,4,3,5,-1,3,2]
print(biotonic(ar))
#Biotonic sequence-Longest incresing and then decreasing subsequence
