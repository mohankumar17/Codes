def consecutive(ar):
    ar.sort()
    m=1
    c=1
    for i in range(0,len(ar)-1):
        if ar[i]+1==ar[i+1]:
            c=c+1
        else:
            if c>m:
                m=c
            c=1
    return max(m,c)

ar=[4,2,1,6,5]
#ar=[5,5,3,1]
print(consecutive(ar))
