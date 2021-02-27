class Solution:
    def findLargest(self, N, S):
        # code here
        if S==0 and N>1:
            return -1
        if S==0 and N==1:
            return 0

        ar=[9]*N
        sum_ar=9*N

        f=1
        i=N-1
        while i>=0:
            if sum_ar<S:
                return -1

            if sum_ar==S:
                f=0
                break
            else:
                if ar[i]==0:
                    i=i-1
                ar[i]=ar[i]-1
                sum_ar=sum_ar-1

        if f==1:
            return -1

        s=0
        for i in range(N):
            s=(s*10)+ar[i]
        return s
