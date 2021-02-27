def util(d,ar,p):
    i=p+1
    while i!=p:
        x=d[i]
        if ((ar[0]+x[0])*(ar[1]+x[1]))>0:
            return i
        i=i+1
        if i>=3:
            i=0
    return -1

def maxTime(d,ar):
    c=0
    p=-1
    while True:
        ind=util(d,ar,p)
        if ind!=-1:
            x=d[ind]
            ar[0]=ar[0]+x[0]
            ar[1]=ar[1]+x[1]
            p=ind
            c=c+1
        else:
            return c

d=[[3,2],[-5,-10],[-20,5]]
ar=[20,8]
ans=maxTime(d,ar)
print(ans)
