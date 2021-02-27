'''def palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False'''

def palindrome(s):
    i=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i=i+1
        j=j-1
    return True

s='malayalam'
print(palindrome(s))
