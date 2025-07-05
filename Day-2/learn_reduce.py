"""
It is in the functools module, so you need to import it:
from functools import reduce

reduce(function, iterable, initializer)
function: takes two arguments and returns a single value.
iterable: list, tuple, etc.
initializer (optional): starting value.
"""
from functools import reduce
nums = [1,2,3,4,5,6,7,8,9,10]
sum_nums = reduce(lambda x,y:x+y,nums,5)
print(sum_nums)
# concat all
given = ["a", "b", "c", "d"]
conc = reduce(lambda x,y: x+y,given)
print(conc)
# Find the maximum number in [10, 5, 25, 3, 7] using reduce.
nums = [10, 5, 25, 3, 7]
fmax = reduce(lambda x,y:max(x,y),nums)
print(fmax)