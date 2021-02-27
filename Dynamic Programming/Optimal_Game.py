#Optimal Strategy for a Game
#Pick from ends to maximize the value(win the game)
def game(ar):
    n=len(ar)
    ans=[[[0,0] for i in range(n)] for i in range(n)]

    for i in range(n):
        ans[i][i]=[ar[i],0]

    for l in range(2,n+1):
        for i in range(0,n-l+1):
            j=i+l-1
            a=ar[i]+ans[i+1][j][1]
            b=ar[j]+ans[i][j-1][1]
            if a>b:
                ans[i][j][0]=a
                ans[i][j][1]=ans[i+1][j][0]
            else:
                ans[i][j][0]=b
                ans[i][j][1]=ans[i][j-1][0]

    for i in ans:
        print(i)

    return ans[0][n-1]

ar=[3,9,1,2]
print(game(ar))
