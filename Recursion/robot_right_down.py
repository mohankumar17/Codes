def robot(m,n):
    if m==1 or n==1:
        return 1
    return robot(m-1,n)+robot(m,n-1)

m,n=4,3
print(robot(m,n))


'''def func(m,n):
  if m==1 or n==1:
    return 1
  else:
    return func(m-1,n)+func(m,n-1)
m,n=list(map(int,input().split()))
print(func(m,n))

'''
