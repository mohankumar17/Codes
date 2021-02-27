#This is The Coding Area
N=int(input())
ar=list(map(int,input().split()))

bit_sc=[]
for num in ar:
  ex=str(num)
  large=int(max(ex))
  small=int(min(ex))
  x=(large*11)+(small*7)
  if len(str(x))>2:
      x=str(x)
      x=x[-3:-1]
      x=int(x)

  bit_sc.append(x)
print(bit_sc)
odd=[]
even=[]

for i in range(0,len(bit_sc)):
  if i%2==0:
    even.append(bit_sc[i])
  else:
    odd.append(bit_sc[i])

pairs=0
d={}
for n in odd:
  key=(str(n))[0]
  d[key]=d.get(key,0)+1
for i in d:
  if d[i]==2:
    pairs=pairs+1
  elif d[i]>=3:
    pairs=pairs+2

d={}
for n in even:
  key=(str(n))[0]
  d[key]=d.get(key,0)+1
for i in d:
  if d[i]==2:
    pairs=pairs+1
  elif d[i]>=3:
    pairs=pairs+2

print(pairs)
