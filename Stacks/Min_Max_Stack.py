import sys
s=[5,1,3,7,4,8,2]
min=[s[0]]
max=[s[0]]
for i in range(1,len(s)):
    if s[i]<min[-1]:
        min.append(s[i])
    if s[i]>max[-1]:
        max.append(s[i])
print('Min:',min[-1])
print('Max:',max[-1])


min=sys.maxsize
max=-sys.maxsize

for i in range(len(s)):
    if s[i]<min:
        min=s[i]
    if s[i]>max:
        max=s[i]
print('Min:',min)
print('Max:',max)
