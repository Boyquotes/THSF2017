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

app = Flask(__name__)

@app.route('/log')
def  log():
    fichier = open("messages.log", "r")
    rawdata=fichier.read()
    fichier.close()
	
    for decoded in iterparse(rawdata):
        out = decoded
        
    return render_template('log2.html',titre="log",out=out)
        	

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
