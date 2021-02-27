def gray(a,b):
    if a==b:
        return False
    #a=bin(a)
    #b=bin(b)
    #a=a[2:]
    #b=b[2:]
    x=a&b
    if x==a or x==b:
        return True
    else:
        return False



print(gray(0,1))
print(gray(1,2))
print(gray(8,9))
