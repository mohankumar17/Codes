def computeLPS(m,p,lps):
    len=0
    i=1
    while i<m:
        if p[i]==p[len]:
            len=len+1
            lps[i]=len
            i=i+1

        elif len!=0:
            len=lps[len-1]
        else:
            lps[i]=0
            i=i+1

def KMP(s,p):
    m=len(p)
    n=len(s)
    lps=[0]*m
    computeLPS(m,p,lps)
    i=0
    j=0
    ans=[]

    while i<n:
        if s[i]==p[j]:
            i=i+1
            j=j+1
        if j==m:
            ans.append(i-j)
            j=lps[j-1]

        elif i<n and s[i]!=p[j]:
            if j!=0:
                j=lps[j-1]
            else:
                i=i+1
    return ans

s='ORRGEKSFORGEEKS'
p='RRG'
print(KMP(s,p))


'''def computeLPSArray(pat, M, lps):
	len = 0
	i = 1
	while i < M:
		if pat[i]== pat[len]:
			len += 1
			lps[i] = len
			i += 1
		else:
			# AAACAAAA and i = 7. The idea is similar to search step.
			if len != 0:
				len = lps[len-1]
			else:
				lps[i] = 0
				i += 1

def KMPSearch(pat, txt):
	M = len(pat)
	N = len(txt)
	lps = [0]*M

	computeLPSArray(pat, M, lps)
	j = 0
	i = 0
	while i < N:
		if pat[j] == txt[i]:
			i += 1
			j += 1

		if j == M:
			print(i-j) #index found=i-j
			j = lps[j-1]

		elif i < N and pat[j] != txt[i]:
			if j != 0:
				j = lps[j-1]
			else:
				i += 1

#txt=input()
#pat=input()

txt = "ABCBDABABDABADCABAB"
pat = "ABAB"
KMPSearch(pat, txt)
'''
