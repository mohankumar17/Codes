def jobSch(ar):
    ar=sorted(ar,key=lambda x:x[1])
    ans=[]
    n=len(ar)
    for i in ar:
        ans.append(i[2])

    for i in range(1,n):
        for j in range(0,i):
            #check non-overlap
            if ar[i][0]>=ar[j][1]:
                ans[i]=max(ans[i],ans[j]+ar[i][2])  #ar[i][2]-profit
    return max(ans)

ar=[[1,3,5],[2,5,6],[6,7,4],[7,9,2],[4,6,5],[5,8,11]]
print(jobSch(ar))
