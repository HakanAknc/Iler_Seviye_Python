import json

person_string = '{"name": "Hakan", "Diller": ["Python","C#"]}'

# print(person["name"])
# print(person["Diller"])

#print(json.loads(person_string))

# a = json.loads(person_string)
# a = a["name"]

with open("person.json") as f:
    data = json.load(f)
    print(data)
