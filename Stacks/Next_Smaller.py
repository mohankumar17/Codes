def nextSmaller(ar):
    n=len(ar)
    ans=[-1]*n
    s=[]
    for i in range(n-2,-1,-1):
        if ar[i]>ar[i+1]:
            ans[i]=ar[i+1]
            s.append(ar[i+1])
        else:
            while len(s):
                if ar[i]>s[-1]:
                    ans[i]=s[-1]
                    break
                s.pop()

    return ans

ar=[4,3,8,9,7]
#ar=[1,2,3,7,4]
ans=nextSmaller(ar)
print(ans)
