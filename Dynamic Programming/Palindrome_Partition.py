import sys
def isPalindrome(s,i,j):
    if len(s)==1:
        return True
    while i<j:
        if s[i]!=s[j]:
            return False
        i=i+1
        j=j-1
    return True

def partPalindrome(s):
    n=len(s)
    ans=[[0 for i in range(n)] for i in range(n)]

    for l in range(1,n+1):
        for i in range(0,n-l+1):
            j=i+l-1
            if isPalindrome(s,i,j):
                ans[i][j]=0
            else:
                ans[i][j]=sys.maxsize
                for k in range(i,j):
                    splits=1+ans[i][k]+ans[k+1][j]
                    if splits<ans[i][j]:
                        ans[i][j]=splits

    for i in ans:
        print(i)
    return ans[0][n-1]

s='abbama'
print(partPalindrome(s))
