import sys
#O(n^2)
def minJimps(ar):
    n=len(ar)
    ans=[sys.maxsize]*n
    ans[0]=0
    pos=[-1]*n
    for i in range(1,n):
        for j in range(0,i):
            if ar[j]+j>=i:
                t=1+ans[j]
                if t<ans[i]:
                    ans[i]=t
                    pos[i]=j
    jumps=[]
    for i in pos[1:]:
        if i not in jumps:
            jumps.append(i)
    jumps.append(n-1)
    print(jumps)
    return ans[n-1]

#O(n^2)
def minJumps2(ar):
    n=len(ar)
    dp=[sys.maxsize]*n
    dp[0]=0
    for i in range(1,n):
        for j in range(0,i):
            if ar[j]+j>=i:
                if dp[j]!=sys.maxsize and dp[j]+1<dp[i]:
                    dp[i]=dp[j]+1

    return dp[n-1]

#O(n)
def minJumps3(ar):
    n=len(ar)
    if ar[0]==0:
        return -1
    maxReach=ar[0]
    step=ar[0]
    jumps=1
    for i in range(1,n-1):
        maxReach=max(maxReach,ar[i]+i)
        step=step-1
        if step==0:
            jumps=jumps+1
            if maxReach<=i:
                return -1
            step=maxReach-i

    return jumps

#ar=[2,3,1,1,2,4,2,0,1,1]
ar=[2,1,4,1,2,1,3,1]
print(minJimps(ar))
print(minJumps2(ar))
print(minJumps3(ar))
