def util(s,i):
    if (ord(s[i])>=65 and ord(s[i])<=(65+25)) or (ord(s[i])>=97 and ord(s[i])<=(97+25)):
        return True
    return False

t=int(input())
while t>0:
    t-=1
    s=input()
    n=len(s)
    s=[i for i in s]
    i=0
    j=n-1

    while i<j:
        if util(s,i) and util(s,j):
            s[i],s[j]=s[j],s[i]
            i=i+1
            j=j-1
        else:
            if not util(s,j):
                j=j-1
            if not util(s,i):
                i=i+1

    s=''.join(s)
    print(s)
