def isShuffle(s,x):
    if len(s)!=len(x):
        return -1
    for i in range(len(s)):
        if ord(s[i])>=65 and ord(s[i])<=90:






s='XY12'
x='X1Y2'
print(isShuffle(s,x))
