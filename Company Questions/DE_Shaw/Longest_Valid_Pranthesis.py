def func(s):
    n=len(s)
    res=0
    st=[]
    st.append(-1)
    for i in range(0,n):
        if s[i]=='(':
            st.append(i)
        else:
            st.pop()
            if len(st):
                res=max(res,i-st[len(st)-1])
            else:
                st.append(i)
    return res

s="))((())())("
print(func(s))
