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

rawdata = '{"TAGS":".source.s_src","SOURCEIP":"127.0.0.1","SEQNUM":"1711","PROGRAM":"CRON","PRIORITY":"info","PID":"9389","MESSAGE":"pam_unix(cron:session): session closed for user noghost","LEGACY_MSGHDR":"CRON[9389]: ","HOST_FROM":"deuX260","HOST":"LINUX_HOST","FACILITY":"authpriv","DATE":"May  3 22:39:11"}{"TAGS":".source.s_src","SOURCEIP":"127.0.0.1","SEQNUM":"1711","PROGRAM":"CRON","PRIORITY":"info","PID":"9389","MESSAGE":"pam_unix(cron:session): session closed for user noghost","LEGACY_MSGHDR":"CRON[9389]: ","HOST_FROM":"deuX260","HOST":"BSD_HOST","FACILITY":"authpriv","DATE":"May  3 22:39:11"}'

compteur = 0
for decoded in iterparse(rawdata):
    compteur = compteur +1
    print ("################################## "+str(compteur))
    #print(decoded)
    #print(decoded['HOST'])
    #print(decoded['DATE'])
    decoded.append(decoded)

print (decoded)
