def BoxStacking(B1,B2):
    ar=[[B1[0],B1[1],B1[2]],[B1[2],B1[1],B1[0]],[B1[2],B1[0],B1[1]],
        [B2[0],B2[1],B2[2]],[B2[2],B2[1],B2[0]],[B2[2],B2[0],B2[1]]]

    ar=sorted(ar,key=lambda x:x[0]*x[1])
    ar=ar[::-1]
    height=[]
    res=[]
    for i in range(len(ar)):
        height.append(ar[i][2])
        res.append(i)

    #print(max)
    n=len(height)

    for i in range(1,len(height)):
        for j in range(0,i):
            if (ar[i][0]<ar[j][0] and ar[i][1]<ar[j][1]) or (ar[i][0]<ar[j][1] and ar[i][1]<ar[j][0]):
                m=height[j]+ar[i][2]
                if m>height[i]:
                    height[i]=m
                    res[i]=j
    #print(res)
    ans=[]
    j=len(ar)-1
    for i in range(len(res)-1,0,-1):
        ans.append(ar[j])
        j=res[i]
        if j==0:
            break

    for i in ans:
        print(i)

    return height[n-1]

B1=[1,2,4]
B2=[3,2,5]
print(BoxStacking(B1,B2))
