def patternMatch(s,p):
    n=len(p)
    for i in range(len(s)):
        if s[i:i+n]==p:
            return i
    return -1

s='OREKSFORGEEKS'
p='ORG'
print(patternMatch(s,p))
