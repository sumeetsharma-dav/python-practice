"""
new_list = [expression for item in iterable]
Components:
expression   : This is the value that will be added to the new list for each item. It can be the item itself, or a transformation of the item.
item         : This is a variable that takes on the value of each element in the iterable during the iteration.
iterable     : This is any object that can be iterated over, such as a list, tuple, string, or range object.
"""

"""
1. Find the square of each element of list
"""
list = range(10)
squared_list = [num*num for num in list]
print(squared_list)

"""
2. Find the even numbers in a list
"""
find_even = range(20)
even_list = [num for num in find_even if num%2 == 0]
print(even_list)

"""
3. Convert to Uppercase
"""
names = ["alice", "bob", "charlie"]
Upper_names = [name.title() for name in names]
print(Upper_names)

"""
Nested List Flatten
"""
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flatten_list = [nnum for num in nested for nnum in num ]
print(flatten_list)

