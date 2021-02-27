def threeSum(ar):
    n=len(ar)
    ans=[]
    for i in range(0,n-1):
        h=set()
        for j in range(i+1,n):
            t=ar[i]+ar[j]
            if -t in h:
                ans.append([ar[i],ar[j],-t])
            h.add(ar[j])
    return ans

#ar=[ -1 , 0 , 1 , 2 , -1 , -4 ]
ar=[1,2,-3,0,3]
print(threeSum(ar))
#[ -1 , -1 , 2 ] , [ -1 , 0 , 1 ]
