import json



with open('log.json', 'r') as f:
	datas = json.dump(f)
	print(datas)

