def swap(a,b):
    print('Before swap: a =',str(a)+' b =',str(b))
    #a,b=b,a
    a=a+b
    b=a-b
    a=a-b
    print('After swap: a =',str(a)+' b =',str(b))

a=5
b=7
swap(a,b)
