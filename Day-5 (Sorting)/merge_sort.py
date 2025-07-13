"""
Merge two sorted Arrays
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_two_arrays(left,right)

def merge_two_arrays(left, right):

    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j +=1
    if i < len(left):
        #result.extend(left[i:])
        while i < len(left):
            result.append(left[i])
            i += 1
    if j < len(right):
        #result.extend(right[j:])
        while j < len(right):
            result.append(right[j])
            j += 1
    return result
l = [1,1,6,99,202,101,65,88,802,3,4,5,66,76,77,88]
print(merge_sort(l))

"""
TC: O(log2 N X (N + M))
SC: O(N)
"""