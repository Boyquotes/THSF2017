#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

logs = [
   
   {"TAGS":".source.s_src","SOURCEIP":"127.0.0.1","SEQNUM":"354","PROGRAM":"CRON","PRIORITY":"info","PID":"5170","MESSAGE":"pam_unix(cron:session): session closed for user noghost","LEGACY_MSGHDR":"CRON[5170]: ","HOST_FROM":"deuX260","HOST":"deuX260","FACILITY":"authpriv","DATE":"May 10 07:45:11"}
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'logs': logs})

if __name__ == '__main__':
    app.run(debug=True)


