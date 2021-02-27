def splitStr(s):
    n=len(s)
    zc=0
    oc=0
    c=0
    for i in range(n):
        if s[i]=='0':
            zc=zc+1
        else:
            oc=oc+1
        if zc==oc:
            c=c+1
            zc=oc=0
    return c

s='010001111'
ans=splitStr(s)
print(ans)
#split string in to equal zeros and ones
