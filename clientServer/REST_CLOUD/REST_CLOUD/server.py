from flask import Flask, json, request, render_template
import random
import os
import dbclient as db
import sys

api = Flask(__name__)
mydb = db.connect()
if mydb is None:
    print("Errore connesione al DB")
    sys.exit()

if not os.path.isfile('utenti.json'):
    with open("utenti.json", "w") as json_file:
        json.dump({}, json_file)
        
if not os.path.isfile('anagrafe.json'):
    with open("anagrafe.json", "w") as json_file:
        json.dump({}, json_file)
        
def login_interno(user: dict):
    with open('utenti.json') as json_file:
        users = json.load(json_file)
    for key, value in user.items():
        if key in users:
            if users[key][0] == value[0]:
                return True
    return False

def controllo_privilegi_admin(user: dict):
    with open('utenti.json') as json_file:
        users = json.load(json_file)    
    for key, value in user.items():
        if key in users:
            if value[0] == users[key][0]:
                if users[key][1] == 1:
                    return True
    return False

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if login_interno(accesso) and controllo_privilegi_admin(accesso):
            with open("anagrafe.json") as json_file:
                cittadini = json.load(json_file)
            for key, vale in dati.items():
                if key in cittadini:
                    print("Errore codice fiscale già esistente")
                    return "True"
            with open("anagrafe.json", "w") as json_file:
                cittadini |= dati
                json.dump(cittadini, json_file)
            return "True"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
    
@api.route('/read_cittadino', methods=['POST'])
def GestisciReadCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if login_interno(accesso):
            with open("anagrafe.json") as json_file:
                cittadini = json.load(json_file)
            for key, value in cittadini.items():
                if dati == key:
                    return cittadini[key]
            return "Cittadino non trovato"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
@api.route('/update_cittadino', methods=['POST'])
def GestisciUpdateCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if login_interno(accesso) and controllo_privilegi_admin(accesso):
            with open("anagrafe.json") as json_file:
                cittadini = json.load(json_file)
        
            if dati[0] not in cittadini:
                return "Errore, codice fiscale non trovato"

            for i in range(len(dati) - 1):
                if dati[i+1]:
                    if i + 1 == 1:
                        cittadini[dati[0]]["cognome"] = dati[i+1]
                    elif i + 1 == 2:
                        cittadini[dati[0]]["dataNascita"] = dati[i+1]
                    elif i + 1 == 3:
                        cittadini[dati[0]]["nome"] = dati[i+1]
            with open("anagrafe.json", "w") as json_file:
                json.dump(cittadini, json_file)
            return "Modifica avvenuta con successo"   
        else:
            return "Dati errati"     
    else:
        return 'Content-Type not supported!'

@api.route('/delete_cittadino', methods=['POST'])
def GestisciDeleteCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        accesso = request.json[1]
        dati = request.json[0]
        if login_interno(accesso) and controllo_privilegi_admin(accesso):
            with open("anagrafe.json") as json_file:
                cittadini = json.load(json_file)
        
            if dati not in cittadini:
                return "Errore, codice fiscale non trovato"
            cittadini.pop(dati)
            with open("anagrafe.json", "w") as json_file:
                json.dump(cittadini, json_file)
                
            return "Eliminazione avvenuta con successo"
        else:
            return "Dati errati"
    else:
        return 'Content-Type not supported!'
    
@api.route('/login', methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        with open('utenti.json') as json_file:
            user = json.load(json_file)
        for key, value in request.json.items():
            if key in user:
                if user[key][0] == value[0]:
                    return "True"
        return "Nome utente o password non trovati"
    else:
        return 'Content-Type not supported!'

@api.route('/registrazione', methods=['POST'])
def Registrazione():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        #verificare se username è nella tabella utenti 
        #altrimenti facciamo la insert
        with open('utenti.json') as json_file:
            user = json.load(json_file)        
        for key, value in request.json.items():
            if key not in user:
                request.json[key].append(random.randint(0,1))
                user |= request.json  #|= appende un nuovo elemento al dizionario
                with open('utenti.json', 'w') as json_file:
                    json.dump(user, json_file)
            else:
                return "Nome utente già in uso"
        return "Registrazione avvenuta con successo"
    else:
        return 'Content-Type not supported!'

api.run(host="127.0.0.1", port=8080, ssl_context='adhoc')
