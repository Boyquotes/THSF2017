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


#rawdata = '{"TAGS":".source.s_src","SOURCEIP":"127.0.0.1","SEQNUM":"1711","PROGRAM":"CRON","PRIORITY":"info","PID":"9389","MESSAGE":"pam_unix(cron:session): session closed for user noghost","LEGACY_MSGHDR":"CRON[9389]: ","HOST_FROM":"deuX260","HOST":"deuX260","FACILITY":"authpriv","DATE":"May  3 22:39:11"}'


with open('messages2.log', 'r') as rawdata:
    datas = json.load(rawdata)
    for decoded in iterparse(datas):
        print(decoded)
    #print("########################################")
    #print(decoded['HOST'])
