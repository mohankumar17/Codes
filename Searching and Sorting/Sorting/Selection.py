def selection(ar):
    for i in range(0,len(ar)):
        min_index=i
        for j in range(i+1,len(ar)):
            if ar[j]<ar[min_index]:
                min_index=j
        ar[min_index],ar[i]=ar[i],ar[min_index]

    return ar

#A=[12,11,5,13,6]
ar=[5,8,3,7,1,6]
print(selection(ar))
