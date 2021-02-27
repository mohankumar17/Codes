def combUtil(ar,k,n,index,i,data):
    if index==k:
        print(data)
        return
    if i>=n:
        return

    data[index]=ar[i]
    combUtil(ar,k,n,index+1,i+1,data)
    combUtil(ar,k,n,index,i+1,data)


def comb(ar,k):
    n=len(ar)
    data=[0]*k
    combUtil(ar,k,n,0,0,data)

ar=[1,2,3,4]
k=2
comb(ar,k)


'''def combUtil(A,k,n,data,index,i):
    if index==k:
        print(data)
        return
    if i>=n:
        return

    data[index]=A[i]
    combUtil(A,k,n,data,index+1,i+1)
    #while A[i]==A[i+1]:
    #    i=i+1
    combUtil(A,k,n,data,index,i+1)

def combination(A,k):
    data=[0]*k
    n=len(A)
    #A.sort()
    combUtil(A,k,n,data,0,0)

A=[1,2,3,4]
k=3
combination(A,k)

'''
