import json
import re

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

data=[]
with open('messages.log', 'r') as rawdata:
    for ligne in rawdata:
        decoded = iterparse(rawdata)

        print(decoded)
        print(decoded['HOST'][1])
        #print(decoded['DATE'])
