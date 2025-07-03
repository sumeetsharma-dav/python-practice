import json
json_str = '{"name": "John", "age": 32, "skills": ["Python", "SQL", "Spark"]}'
dict_skills = json.loads(json_str)
print(dict_skills)