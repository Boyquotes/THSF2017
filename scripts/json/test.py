import json

data = '{"name": "noghost","age":"43"}'

parsed_json = json.loads(data)

print(parsed_json['name'])
print(parsed_json['age'])
