import os
hostname = "8.8.8.8" #example
response = os.system("ping -c 1 " + hostname)

#and then check the response...
print (response)

if response == 0:
    print ("ok")
