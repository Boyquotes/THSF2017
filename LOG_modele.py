#!flask/bin/python
from flask import Flask, jsonify
import re
import json
import time

app = Flask(__name__)

nonspace = re.compile(r'\S')
def iterparse(j):
    decoder = json.JSONDecoder()
    pos = 0
    while True:
        matched = nonspace.search(j, pos)
        if not matched:
            break
        pos = matched.start()
        decoded, pos = decoder.raw_decode(j, pos)
        yield decoded

fichier = open("messages.log", "r")
rawdata=fichier.read()
fichier.close()


logs=[]
for decoded in iterparse(rawdata):
    logs.append(decoded)

@app.route('/logs', methods=['GET'])
def get_tasks():
    return jsonify({'logs': logs})

if __name__ == '__main__':
    app.run(debug=True)

