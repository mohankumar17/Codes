def nearestGreater(ar):
    n=len(ar)
    ans=[-1]*n
    s=[]
    for i in range(1,n):
        if ar[i]<ar[i-1]:
            ans[i]=ar[i-1]
            s.append(ar[i-1])
        else:
            while len(s):
                if ar[i]<s[-1]:
                    ans[i]=s[-1]
                    break
                s.pop()
    return ans

#ar=[4,3,8,9,7]
#ar=[4,3,1,2,7,6]
#ar=[3,6,4,2,8]
ar=[100,80,60,70,60,75,85]
ans=nearestGreater(ar)
print(ans)
