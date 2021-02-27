def PS(s,n,i,curr):
    if i>=n:
        print(curr)
        return
    PS(s,n,i+1,curr+s[i])
    PS(s,n,i+1,curr)

s='abc'
n=len(s)
curr=''
i=0
PS(s,n,i,curr)


'''def subset(s,n,i,curr,ans):
    if i==n:
        ans.append(curr)
        return

    subset(s,n,i+1,curr+s[i],ans)
    subset(s,n,i+1,curr,ans)


s='abc'
n=len(s)
i=0
curr=''
ans=[]
subset(s,n,i,curr,ans)
print(ans)
'''
