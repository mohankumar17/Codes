def missing(ar):
    ar=set(ar)
    ans=[]
    for i in range(1,len(ar)+3):
        if i not in ar:
            ans.append(i)
    return ans

ar=[4,2,3,7]
print(missing(ar))
