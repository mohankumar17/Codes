def insertion(ar):
    for i in range(0,len(ar)):
        key=ar[i]
        j=i-1
        while j>=0 and key<ar[j]:
            ar[j+1]=ar[j]
            j=j-1
        ar[j+1]=key
    return ar

def Insertion(ar):
    for i in range(0,len(ar)):
        key=ar[i]
        j=i-1
        while j>=0 and key<ar[j]:
            ar[j+1]=ar[j]
            j=j-1
        ar[j+1]=key
    return ar

#A=[12,11,5,13,6]
A=[5,3,1,2]
print(Insertion(A))
