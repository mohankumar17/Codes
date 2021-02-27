def maxAreaHist(ar):
    n=len(ar)
    s=[]
    i=0
    m=0
    while i<n:
        if len(s)==0 or ar[s[-1]]<=ar[i]:
            s.append(i)
            i=i+1
        else:
            x=s.pop()
            if len(s):
                area=ar[x]*(i-s[-1]-1)
            else:
                area=i
            m=max(m,area)

    while len(s):
        x=s.pop()
        if len(s):
            area=ar[x]*(i-s[-1]-1)
        else:
            area=i
        m=max(m,area)

    return m

def maxAreaRect(ar):
    t=ar[0]
    ans=0
    r=maxAreaHist(t)
    ans=max(ans,r)

    for i in range(1,len(ar)):
        for j in range(len(ar[0])):
            if ar[i][j]==0:
                t[j]=0
            else:
                t[j]=t[j]+ar[i][j]

        r=maxAreaHist(t)
        ans=max(ans,r)
    return ans


ar=[[1,1,0,1,0],
    [1,0,0,1,1],
    [0,1,1,1,1],
    [1,1,1,1,1]]

print(maxAreaRect(ar))
