ar=[2,3,-5,4,-6,-1]
#[-5,-6,-1,2,3,4]

i=0
j=0
p=[];n=[]
while i<len(ar):
    if ar[i]>0:
        p.append(ar[i])
    else:
        n.append(ar[i])
    i+=1

i=0
while i<len(n):
    ar[j]=n[i]
    j+=1
    i+=1

i=0
while i<len(p):
    ar[j]=p[i]
    j+=1
    i+=1

print(ar)
