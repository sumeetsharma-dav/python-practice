"""
Dictionary is same as map in scala or java
Let's declare one
"""
empty_dict = {}
emp_salary_dict ={
    "Alex": 15000,
    "John" : 16000,
    "Jose" : 10000
}
print(emp_salary_dict)

"""
Accessing Value
"""
print(emp_salary_dict["Alex"])
print(emp_salary_dict.get("Alex1","Not Found"))

"""
Update Value
"""
emp_salary_dict["Alex"] = "20000"
print(emp_salary_dict.get("David","Not Found"))
print(emp_salary_dict)

"""
Add Value
"""
emp_salary_dict["David"] = "21000"
print(emp_salary_dict.get("David","Not Found"))
print(emp_salary_dict)

"""
Delete Value
"""
del emp_salary_dict["David"]
print(emp_salary_dict.get("David","Not Found"))
print(emp_salary_dict)

"""
Iterating Over Dictionary
"""
for k, v in emp_salary_dict.items():
    print(f"{k} has salary {v}")

"""
Practice Task
 . Create a dictionary with 3 students and their marks. Then:
 . Print all student names.
 . Increase marks by 10 for each student.
 . Add a new student.
 . Print the updated dictionary.
"""
student = {}
student["Ali"] = 50
student["Ahmad"] = 60
student["Yusuf"] = 70
print(student)
for names in student:
    print(names)
for names in student:
    student[names] = student[names] + 10
print(student)

"""
You have a dictionary of employees and their departments:

python
Copy
Edit
employees = {
    "Ali": "HR",
    "Ahmad": "Finance",
    "Yusuf": "Engineering",
    "Sara": "Marketing"
}
🔹 Tasks:

Print all employee names who work in Engineering or Marketing.

Change the department of Ahmad to Operations.

Add a new employee "Fatima" in Sales department.

Delete Ali from the dictionary.

Print the final updated dictionary.
"""
employees = {
    "Mike": "HR",
    "Joe": "Finance",
    "Monika": "Engineering",
    "Peter": "Marketing"
}
for emp, depart in employees.items():
    #if depart == "Marketing" or depart == "Engineering":
    if depart in ["Marketing","Engineering"]:
        print(emp)
employees["Joe"] = "Operations"
print(employees)
employees["Laura"] = "Finance"
print(employees)
del employees["Mike"]
print(employees)