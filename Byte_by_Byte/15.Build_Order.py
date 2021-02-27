def buildOrd(d):
    ans=[]
    rem=[]
    for i in d:
        if len(d[i])==0:
            ans.append(i)
        else:
            f=0
            for j in d[i]:
                if j not in ans:
                    f=1
                    break
            if f==0:
                ans.append(i)
            else:
                rem.append(i)

    for i in rem:
        f=0
        for j in d[i]:
            if j not in ans:
                f=1
                break
        if f==0:
            ans.append(i)

    return ans

d={0:[],1:[0],2:[3],3:[1],4:[1,2]}
#ans=[0,1,3,2,4]
print(buildOrd(d))
