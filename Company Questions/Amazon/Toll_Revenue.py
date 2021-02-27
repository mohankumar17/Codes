# You are using Python
'''m=int(input())
n=int(input())
x=list(map(int,input().split()))
revenue=list(map(int,input().split()))
t=int(input())'''
m=15
n=4
x=[6,9,12,14]
revenue=[5,6,3,7]
t=2

maxrev=[0]*(m+1)
nxt=0
for i in range(1,m+1):
    if nxt<n:
        if x[nxt]!=i:
            maxrev[i]=maxrev[i-1]
        else:
            if i<=t:
                maxrev[i]=max(maxrev[i-1],revenue[nxt])
            else:
                maxrev[i]=max(maxrev[i-t-1]+revenue[nxt],maxrev[i-1])
            nxt=nxt+1
    else:
        maxrev[i]=maxrev[i-1]
print(maxrev[m])
