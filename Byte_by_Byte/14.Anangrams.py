def isAnagram(s1,s2):
    if s1=="" and s2=="":
        return True
    s1=s1.lower()
    s2=s2.lower()
    d1={}
    d2={}
    for i in s1:
        d1[i]=d1.get(i,0)+1
    for i in s2:
        d2[i]=d2.get(i,0)+1
    for i in d1:
        if i in d2:
            if d1[i]!=d2[i]:
                return False
        else:
            return False
    return True

print(isAnagram ( "" , "" ))
print(isAnagram ( "A" , "A" ))
print(isAnagram ( "A" , "B" ))
print(isAnagram ( "ab" , "ba" ))
print(isAnagram ( "AB" , "ab" ))
print(isAnagram ( "AB" , "abc" ))
