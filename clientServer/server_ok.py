from flask import Flask,json,request
from myjson import *

api=Flask(name)
pAnagrafe="anagrafe.json"
pUtenti="utenti.json"
cittadini=JsonDeserialize(pAnagrafe)
utenti=JsonDeserialize(pUtenti)

@api.route('/add_cittadino',methods=['POST'])
def GestisciAddCittadino():
    username=request.json["login"]["username"]
    password=request.json["login"]["password"]
    if Login(username,password)==True:
        dati = request.json["dati"]
        for c in cittadini.keys():
            if dati["codice fiscale"] ==c:
                jsonResp = {"Esito":"400", "Msg":"cittadino gia presente"}
                return json.dumps(jsonResp)
        cittadini.update({dati["codice fiscale"]:dati})
        JsonSerialize(cittadini,pAnagrafe)
        jsonResp = {"Esito":"200", "Msg":"cittadino aggiunto"}
        return json.dumps(jsonResp)
    else:
        jsonResp = {"Esito":"400", "Msg":"diritti negati"}
        return json.dumps(jsonResp)

@api.route('/read_cittadino',methods=['POST'])
def GestisciReadCittadino():
    username=request.json["login"]["username"]
    password=request.json["login"]["password"]
    if Login(username,password)==True:
        cod=request.json["codF"]
        for c in cittadini:
            if cod==c:
                jsonResp = {"Esito":"200", "Msg":"ok","Dati cittadino":cittadini[c]}
                return json.dumps(jsonResp)
        jsonResp = {"Esito":"400", "Msg":"cittadino non presente"}
        return json.dumps(jsonResp)
    else:
        jsonResp = {"Esito":"400", "Msg":"diritti negati"}
        return json.dumps(jsonResp)

@api.route('/update_cittadino',methods=['POST'])
def GestisciUpdateCittadino():
    username=request.json["login"]["username"]
    password=request.json["login"]["password"]
    if Login(username,password)==True:
        dati=request.json["dati"]
        for c in cittadini.keys():
            if dati["codice fiscale"] ==c:
                cittadini[c]=dati
                jsonResp = {"Esito":"200", "Msg":"dati cittadino aggiornati"}
                JsonSerialize(cittadini,pAnagrafe)
        jsonResp = {"Esito":"400", "Msg":"cittadino non presente"}
        return json.dumps(jsonResp)
    else:
        jsonResp = {"Esito":"400", "Msg":"diritti negati"}
        return json.dumps(jsonResp)

@api.route('/delete_cittadino',methods=['POST'])
def GestisciDeleteCittadino():
    username=request.json["login"]["username"]
    password=request.json["login"]["password"]
    if Login(username,password)==True:
        cod=request.json["codF"]
        for c in cittadini:
            if cod==c:
                del cittadini[cod]
                jsonResp = {"Esito":"200", "Msg":"cittadino rimosso"}
                JsonSerialize(cittadini,pAnagrafe)
                return json.dumps(jsonResp)
        jsonResp = {"Esito":"400", "Msg":"cittadino non presente"}
        return json.dumps(jsonResp)
    else:
        jsonResp = {"Esito":"400", "Msg":"diritti negati"}
        return json.dumps(jsonResp)

@api.route('/login',methods=['POST'])
def GestisciLogin():
    utente=request.json  
    for u in utenti:
        if list(utente.keys())[0]==u:
            if list(utente.values())[0]==utenti[u]["password"]:
                if utenti[u]["privilegio"]=="r":
                    jsonResp = {"Esito":"200", "Msg":"login eseguito con successo", "login":True,"privilegio":"r"}
                    return json.dumps(jsonResp)
                elif utenti[u]["privilegio"]=="w":
                    jsonResp = {"Esito":"200", "Msg":"login eseguito con successo", "login":True,"privilegio":"w"}
                    return json.dumps(jsonResp)
            else:
                jsonResp = {"Esito":"401", "Msg":"username o password errati", "login":False}
                return json.dumps(jsonResp)
    jsonResp = {"Esito":"402", "Msg":"username o password errati", "login":False}
    return json.dumps(jsonResp)

def Login(utente,password):
    if utente in utenti:
        if password==utenti[utente]["password"]:
            return True
        else:
            return False
    else:
        return False
       
           


api.run(host="127.0.0.1", port=8080,ssl_context='adhoc')
