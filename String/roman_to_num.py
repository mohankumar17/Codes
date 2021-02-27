def romanToDecimal(s):
    # code here
    d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    if len(s)==1:
        return d[s[0]]
    if len(s)==2 and d[s[1]]>d[s[0]]:
        return d[s[1]]-d[s[0]]

    n=len(s)
    i=0
    ans=0
    while i<n-1:
        if d[s[i]]<d[s[i+1]]:
            ans=ans+(d[s[i+1]]-d[s[i]])
            i=i+1
        else:
            ans=ans+d[s[i]]
        i=i+1

    if i<n:
        ans=ans+d[s[i]]

    return ans

l=['V','IX','XII','XIV','XXVI','XXXIX','CMXVI']
for i in range(7):
    print(l[i],' -> ',romanToDecimal(l[i]))
