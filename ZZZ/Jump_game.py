def func(nums):
    if len(nums)==1:
        return True
    n=len(nums)-1
    i=0
    while i<n:
        if nums[i]+i>=n:
            return True
        i=i+1
    return False
nums=[0]
print(func(nums))
