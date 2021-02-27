def ms(arr):
    if len(arr)>1:
        m=len(arr)//2
        left=arr[:m]
        right=arr[m:]
        l=ms(left)
        r=ms(right)
        i=0
        while len(l)>0 and len(r)>0:
            if l[0]<r[0]:
                arr[i]=l[0]
                l.pop(0)
            else:
                arr[i]=r[0]
                r.pop(0)
            i=i+1

        while len(l)>0:
            arr[i]=l[0]
            l.pop(0)
            i=i+1

        while len(r)>0:
            arr[i]=r[0]
            r.pop(0)
            i=i+1

    return arr

arr=[5,3,7,1,6]
ms(arr)
print(arr)
