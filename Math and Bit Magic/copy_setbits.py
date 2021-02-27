def dec(x):
    ans=0
    x=x[::-1]
    for i in range(len(x)):
        ans=ans+(int(x[i])*(2**i))
    return ans

def bin_(x):
    ans=''
    while x>0:
        r=x%2
        ans=ans+str(r)
        x=x//2
    return ans[::-1]

def copySet(x,y,l,r):
    x=bin_(x)
    y=bin_(y)
    y=[i for i in y]
    l-=1;r-=1
    for i in range(len(y)):
        if i<l or i>r:
            y[i]='0'
    y=''.join(y)
    return dec(x)+dec(y)


x=10
y=13
l=2
r=3
print(copySet(x,y,l,r))
