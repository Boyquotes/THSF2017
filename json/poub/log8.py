import json

with open('messages.log', 'r') as f:
    json.dump(obj, f, indent=4)