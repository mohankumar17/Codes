def LCP(s1,s2):
    i=0
    ans=''
    while i<len(s1) and i<len(s2):
        if s1[i]==s2[i]:
            ans+=s1[i]
        else:
            break
        i=i+1

    return ans

s1='Monhan'
s2='Monhey'
print(LCP(s1,s2))
