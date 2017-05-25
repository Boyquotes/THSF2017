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

out = []
with open('/home/noghost/TIM/json/messages2.log', 'r') as mon_fichier:
    ligne = mon_fichier.read()
    for decoded in iterparse(ligne):
        out.append(ligne)

    print(out[0][0])

    print (out)

    # TEST LOADS

    obj = json.loads(out)
    print (repr(obj))

'''
    with open('Out.json', 'w') as f:
        json.dump(out, f, indent=4)
'''