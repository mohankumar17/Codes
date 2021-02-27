t=int(input())
while t>0:
    n=int(input())
    ar=list(map(int,input().split()))
    start=0
    end=n-1
    count=0
    while start<end:
        if ar[start]==ar[end]:
            start+=1
            end-=1
        elif ar[start]>ar[end]:
            ar[end-1]=ar[end]+ar[end-1]
            end=end-1
            count=count+1
        else:
            ar[start+1]=ar[start]+ar[start+1]
            start=start+1
            count=count+1
    print(count)
    t-=1
