def func(s,l,r):
    if l==r:
        #f=''.join(s)
        print(s)

    else:
        for i in range(l,r+1):
            s[l],s[i]=s[i],s[l]
            func(s,l+1,r)
            s[l],s[i]=s[i],s[l]

#st=input()
#s=[]
#for i in st:
#    s.append(i)
s=[1,2,3]
l=0
r=len(s)-1
func(s,l,r)
