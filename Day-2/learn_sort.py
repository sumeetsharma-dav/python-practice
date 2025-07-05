"""
What is sort in Python?
Definition
✅ The sort method sorts a list in place.
✅ The sorted function returns a new sorted list.
list.sort(key=function, reverse=False)
or
sorted(iterable, key=function, reverse=False)
"""
pairs = [(1, 3), (2, 2), (3, 1)]
sorted_pair = sorted(pairs,key=lambda x:x[1])
print(sorted_pair)

# sort string by their length
words = ["apple", "kiwi", "banana"]
sorted_words = sorted(words,key=lambda x: len(x),reverse=False)
print(sorted_words)