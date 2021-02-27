def func(m,n):
    if m==n:
        return 1
    if m>n:
        return 1+func(m-n,n)
    else:
        return 1+func(m,n-m)

min_l=5
max_l=7
min_w=3
max_w=4

res=0

for l in range(min_l,max_l+1):
    for w in range(min_w,max_w+1):
        res=res+func(l,w)
print(res)
