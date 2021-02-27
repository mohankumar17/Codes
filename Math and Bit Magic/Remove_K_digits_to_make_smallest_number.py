class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s=[]
        #s.append()
        for i in num:
            while len(s) and k>0 and int(i)<int(s[-1]):
                s.pop()
                k=k-1
            if len(s) or i!='0':
                s.append(i)
        while len(s) and k>0:
            s.pop()
            k-=1
        if len(s)==0:
            return '0'
        s=''.join(s)
        #print(s)
        return s

num="5337"
k=2
s=Solution()
print(s.removeKdigits(num,k))
