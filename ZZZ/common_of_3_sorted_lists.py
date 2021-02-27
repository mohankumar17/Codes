def cThree(ar1,ar2,ar3):
    i=j=k=0
    ans=[]
    while i<len(ar1) and j<len(ar2) and k<len(ar3):
        if ar1[i]==ar2[j] and ar2[j]==ar3[k]:
            ans.append(ar1[i])
            i=i+1
            j=j+1
            k=k+1

        elif ar1[i]<ar2[j]:
            i=i+1

        elif ar2[j]<ar3[k]:
            j=j+1

        else:
            k=k+1
    return ans

ar1=[2,3,6,7]
ar2=[5,6,7]
ar3=[6,7,8]
print(cThree(ar1,ar2,ar3))
