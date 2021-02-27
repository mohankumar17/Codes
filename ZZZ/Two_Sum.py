def TwoSum(ar,target):
    ans=[]
    d={}
    for i in range(0,len(ar)):
        r=target-ar[i]
        if r in d:
            ans.append(d[r])
            ans.append(i+1)
            break
        if r not in d:
            d[ar[i]]=i+1
    return ans
ar=[2, 1, 3, 2]
target=4
print(TwoSum(ar,target))
