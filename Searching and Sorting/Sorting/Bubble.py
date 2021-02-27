def bubble(ar):
    for i in range(0,len(ar)):
        s=False
        print(ar)
        for j in range(0,len(ar)-i-1):
            if ar[j]>ar[j+1]:
                ar[j],ar[j+1]=ar[j+1],ar[j]
                s=True
        if s==False:
            break
    return ar

#A=[12,11,5,13,6]
#A=[5,3,1,2]
A=[64,25,12,22,11]
print(bubble(A))
