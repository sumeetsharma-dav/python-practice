"""
📝 ✅ 1. List Comprehensions
Level 1 – Easy
 . Create a list of squares from 1 to 10 using list comprehension.
 . From a list of numbers, create a new list containing only even numbers.

Level 2 – Medium
 . Given a list of words, create a new list containing the length of each word.
 . Flatten a nested list [[1,2],[3,4],[5,6]] into a single list using nested list comprehension.

Level 3 – Hard
 . For a list of words, create a list of uppercase words with length > 3 using list comprehension with a condition.

📝 ✅ 2. Dictionaries
Level 1 – Easy
 . Create a dictionary with 3 fruits as keys and their prices as values. Print all keys.

Level 2 – Medium
 . Update the price of one fruit and add a new fruit. Print the updated dictionary.
 . Given a dictionary of students and marks, increase marks by 5 for all students scoring below 50.

Level 3 – Hard
 . You have a dictionary of employees with departments. Print only those employees whose department name starts with 'F'.

📝 ✅ 3. JSON Module
Level 1 – Easy
 . Convert a given JSON string to dict and print a value for a given key.

Level 2 – Medium
 . Parse a nested JSON string and print a nested value (e.g., city inside address).
 . Convert a Python dict to JSON string using json.dumps() and print it.

Level 3 – Hard
 . Given a list of JSON strings representing users, load them into dicts and print names of users aged above 25.

📝 ✅ 4. Combined Practice
Level 4 – Advanced
 . You are given a list of dictionaries each representing an employee with name, department, and salary.
 . Use list comprehension to create a list of names of employees who work in 'Engineering' and earn more than 50000.
"""

# Level 1
square_list = [num*num for num in range(11)]
print(square_list)
square_list_even = [num for num in square_list if num%2 == 0]
print(square_list_even)

#Level 2
word_list = ["hello", "my", "name", "is", "slim", "shady"]
print(word_list)
word_list_length = [len(word) for word in word_list]
print(word_list_length)

list =  [[1,2],[3,4],[5,6]]
flatten_list = [nnum for num in list for nnum in num]
print(flatten_list)

#Level 3
hard_list = ["a","bb","ccc","dddd","eeeee"]
hard_list_upper = [word.upper() for word in hard_list if len(word)>3]
print(hard_list_upper)

