"""
map(function, iterable)
function → The function to apply (can be lambda or a defined function).
iterable → The collection of items to process.
"""

num = [1,2,3,4,5,6]
sq_list = map((lambda x: x*x), num)
print(list(sq_list))

"""
1. map does not modify the original list.
2. It returns a map object, which is lazy (evaluated when used).
3. You can combine lambda + map for quick one-line transformations.
"""