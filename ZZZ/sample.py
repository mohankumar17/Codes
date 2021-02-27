ar=[[3,2],[1,6],[2,5]]
ind=[[1,0]]
for i in ind:
    ar.sort(key=lambda x:x[i[0]],reverse=True)
print(ar)
