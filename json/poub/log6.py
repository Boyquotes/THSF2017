import json
import re

import json
obj = {"TAGS":".source.s_src","SOURCEIP":"127.0.0.1","SOURCE":"s_src","SEQNUM":"1","PROGRAM":"syslog-ng","PRIORITY":"notice","PID":"8046","MESSAGE":"syslog-ng starting up; version='3.5.6'","HOST_FROM":"deuX260","HOST":"deuX260","FACILITY":"syslog","DATE":"May  4 21:53:41"}
print(json.dumps(obj, indent=4))