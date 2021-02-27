import sys
def mXOR(ar):
    ar.sort()
    m=sys.maxsize
    for i in range(0,len(ar)-1):
        x=ar[i]^ar[i+1]
        if x<m:
            m=x
    return m
    #return min(ar[-1]^ar[-2],ar[0]^ar[1])

ar=[0,2,8,1,5,6]
print(mXOR(ar))
