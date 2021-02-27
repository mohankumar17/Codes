def maxAreaHist(ar):
    n=len(ar)
    s=[]
    i=0
    m=0
    area=0

    while i<n:
        if len(s)==0 or ar[s[-1]]<=ar[i]:
            s.append(i)
            i=i+1
        else:
            x=s.pop()
            if len(s):
                area=ar[x]*(i-s[-1]-1)
            else:
                area=i*ar[x]
            m=max(m,area)

    while len(s):
        x=s.pop()
        if len(s):
            area=ar[x]*(i-s[-1]-1)
        else:
            area=ar[x]*i

        m=max(m,area)

    return m


def maxAreaRect(ar):
    t=ar[0]
    ans=0
    r=maxAreaHist(t)
    ans=max(ans,r)

    for i in range(1,len(ar)):
        for j in range(len(ar[0])):
            if ar[i][j]==1:
                t[j]=t[j]+ar[i-1][j]

        r=maxAreaHist(t)
        ans=max(ans,r)

    return ans


ar=[[1,1,0,1,0],
    [1,0,0,1,1],
    [0,1,1,1,1],
    [1,1,1,1,1]]

print(maxAreaRect(ar))

'''def maxAreaHist(ar):
    s=[]
    m=0
    i=0
    while i<len(ar):
        if len(s)==0 or ar[s[0]]<=ar[i]:
            s.append(i)
            i=i+1
        else:
            top=ar[s[0]]
            s.pop()
            area=top*i

            if len(s):
                area=top*(i-s[0]-1)

            m=max(m,area)

    while len(s):
        top=ar[s[0]]
        s.pop()
        area=top*i

        if len(s):
            area=top*(i-s[0]-1)

        m=max(m,area)
    return m

def maxRectangle(A):
    R=len(A)
    C=len(A[0])
    result = maxAreaHist(A[0])
    for i in range(1, R):
        for j in range(C):
            if A[i][j]:
                A[i][j] += A[i - 1][j]
        result = max(result, maxAreaHist(A[i]))
    return result

ar = [[0, 1, 1, 0],
      [1, 1, 0, 0],
      [1, 1, 1, 1],
      [1, 1, 1, 1]]

ans=maxRectangle(ar)
print(ans)
'''
