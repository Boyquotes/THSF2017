#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

# VERSION SIMPLIFIEE

from flask import Flask, Response, render_template, redirect, url_for, request, jsonify
from flask_wtf import Form
import urllib2
import sys, time, re, json, urllib2, string
'''import time
import re
import json
import string'''


app = Flask(__name__)

@app.route('/code001')
def code001():
    return render_template('code001.html',titre="code001")

@app.route('/code002')
def code002():
    return render_template('code002.html',titre="code002")

@app.route('/log')
def  log():
    return render_template('log.html',titre="log")

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

def event_stream():
    out = []
    while True:
        fichier = open("messages.log", "r")
        rawdata=fichier.read()
        fichier.close()
        
        for decoded in iterparse(rawdata):
            out = decoded
            print(out)
            yield 'data: %s\n\n' % out
        
        time.sleep(20)


@app.route('/my_event_source')

def sse_request():
    return Response(
            event_stream(),
            mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
