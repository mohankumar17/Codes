'''def isPalindrome(s):
    i=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return False
        i=i+1
        j=j-1
    return True'''

def longPalindrome(s):
    n=len(s)
    dp=[[False for i in range(n)] for i in range(n)]
    for i in range(n):
        dp[i][i]=True
    maxLength=1
    start=0

    for i in range(n-1):
        if s[i]==s[i+1]:
            dp[i][i+1]=True
            start=i
            maxLength=2

    for l in range(3,n+1):
        for i in range(0,n-l+1):
            j=i+l-1
            if s[i]==s[j] and dp[i+1][j-1]==True:
                start=i
                dp[i][j]=True
                maxLength=max(maxLength,l)
    #print(start)
    return s[start:start+maxLength]

#t=int(input())
t=1
while t>0:
    t-=1
    #s=input()
    s='abaabab'
    ans=longPalindrome(s)
    print(ans)
