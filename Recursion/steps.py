def func(n):
  ar=[]
  ar.append(0)
  ar.append(1)
  ar.append(2)
  for i in range(3,n+1):
    ar.append(ar[i-1]+ar[i-2])
  return ar[n]

n=int(input())
print(func(n))

'''
def steps(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return n

    return steps(n-1)+steps(n-2)

n=5
print(steps(n))

'''
