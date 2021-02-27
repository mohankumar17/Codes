#Time: O(log(m+n)), m-len(arr1) and n-len(arr2)
import sys
def median(A,B):
    if len(A)>len(B):
        A,B=B,A
    start_a=0
    end_a=len(A)
    start_b=0
    end_b=len(B)
    while start_a<=end_a:
        position_a=(start_a+end_a)//2
        position_b=((len(A)+len(B)+1)//2)-position_a

        if position_a==0:
            max_left_a=-sys.maxsize
        else:
            max_left_a=A[position_a-1]

        if position_a==len(A):
            min_right_a=sys.maxsize
        else:
            min_right_a=A[position_a]

        if position_b==0:
            max_left_b=-sys.maxsize
        else:
            max_left_b=B[position_b-1]

        if position_b==len(B):
            min_right_b=sys.maxsize
        else:
            min_right_b=B[position_b]

        if (max_left_a<=min_right_b) and (max_left_b<=min_right_a):
            if (len(A)+len(B))%2==0:
                return (max(max_left_a,max_left_b)+min(min_right_a,min_right_b))/2
            else:
                return max(max_left_a,max_left_b)
        elif max_left_a>min_right_b:
            end_a=position_a-1
        else:
            start_a=position_a+1

arr1 = [1,5,7]
arr2 = [2,4,6]
#ans=3.5
print(median(arr1, arr2))
