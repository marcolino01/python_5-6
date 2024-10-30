
import requests, json, sys
import subprocess
#from generativeIA.myjson import ComponiJsonPerImmagine
from myjson import *

base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key="
google_api = "AIzaSyBOkpczrudqDXMQd1En6RpaI15EJ6PCAmM"
api_url = base_url+google_api

def ComponiJsonPerImmagine(sImagePath):
  subprocess.run(["rm", "./image.jpg"])
  subprocess.run(["rm", "./request.json"])
  subprocess.run(["cp", sImagePath,"./image.jpg"])
  subprocess.run(["bash", "./creajson.sh"])

print("Benvenuti al Comune - sede locale")

iFlag = 0
while iFlag==0:
    print("\nOperazioni disponibili:")
    print("1. Inserisci una domanda")
    print("2. Richiedi una domanda su un'immagine")
    print("3. Esci")

    try:
        iOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue


    if iOper == 1:
        sDomanda = input("Inserisci domanda: ")
        jsonDataRequest = {"contents": [{"parts":[{"text":sDomanda}]}]}
        response = requests.post(api_url, json=jsonDataRequest)
        if response.status_code == 200:
            print(response.json())
            lListaRisposte = response.json()["candidates"]
            for dRisposta in lListaRisposte:
                sTestoRisposta = dRisposta["content"]["parts"][0]["text"]
                print(sTestoRisposta)
    # Richiesta dati cittadino
    elif iOper == 2:
        sImage = input ("Inserisci file img da analizzare:")
        sDomanda = input("Inserisci la domanda ")
        ComponiJsonPerImmagine(sImage)
        jsonDataRequest = JsonDeserialize("request.json")
        response = requests.post(api_url, json=jsonDataRequest)
        if response.status_code == 200:
            print(response.json())
            lRisposte = response.json()['candidates']
            for risposta in lRisposte:
                sTestoRisposta = risposta["content"]["parts"][0]["text"]
                print(sTestoRisposta)


    elif iOper == 3:
        print("Buona giornata!")
        iFlag = 1

    else:
        print("Operazione non disponibile, riprova.")

