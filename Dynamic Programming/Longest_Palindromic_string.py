def printSubStr(st, low, high) :
	print(st[low : high + 1])
	return None

def longestPalSubstr(st) :
	n = len(st)
	table = [[False for x in range(n)] for y in range(n)]

	#sub-string of length 1 is always palindrome.
	maxLength = 1
	i = 0
	while (i < n) :
		table[i][i] = True
		i = i + 1

	# check for sub-string of length 2.
	maxLength = 2
	start = 0
	i = 0
	while i < n - 1 :
		#if 2 characters are same then they are also palidrome
		if (st[i] == st[i + 1]) :
			table[i][i + 1] = True
			start = i
			maxLength = 2
		i = i + 1

	# Check for lengths greater than 2.
	# k is length of substring
	k = 3
	while k <= n :
		# Fix the starting index
		i = 0
		while i < (n - k + 1) :
			# Get the ending index of substring from starting index i and length k
			j = i + k - 1

			# checking for sub-string from ith index to jth index
			#if st[i + 1] to st[j-1] is a palindrome
			if (table[i + 1][j - 1] and st[i] == st[j]) :
				table[i][j] = True

				if (k > maxLength) :
					start = i
					maxLength = k
			i = i + 1
		k = k + 1

	printSubStr(st, start,start + maxLength - 1)
	return maxLength

#st = "forgeeksskeegfor"
st="tmamg"
l = longestPalSubstr(st)
print (l)

#Brute-Force
'''
class Solution:
    def isPalin(self,s,i,j):
        #print(s[i:j+1])
        while i<j:
            if s[i]!=s[j]:
                return False
            i=i+1
            j=j-1

        return True

    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        import sys
        m=-sys.maxsize
        ans=""
        for l in range(1,n+1):
            for i in range(0,n-l+1):
                j=i+l-1
                #print(l,i,j)
                if self.isPalin(s,i,j):
                    if j-i+1>m:
                        m=j-i+1
                        ans=s[i:j+1]
        return ans
        
'''
