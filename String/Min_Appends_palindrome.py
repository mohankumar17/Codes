'''def isPalindrome(Str):
	Len = len(Str)
	if (Len == 1):
		return True
	ptr1 = 0
	ptr2 = Len - 1
	while (ptr2 > ptr1):
		if (Str[ptr1] != Str[ptr2]):
			return False
		ptr1 += 1
		ptr2 -= 1

	return True

def isPalindrome2(Str):
	if Str==Str[::-1]:
		return True
	return False

def noOfAppends(s):
	if (isPalindrome2(s)):
		return 0
	s=s[1:]
	return 1 + noOfAppends(s)

se = "abede"
s = [i for i in se]
print(noOfAppends(s))
'''

class Solution:
    # @param A : string
    # @return an integer
    def isPal(self,A,i,j):
        #t=A[i:j+1]
        #if t==t[::-1]:
        #    return True
        #return False
        while i<j:
            if A[i]!=A[j]:
                return False
            i=i+1
            j=j-1
        return True

    def solve(self, A):
        i=0
        j=len(A)-1
        m=0
        while i<j:

            if A[i]==A[j]:
                if self.isPal(A,i,j):
                    return m

            i=i+1
            m=m+1

        return m
