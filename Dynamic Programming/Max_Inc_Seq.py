def maxSumInc(ar):
    n=len(ar)
    ans=[i for i in ar]
    rec=[i for i in range(n)]

    for i in range(1,n):
        for j in range(0,i):
            if ar[j]<ar[i]:
                t=ans[j]+ar[i]
                if t>ans[i]:
                    ans[i]=t
                    rec[i]=j
    print(rec)
    print(ans)
    return max(ans)

ar=[4,6,1,3,8,4,6]
print(maxSumInc(ar))
