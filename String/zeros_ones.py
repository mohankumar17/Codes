#s='0100110101'
s='01001100011101010011'

zc=0
oc=0
ans=0

for i in range(len(s)):
    if s[i]=='0':
        zc=zc+1
    if s[i]=='1':
        oc=oc+1
    if zc==oc:
        ans=ans+1

print(ans)
