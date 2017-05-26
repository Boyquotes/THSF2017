#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

from flask import Flask, Response, render_template, redirect, url_for, request, jsonify
from flask_wtf import Form
import urllib2
import sys
import sqlite3

import os.path

from rivescript import RiveScript
rs = RiveScript()
rs.load_directory("./brainADA")
rs.sort_replies()

from OpenSSL import SSL
context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('./certificats/ADA.key')
context.use_certificate_file('./certificats/ADA.crt')

from scapy.all import *

# PARTIE JSON A RESTRUCTURER
import json
import string

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
# FIN PARTIE JSON

app = Flask(__name__)

@app.route('/TIM')
def botAiml():
    return render_template('Machine.html',titre="TIM")

@app.route('/echo', methods=['POST'])
def echo():
    # le bot Riverscript est ici
    msg = request.form['text']
    msg = msg.strip("\n\t Ct,.;?!")
    response = rs.reply("localuser", msg)
    response = response
    return render_template('Machine.html', response=response)

@app.route('/listageMachines')
def requete():
    conn = None
    conn = sqlite3.connect('machines.db')
    cursor=conn.cursor()
    cursor.execute("""SELECT * FROM machines""");
    rows = cursor.fetchall()
    for row in rows:
    	print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
    return render_template('listageMachines.html', modele=rows)

#FORMULAIRE CREATION MACHINES
@app.route('/creationMachines', methods=['GET'])
def formulaire():
    return render_template('creationMachines.html',titre="formulaire")

# TRAITEMENT CREATION D UNE MACHINE
@app.route('/traitementCreation', methods=['POST'])
def traiter_donnees():
    # traiter les donnees recues
    # afficher la variable
    whatis = (request.form['whatis'])
    mac = (request.form['mac'])
    ip = (request.form['ip'])
    conn = None
    #Creation de la session de la base de donnee
    conn = sqlite3.connect('machines.db')
    #Create a client cursor to execute commands
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO machines (whatis, mac, ip) VALUES  (?,?,?)""",(whatis,mac, ip))
    conn.commit()
    return render_template('traitementCreation.html',  whatis=whatis, mac=mac)

@app.route('/modifierMachine', methods=['GET', 'POST'])
def formModRempli():
    conn = None
    conn = sqlite3.connect('machines.db')
    cursor = conn.cursor()
    mac = (request.form['mac'])
    cursor.execute(""" SELECT id_machines FROM machines WHERE mac =?;""",(mac,))  
    row = cursor.fetchall()
    index = row[0]

    if request.form['choix'] == 'sup':
        cursor.execute("DELETE FROM machines WHERE id_machines = ?;",(int(index[0]),))
        conn.commit()
        #return render_template('supprimer.html', modele=index[1] )
        return render_template('supprimer.html')

    elif request.form['choix'] == 'mod':
        cursor.execute(""" SELECT  whatis, mac, ip,id_machines FROM machines WHERE id_machines =?;""",(int(index[0]),))
        rows = cursor.fetchall()
        for row in rows:
        	id_machines = row[3]
        	ip = row[2]
        	whatis = row[0]
        	mac = row[1]
        return render_template('modifierMachine.html', id =id_machines,whatis=whatis, mac=mac, ip = ip)

@app.route('/modif', methods=['POST'])
def modifier_donnees():
    iD  = (request.form['id'])
    whatis = (request.form['whatis'])
    ip = (request.form['ip'])
    mac = (request.form['mac'])

    conn = None
    conn = sqlite3.connect('machines.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT whatis FROM machines WHERE id_machines =?;",(iD,))

    rows = cursor.fetchall()
    if rows:
        for row in rows:
            ID = row[0]
            cursor.execute("""UPDATE machines SET whatis=? ,mac=?, ip=? WHERE id_machines=?;""", (whatis, mac, ip, iD))
    conn.commit()
    return render_template('modif.html', whatis=whatis, ip=ip,mac=mac, id=iD)

@app.route('/code001')
def code001():
    return render_template('code001.html',titre="code001")

@app.route('/code002')
def code002():
    return render_template('code002.html',titre="code002")

@app.route('/code003')
def code003():
    return render_template('code003.html',titre="code003")

@app.route('/log')
def log():
    fichier = open("messages.log", "r")
    rawdata=fichier.read()
    fichier.close()

    logs=[]
    for decoded in iterparse(rawdata):
        logs.append(decoded)
    #logs =jsonify({'logs': logs})
    #logs =jsonify({'logs': logs})
    #logs = json.dumps(logs)
    logs = json.dumps(logs, ensure_ascii = False)
    #logs = json.dumps(logs, indent=2, separators=(', ', ': '))
    print (logs)
    return render_template('log.html',titre="out_logs",logs=logs, content_type="application/json; charset=utf-8" )
    

def event_stream():
    while True:
        with open('tableau.json', 'r') as mon_fichier:
            out = mon_fichier.read()
            out = json.dumps(json.loads(out))
        yield 'data: %s\n\n' % out
        time.sleep(10)

@app.route('/my_event_source')
def sse_request():
    return Response(
            event_stream(),
            mimetype='text/event-stream')

if __name__ == "__main__":
    context = ('ADA.crt', 'ADA.key')
    app.run(host='0.0.0.0', port=8080, ssl_context=context, threaded=True, debug=True)
