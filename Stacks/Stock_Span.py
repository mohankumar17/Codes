def stockSpan(ar):
    n=len(ar)
    ans=[0]*n
    ans[0]=1
    s=[0]
    for i in range(1,n):
        while len(s) and ar[i]>ar[s[-1]]:
            s.pop()

        if len(s)<=0:
            ans[i]=i+1
        else:
            ans[i]=i-s[-1]
        s.append(i)

    return ans

    '''n=len(ar)
    ans=[1]*n
    for i in range(1,n):
        for j in range(0,i):
            if ar[j]<ar[i]:
                ans[i]=ans[i]+1
    return ans'''
    '''
    n=len(ar)
    res=[1]*n
    s=[]
    for i in range(1,n):
        if ar[i]<ar[i-1]:
            s.append(ar[i-1])
        else:
            while len(s):
                if ar[i]<s[-1]:
                    #res[i]=i-ar.index(s[-1])
                    res[i]=i-ar.index(s[-1])
                    break
                s.pop()

    return res'''

ar=[100,80,60,70,60,75,85]
ans=stockSpan(ar)
print(ans)
