def reverse_stack(s):
    n=len(s)
    i=n-1
    while i>=n//2:
        temp=s[i]
        s[i]=s[n-i-1]
        s[n-i-1]=temp
        i=i-1

s=[1,2,3,4,5]
reverse_stack(s)
print(s)
