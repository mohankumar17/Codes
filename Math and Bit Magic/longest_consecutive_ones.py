n=int(input())
b=bin(n)
b=b[2:]
#b=input()
c=0
m=0
l=[]
for i in b:
    if i=='1':
        c+=1
    else:
        l.append(c)
        c=0

for i in l:
    if i>m:
        m=i
print(m)
