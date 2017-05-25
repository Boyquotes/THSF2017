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
with open('/home/noghost/TIM/json/messages.log', 'r') as mon_fichier:
    ligne = mon_fichier.read()
    for decoded in iterparse(ligne):
        out.append(ligne)
    out= dict(out)
    print (out)


'''
    with open('Out.json', 'w') as f:
        json.dump(out, f, indent=4)
'''

'''
    print("ETAPE 1 sortie out.append :")

    print(out)
    
    print('ETAPE 2')
 
    out_oDump = json.dumps(out)
    print (out_oDump)

    out_oLoads = json.loads(out_oDump)

    for count in out_oLoads:
        print count['HOST']

    #print(out_oLoads)

    for item in out_oLoads['HOSTS']:
        print (item["HOSTS"])



    d = parsed['out_oLoads']
    print (d['HOST'])
    #print(out_o)
    #print(out)
    #print(out_o['HOST'])
    print("FIN")

'''

'''
json.dumps transforme en json
json.loads

First of all, you should be using json.loads, not json.dumps. 
loads converts JSON source text to a Python value, while dumps goes the other way.

readable_json will be a list, and so readable_json['firstName'] is meaningless. 

The correct way to get the 'firstName' field of every element of a list is to eliminate the playerstuff = readable_json['firstName'] line and change for i in playerstuff: to for i in readable_json

'''
