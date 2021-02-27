import math
def isPrime(n):
    p=int(math.sqrt(n))
    for i in range(2,p+1):
        if n%i==0:
            return False
    return True

n1,n2=map(int,input().split())
primeList=[]
for i in range(n1,n2+1):
    if isPrime(i):
        primeList.append(i)
#print(primeList)
comb=[]
for i in range(len(primeList)):
    for j in range(len(primeList)):
        if i!=j:
            s=str(primeList[i])+str(primeList[j])
            comb.append(s)
#print(comb)
primeList2=[]
for i in comb:
    if isPrime(int(i)):
        primeList2.append(int(i))

primeList2=list(set(primeList2))
count=len(primeList2)
lar=max(primeList2)
small=min(primeList2)
#print(count)
if count<2:
    if count==0:
        print(0)
    elif count==1:
        print(small)
    else:
        print(lar)
else:
    fib=[0 for i in range(count)]
    fib[0]=small
    fib[1]=lar
    for i in range(2,count):
        fib[i]=(fib[i-1]+fib[i-2])
    #print(fib)

    print(fib[count-1])  #13158006689
