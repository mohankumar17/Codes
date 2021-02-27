class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def dfs(self,A,B,stepNum,ans):
        if stepNum>=A and stepNum<=B:
            ans.append(stepNum)

        if stepNum==0 or stepNum>B:
            return

        lastdigit=stepNum%10

        stepNumA=(stepNum*10)+lastdigit-1
        stepNumB=(stepNum*10)+lastdigit+1

        if lastdigit==0:
            self.dfs(A,B,stepNumB,ans)
        elif lastdigit==9:
            self.dfs(A,B,stepNumA,ans)
        else:
            self.dfs(A,B,stepNumA,ans)
            self.dfs(A,B,stepNumB,ans)

    def func(self,A,B,ans):
        for i in range(0,10):
            self.dfs(A,B,i,ans)
        return ans

    def stepnum(self, A, B):
        ans=[]
        self.func(A,B,ans)
        ans.sort()
        return ans
