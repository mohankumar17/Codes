def genPar(s,n,pos,open,closed):
    if closed==n:
        a=''.join(s)
        print(a)
    else:
        if open<n:
            s[pos]='('
            genPar(s,n,pos+1,open+1,closed)
        if open>closed:
            s[pos]=')'
            genPar(s,n,pos+1,open,closed+1)

n=3
s=['']*2*n
open=0
closed=0
pos=0
genPar(s,n,pos,open,closed)
'''
def func(s,n,pos,open,close):
    if close==n:
        s=''.join(s)
        print(s)
    else:
        if open<n:
            s[pos]='('
            func(s,n,pos+1,open+1,close)
        if open>close:
            s[pos]=')'
            func(s,n,pos+1,open,close+1)


n=int(input())
s=[' ']*2*n
#paranthesis(s,n,0,0,0)
func(s,n,0,0,0)
'''
