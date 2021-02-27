def threeSum(ar,target):
    ans=[-1,-1,-1]
    for i in range(0,len(ar)):
        s=set()
        r=target-ar[i]
        for j in range(i+1,len(ar)):
            p=r-ar[j]
            if p in s:
                ans[0]=ar[i]
                ans[2]=ar[j]
                ans[1]=p
                return ans
            s.add(ar[j])
    return ans

'''def threeSum(ar,target):
    ans=[-1,-1,-1]
    for i in range(0,len(ar)):
        for j in range(i+1,len(ar)):
            r=target-(ar[i]+ar[j])
            if r in ar:
                ans[0]=ar[i]
                ans[1]=ar[j]
                ans[2]=r
                return ans
    return ans'''

ar=[9,8,5,6,1,7]
target=14

#ar = [1, 4, 45, 6, 10, 8]
#target = 22

print(threeSum(ar,target))



'''def twoSum(ar,target):
    ans=[-1,-1]
    for i in range(0,len(ar)):
        r=target-ar[i]
        if r in ar:
            ans[0]=ar[i]
            ans[1]=r
            return ans
    return ans

ar=[2,8,5,6,1,7]
target=14
print(twoSum(ar,target))
'''
