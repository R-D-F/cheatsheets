import json
from datetime import datetime

# 1️⃣ Convert Python Dictionary to JSON (Serialization)
data = {"name": "Alice", "age": 25, "city": "New York"}
json_string = json.dumps(data, indent=4, sort_keys=True)
print("Serialized JSON:\n", json_string)

# 2️⃣ Convert JSON String to Python Dictionary (Deserialization)
json_data = '{"name": "Alice", "age": 25, "city": "New York"}'
parsed_data = json.loads(json_data)
print("Deserialized JSON:\n", parsed_data)

# 3️⃣ Write JSON to a File
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# 4️⃣ Read JSON from a File
with open("data.json", "r") as file:
    file_data = json.load(file)
print("Read from file:\n", file_data)

# 5️⃣ JSON with Lists
data_list = {"name": "Bob", "age": 30, "skills": ["Python", "JavaScript", "SQL"]}
print("JSON with List:\n", json.dumps(data_list, indent=4))

# 6️⃣ JSON with Nested Objects
data_nested = {
    "user": {
        "name": "John",
        "contact": {
            "email": "john@example.com",
            "phone": "123-456-7890"
        }
    }
}
print("Nested JSON:\n", json.dumps(data_nested, indent=4))

# 7️⃣ Error Handling in JSON
invalid_json = '{ "name": "Alice", age: 25 }'  # Invalid JSON
try:
    parsed_invalid = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print("Error loading JSON:", e)

# 8️⃣ Convert Python Object to JSON (Custom Encoding)
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data_custom = {"name": "Alice", "joined": datetime.now()}
json_string_custom = json.dumps(data_custom, indent=4, cls=CustomEncoder)
print("Custom Encoded JSON:\n", json_string_custom)

# 9️⃣ Convert JSON to Python Object (Custom Decoding)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def decode_person(dct):
    return Person(dct["name"], dct["age"])

json_person = '{"name": "Alice", "age": 25}'
person_obj = json.loads(json_person, object_hook=decode_person)
print("Decoded Person Object:", person_obj.name, person_obj.age)
