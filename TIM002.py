#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

from flask import Flask, Response, render_template, redirect, url_for, request, jsonify
from flask_wtf import Form
import urllib2
import sys
import sqlite3
import re

import os.path

from rivescript import RiveScript
rs = RiveScript()
rs.load_directory("./brainADA")
rs.sort_replies()

from OpenSSL import SSL
context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('/home/noghost/TIM/certificats/ADA.key')
context.use_certificate_file('/home/noghost/TIM/certificats/ADA.crt')

from scapy.all import *

import json
import string

app = Flask(__name__)

@app.route('/TIM')
def botAiml():
    return render_template('Machine.html',titre="TIM")
@app.route('/code001')
def code001():
    return render_template('code001.html',titre="code001")

@app.route('/code002')
def code002():
    return render_template('code002.html',titre="code002")

@app.route('/code003')
def code003():
    return render_template('code003.html',titre="code003")

@app.route('/code004')
def code004():
    return render_template('code004.html',titre="code004")

@app.route('/log')
def  log():
    return render_template('log.html',titre="log")

# VERSION LOGS
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
        with open('messages.log', 'r') as mon_fichier:
            ligne = mon_fichier.read()
            for decoded in iterparse(ligne):
                out.append(ligne)
            print(out)

        yield 'data: %s\n\n' % out
        
        time.sleep(40)



@app.route('/my_event_source')
def sse_request():
    return Response(
            event_stream(),
            mimetype='text/event-stream')

if __name__ == "__main__":
    context = ('ADA.crt', 'ADA.key')
    app.run(host='0.0.0.0', port=8080, ssl_context=context, threaded=True, debug=True)
