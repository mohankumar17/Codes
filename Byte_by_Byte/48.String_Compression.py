from collections import OrderedDict
def compress(s):
    d=OrderedDict()
    for i in s:
        d[i]=d.get(i,0)+1
    ans=''
    for i in d:
        ans=ans+(i)+str(d[i])
    return ans

print(compress("a"))
print(compress("aaa"))
print(compress("aaabbb"))
print(compress("aabbbc"))
