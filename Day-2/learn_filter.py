"""
✅ filter is used to filter out elements from an iterable based on a condition.

filter(function, iterable)
function → Returns True or False for each element.

iterable → Collection to filter.
"""
nums = [1,2,3,4,5,6,7,8,9,10]
filter_even = filter(lambda x : x*0,nums)
print(list(filter_even))