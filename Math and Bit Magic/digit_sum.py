def digitSum(n):
    if n%9==0 or n==9:
        return 9
    return n%9
'''def digitSum(n):
    while n>=10:
        s=0
        while n>0:
            s=s+(n%10)
            n=n//10
        n=s
    return n'''

n=1286
print(digitSum(n))
