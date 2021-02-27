from queue import PriorityQueue

def topK(ar,k):
    d={}
    n=len(ar)
    for i in ar:
        d[i]=d.get(i,0)+1

    d=sorted(d,key=lambda x:d[x])
    d=d[::-1]
    return d[0:k]

def freqK(ar,k):
    n=len(ar)
    if k>n:
        return ar

    d={}
    q=PriorityQueue()
    for i in ar:
        d[i]=d.get(i,0)+1
    l=len(d)
    for i in d:
        q.put((l-d[i],i))

    ans=[]
    while k>0:
        ans.append(q.get()[1])
        k=k-1

    return ans


ar=[3,4,4,1,6,1,1,5,4,6,1]
k=int(input())
#print(topK(ar,k))
print(freqK(ar,k))
