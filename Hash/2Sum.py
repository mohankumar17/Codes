def TwoSum(ar,target):
    d={}
    ans=[-1,-1]
    for i in range(0,len(ar)):
        r=target-ar[i]
        if r not in d:
            d[ar[i]]=i
        else:
            ans[0]=d[r]
            ans[1]=i
            return ans
    return ans

ar=[1,2,4,6,7]
target=8
print(TwoSum(ar,target))


'''#Return the index of the elemnts  [i,j] where i<j which can sum to target
def two_sum(ar,target):
    d={}
    ans=[]
    for i in range(0,len(ar)):
        x=target-ar[i]

        if ar[i] not in d:
            d[ar[i]]=i

        if x in d:
            ans.append(d[x])
            ans.append(i)
            break

    return ans


ar=[2,7,11,14]
target=9
print(two_sum(ar,target))
''''
