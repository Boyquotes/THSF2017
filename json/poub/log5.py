import json

with open('messagesOut.json', 'r') as f:
	datas = json.load(f)

	print(datas[0][0])