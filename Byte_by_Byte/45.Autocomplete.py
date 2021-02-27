from collections import defaultdict
def auto(l,letter):
    d=defaultdict(list)
    for i in l:
        d[i[0]].append(i)
    ans=d[letter]
    return ans

l=["must","abcd","ace","mohan","ban","ram","rest","abhi"]
print(auto(l,'a'))
print(auto(l,'b'))
print(auto(l,'m'))
print(auto(l,'r'))
