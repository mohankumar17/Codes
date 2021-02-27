def util(n,i):
    while n%i==0:
        n=n//i
    return n

def ugly(n):
    n=util(n,2)
    n=util(n,3)
    n=util(n,5)
    if n==1:
        return True
    else:
        return False

n=10
i=1
ans=1
while True:
    if ugly(i):
        ans=i
        n=n-1
        if n==0:
            break
    i=i+1
print(ans)


'''class Solution:
    def util(self,a,i):
        while a%i==0:
            a=a/i
        return a
    def isUgly(self, num: int) -> bool:
        if num==0:
            return False
        num=self.util(num,2)
        num=self.util(num,3)
        num=self.util(num,5)
        if num==1:
            return True
        else:
            return False


'''
