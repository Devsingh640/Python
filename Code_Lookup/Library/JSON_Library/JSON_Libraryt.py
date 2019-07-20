import json


z =  '{ "name":"John", "age":30, "city":"New York"}'
k = json.loads(z)
print(k["age"])


x = {"first_name": "OM",
    "middle_name": "DEV",
    "last_name": "SINGH",
    "phone_number": 8826621005}
y = json.dumps(x,indent=4)
print(y)


print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


p = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(p, indent=4, separators=(". ", " = ")))

print(json.dumps(p, indent=4, sort_keys=True))