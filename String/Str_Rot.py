def func(s1,s2):
    if len(s1)!=len(s2):
        return -1
    t=len(s1)-1
    i=0
    while t:
        f=s1[0]
        s1=s1+s1[0]
        s1=s1[1:]
        if s1==s2:
            return 1
        t=t-1
    return -1

s1='ABCD'
s2='CDAB'
#s3='ACBD'
s3='DABC'
print(func(s1,s3))
