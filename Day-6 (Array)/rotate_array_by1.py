def rotate_by_1(nums):
    nums[:] = [nums[-1]] + nums[:len(nums)-1]
    return nums

print(rotate_by_1([5,-2,3,9,0,6,10,7]))