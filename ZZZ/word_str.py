def func(d1,d2):
    c=0
    while True:
        for i in d1:
            if i not in d2:
                return 0
            if d2[i]>=d1[i]:
                d2[i]=d2[i]-d1[i]
            else:
                return c
        c=c+1
    return c

str="this is at test string sit"
word='tsit'
d1={}
for i in word:
    d1[i]=d1.get(i,0)+1
d2={}
for i in str:
    if i in d1:
        d2[i]=d2.get(i,0)+1
print(d1)
print(d2)
ans=func(d1,d2)
print(ans)
