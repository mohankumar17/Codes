import sys
def func(l):
    meh=0
    msf=-sys.maxsize
    for i in l:
        meh=meh+i
        if meh<i:
            meh=i
        if msf<meh:
            msf=meh
    return msf

l=[-2,1,-3,4,-1,2,1,-5,4]
print(func(l))
