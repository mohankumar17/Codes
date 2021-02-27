class Solution:
# @param A : tuple of integers
# @return a strings
    def largestNumber(self, A):
        A = list(A)
        a_len = len(A)
        if a_len < 1:
            return ''
        if a_len == 1:
            return str(A[0])

        result = self.the_sort(A)
        str_result = [str(x) for x in result[::-1]]
        joined_res = ''.join(str_result).lstrip('0')

        return joined_res if joined_res != '' else '0'

    def the_sort(self, arr):
        a_len = len(arr)

        if a_len < 2:
            return arr
        mid = a_len // 2
        left_half = self.the_sort(arr[0:mid])
        right_half = self.the_sort(arr[mid:])
        result = self.merge(left_half, right_half)
        return result

    def merge(self, left, right):
        helper = left + right
        left_pointer = 0
        right_pointer = 0
        current = 0

        while left_pointer < len(left) and right_pointer < len(right):
            str_l = str(left[left_pointer])
            str_r = str(right[right_pointer])
            num_l = int(str_l + str_r)
            num_r = int(str_r + str_l)

            if num_l < num_r:
                helper[current] = left[left_pointer]
                left_pointer += 1
            else:
                helper[current] = right[right_pointer]
                right_pointer += 1
            current += 1

        while left_pointer < len(left):
            helper[current] = left[left_pointer]
            current += 1
            left_pointer += 1

        return helper
from itertools import permutations
def largestNumberPerm(ar):
    ar=[str(i) for i in ar]
    p=permutations(ar)
    m=0
    for i in p:
        #print(i)
        s=list(i)
        s=''.join(s)
        if int(s)>m:
            m=int(s)
    return str(m)

def largeUtil(a,b):
    ab=a+b
    ba=b+a
    if ab>ba:
        return 1
    else:
        return 0
def largestNumber(ar):
    ar=sorted(ar,key=largeUtil)
    return ar

ar=[3, 30, 34, 5, 9]
print(largestNumberPerm(ar))
print(largestNumber(ar))
