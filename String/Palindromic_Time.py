def minTime(s):
    ans=0
    h=int(s[0])*10+int(s[1])
    m=int(s[3])*10+int(s[4])
    while h%10!=m//10 or m%10!=h//10:
        m=m+1
        if m==60:
            h=h+1
            m=0
        if h==24:
            h=0
        ans=ans+1
    return ans
    
s=input()
h=minTime(s)
print(h)
