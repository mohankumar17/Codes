def isAnangram(s1,s2):
    d1={}
    for i in s1:
        d1[i]=d1.get(i,0)+1
    d2={}
    for i in s2:
        d2[i]=d2.get(i,0)+1

    if len(d1)!=len(d2):
        return False

    for i in d1:
        if i in d2:
            if d1[i]!=d2[i]:
                return False
        else:
            return False
    return True

s1="caat"
s2="aatc"
print(isAnangram(s1,s2))
