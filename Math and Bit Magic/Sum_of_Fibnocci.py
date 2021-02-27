class Solution:
    # @param A : integer
    # @return an integer
    def fibsum(self, A):
        fib=[]
        a=0
        b=1
        fib.append(0)
        fib.append(1)
        c=a+b
        while c<=A:
            a,b=b,c
            fib.append(c)
            c=a+b
        i=len(fib)-1
        #print(fib)
        ans=0
        while i>1:
            ans=ans+(A//fib[i])
            A=A%fib[i]
            i=i-1
        return ans

        
