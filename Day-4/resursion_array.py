"""
reverse the array using recursion
"""
def fun(left,right,num):
    if left >= right:
        return num
    num[left], num[right] = num[right], num[left]
    fun(left+1,right-1,num)
    return num



def fun_while(left,right,num):
    while (left <= right):
        num[left], num[right] = num[right], num[left]
        left += 1
        right -= 1
    return num

num = [5,7,3,2,6,1,5,9]
print(fun_while(0,7,num))

"""
TC = O(N/2)
SC = O(N/2)
"""