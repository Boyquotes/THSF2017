import json
import os
hostname = "8.8.8.8" #example
response = os.system("ping -c 1 " + hostname)

with open('tableau.json', 'r') as f:
        datas = json.load(f)
        
if response ==0:
    with open('tableau.json', 'w') as outfile:
        datas['terrain'][0]= [1, 1, 1, 1, 1, 1,1 , 1]
        json.dump(datas, outfile)
