def nextGreater(ar):
    n=len(ar)
    ans=[-1]*n
    s=[]
    for i in range(n-2,-1,-1):
        if ar[i]<ar[i+1]:
            ans[i]=ar[i+1]
            s.append(ar[i+1])
        else:
            while len(s):
                if ar[i]<s[-1]:
                    ans[i]=s[-1]
                    break
                s.pop()

    return ans

#ar=[1,6,2,3,5,9]
ar=[ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
ans=nextGreater(ar)
print(ans)


'''def next_grt(ar):
    s=[]
    n=len(ar)
    ans=[-1]*n
    for i in range(n-1,-1,-1):
        while len(s):
            if ar[i]<s[-1]:
                ans[i]=s[-1]
                break
            else:
                s.pop()
        s.append(ar[i])
    #s=[]
    return ans

#ar=[ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
ar=[1,6,2,3,5,9]
print(next_grt(ar))'''
