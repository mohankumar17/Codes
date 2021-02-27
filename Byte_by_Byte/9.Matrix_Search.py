def matSearch(mat,x):
    for r in range(0,len(mat)):
        row=mat[r]
        l=0
        h=len(row)-1
        while l<=h:
            mid=(l+h)//2
            if row[mid]==x:
                return [r,mid]
            elif x<row[mid]:
                h=mid-1
            elif x>row[mid]:
                l=mid+1
    return [-1,-1]

mat=[[ 1 , 3 , 4 , 5 ],
     [ 2 , 6 , 8 , 9 ],
     [ 11 , 10 , 13 , 14 ]]
x=9
print(matSearch(mat,x))
