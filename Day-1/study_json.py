import json
json_str = '{"name": "John", "age": 32, "skills": ["Python", "SQL", "Spark"]}'
dict_skills = json.loads(json_str)
print(dict_skills)
print(type(dict_skills))

"""
Lets see nested json
"""
nested_json = '''
{
  "employee": {
    "name": "Eric",
    "details": {
      "age": 30,
      "department": "Finance",
      "skills": ["Excel", "Finance Modelling"]
    }
  }
}
'''
nested = json.loads(nested_json)
print(nested["employee"]["name"])
print(nested["employee"]["details"]["age"])
print(nested["employee"]["details"]["skills"][0])
print(nested["employee"]["details"]["skills"][1])
print(nested)
api_call_dump = json.dumps(nested)
print(api_call_dump)
print(type(api_call_dump))


"""
Load the following JSON string to dict:
{
  "course": "Data Engineering",
  "topics": {
    "week1": ["Python Basics", "JSON"],
    "week2": ["SQL", "Pandas"]
  }
}
Print:
 . The course name
 . Week1 topics
 . The first topic in week2
"""
jstring = '''
{
    "course": "Data Engineering",
    "topics": {
        "week1": ["Python Basics", "JSON"],
        "week2": ["SQL", "Pandas"]
    }
}
'''

dict = json.loads(jstring)
print(dict["course"])
print(dict["topics"]["week1"])
print(dict["topics"]["week2"][0])
