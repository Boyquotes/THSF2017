import urllib2

url = 'http://127.0.0.1/CTF/CTF3/post_ctf_3.php'

headers ={'User-Agent':'Mozilla/5.0 (IPhone)'}

request = urllib2.Request(url,None,headers)

response = urllib2.urlopen(request)
payload = response.read()

headers = response.headers

print(headers)

print (payload)