import sys
class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):

        meh=0
        msf=0
        k=0
        n=len(A)
        check=False
        start=0
        end=0
        l=[]
        t=[i for i in range(n)]
        for i in range(0,n):
            if A[i]=='1':
                t[i]=-1
            else:
                t[i]=1
        for i in range(0,n):
            if meh+t[i]<0:
                meh=0
                k=i+1
            else:
                meh=meh+t[i]
            if meh>msf:
                check=True
                msf=meh
                start=k
                end=i

        if check==False:
            return []
        return [start+1,end+1]



            
