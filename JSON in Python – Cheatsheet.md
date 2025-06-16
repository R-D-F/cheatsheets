

Python has a built-in module called `json` for parsing JSON data.

---

## 📦 Importing the Module
```python
import json
```

---

## 📖 Reading JSON

### From a JSON string
```python
json_str = '{"name": "Alice", "age": 30}'
data = json.loads(json_str)  # Convert JSON string to Python dict
```

### From a JSON file
```python
with open('data.json', 'r') as f:
    data = json.load(f)  # Load JSON file into Python dict
```

---

## 📝 Writing JSON

### To a JSON string
```python
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)  # Convert Python dict to JSON string
```

### To a JSON file
```python
with open('data.json', 'w') as f:
    json.dump(data, f)  # Write dict to JSON file
```

---

## 🎛️ Options for `json.dump()` / `json.dumps()`

### Pretty Print
```python
json.dumps(data, indent=4)
```

### Sorted Keys
```python
json.dumps(data, sort_keys=True)
```

### Ensure ASCII (defaults to True)
```python
json.dumps(data, ensure_ascii=False)
```

---

## 🧪 Converting Between Python and JSON

| JSON        | Python     |
|-------------|------------|
| object      | dict       |
| array       | list       |
| string      | str        |
| number      | int, float |
| true/false  | True/False |
| null        | None       |

---

## 🔁 Read + Write Example

```python
import json

# Read
with open('input.json') as f:
    data = json.load(f)

# Modify
data["new_key"] = "new_value"

# Write
with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)
```

---

## 🚨 Common Errors

- `json.decoder.JSONDecodeError`: The JSON string or file is malformed.
- `TypeError: Object of type ... is not JSON serializable`: You're trying to serialize a custom object. Use `default=str` or a custom encoder.

---

## 🧩 Handling Custom Objects

### Using `default` with `dumps`
```python
from datetime import datetime

def encode_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")

json.dumps({"time": datetime.now()}, default=encode_datetime)
```
