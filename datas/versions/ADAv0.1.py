#!/usr/bin/python2.7
# -*-coding:Utf-8 -*

from flask import Flask, render_template, redirect, url_for, request
from flask.ext.wtf import Form
import urllib2
import psycopg2
import psycopg2.extras
import sys

from rivescript import RiveScript

rs = RiveScript()
rs.load_directory("./brainADA")
rs.sort_replies()

app = Flask(__name__)

@app.route('/ADA')
def botAiml():
    return render_template('Machine.html',titre="ADA")

@app.route('/echo', methods=['POST'])
def echo():
    # le bot Riverscript est ici
    msg = request.form['text']
    msg = msg.strip("\n\t Ct,.;?!")
    response = rs.reply("localuser", msg)
    response = response
    return render_template('Machine.html', response=response)

@app.route('/creationMachines', methods=['GET'])
def formulaire():
    # afficher le formulaire de creation de machine
    return render_template('creationMachines.html',titre="formulaire")

# TRAITEMENT CREATION D UNE MACHINE
@app.route('/traitementCreation', methods=['POST'])
def traiter_donnees():
    # traiter les données recues
    # afficher la variable
    # companies = [company.decode("utf-8") for company in companies]
    modele = (request.form['modele'])
    whatis = (request.form['whatis'])
    mac = (request.form['mac'])
    ip = (request.form['ip'])
    db_con = None
    #Creation de la session de la base de donnee
    db_con = psycopg2.connect(database='myDataGoliath', user='postgres', password='postgres')
    #Create a client cursor to execute commands
    cursor = db_con.cursor()
    cursor.execute("INSERT INTO machines (modele, whatis, mac, ip) VALUES  (%s, %s,%s,%s)",(modele,whatis,mac, ip))
    db_con.commit()
    return render_template('traitementCreation.html', modele=modele, whatis=whatis, mac=mac)

@app.route('/modif', methods=['POST'])
def modifier_donnees():
    # traiter les données reçues
    # afficher la variable

    #comment recuperer les variables cachees ?
    modeleCache = (request.form['modeleCache'])
    modele = (request.form['modele'])
    whatis = (request.form['whatis'])
    ip = (request.form['ip'])
    mac = (request.form['mac'])

    db_con = None
    #Create a database session
    db_con = psycopg2.connect(database='myDataGoliath', user='postgres', password='postgres')
    #Create a client cursor to execute commands
    cursor = db_con.cursor()
    
    cursor.execute("SELECT id_machines FROM machines WHERE modele =%s;",(modeleCache,))

    rows = cursor.fetchall()
    if rows:
        for row in rows:
            ID = row[0]
            cursor.execute("UPDATE machines SET modele = %s, whatis=%s ,mac=%s, ip=%s WHERE id_machines=%s;", (modele, whatis, mac, ip, ID))
    db_con.commit()
    return render_template('modif.html', modele=modele, whatis=whatis, ip=ip,mac=mac )

@app.route('/modifierMachine', methods=['GET', 'POST'])
def formModRempli():
    #comment recuperer les variables cachees ?
    db_con = None
    db_con = psycopg2.connect(database='myDataGoliath', user='postgres', password='postgres')
    cursor = db_con.cursor()
    modele = (request.form['modele'])
    cursor.execute("SELECT id_machines FROM machines WHERE modele =%s;",(modele,))    
    row = cursor.fetchall()
    index = row[0]

    if request.form['choix'] == 'sup':
        cursor.execute("DELETE FROM machines WHERE id_machines = %s;",(int(index[0]),))
        db_con.commit()
        #return render_template('supprimer.html', modele=index[1] )
        return render_template('supprimer.html')

    elif request.form['choix'] == 'mod':
        cursor.execute("SELECT modele, whatis, mac, ip FROM machines WHERE id_machines =%s;",(index,))
        rows = cursor.fetchall()
        
        for row in rows:
            modele = row[0]
            whatis = row[1]
            mac = row[2]
            ip = row[3]

        return render_template('modifierMachine.html',modele=modele, whatis=whatis, mac=mac, ip = ip)

@app.route('/listageMachines')
def requete():
    db_con = None
    #Create a database session
    db_con = psycopg2.connect(database='myDataGoliath', user='postgres', password='postgres')
    #Create a client cursor to execute commands
    cursor = db_con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #cursor.execute ("select nom from adherents")
    #rows = cursor.fetchall()
    cursor.execute("SELECT * FROM machines");
    rows = cursor.fetchall()
    db_con.commit()
    return render_template('listageMachines.html', modele=rows)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)