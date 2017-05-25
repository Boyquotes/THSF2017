import json
import os

hostname = "192.168.97.203" #example

response = os.system("ping -c 1 " + hostname)

with open('/home/noghost/TIM/tableau.json', 'r') as f:
        datas = json.load(f)
        
if response == 0:
    with open('/home/noghost/TIM/tableau.json', 'w') as outfile:
        #datas['terrain'][0]= [2, 1, 1, 1, 1, 1,1 , 1]
        datas['terrain'][0][1] = 1
        json.dump(datas, outfile)
else:
	with open('/home/noghost/TIM/tableau.json', 'w') as outfile:
		#datas['terrain'][0]= [0, 1, 1, 1, 1, 1,1 , 1]
		datas['terrain'][0][1] = 0
		json.dump(datas, outfile)
