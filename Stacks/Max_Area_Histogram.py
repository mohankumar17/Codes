import sys
def maxAreaHist(ar):
    n=len(ar)
    s=[]
    i=0
    m=0
    area=0

    while i<n:
        if len(s)==0 or ar[i]>=ar[s[-1]]:
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

#ar=[6,5,6,7]
ar=[1,4,3]
print(maxAreaHist(ar))
