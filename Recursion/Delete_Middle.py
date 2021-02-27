def delMiddle(s,n):
    if n==len(s)//2:
        s.pop(n)
        return
    delMiddle(s,n-1)

s=[1,2,3,4,5,6,7]
delMiddle(s,len(s)-1)
print(s)

def Reverse(s,n,res):
    if n<0:
        return
    Reverse(s,n-1,res)
    res.append(s.pop())

s=[1,2,3,4,5,6,7]
res=[]
Reverse(s,len(s)-1,res)
print(res)
