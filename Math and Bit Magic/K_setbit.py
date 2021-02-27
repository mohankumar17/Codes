def setbitK(n,k):
    if (n& (1<<k-1)):
        return True
    else:
        return False

def setKthBit(N, K):
    if (N&(1<<K)):
        return N
    else:
        return (N^(1<<K))

n=12  #1100
k=2
#print(setbitK(n,k))
print(setKthBit(n,k))
