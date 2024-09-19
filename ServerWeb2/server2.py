from flask import Flask, render_template, request

api = Flask("__name__")


utenti = [["Mario","Rossi"],
          ["Gianni","Bismark"],
          ["Anita","Garibaldi"]]


@api.route('/', methods=['GET'])
def ciao():
    return render_template('index.html')


@api.route('/index2', methods = ['GET'])
def get_code():
    nome = request.args.get("fname")
    cognome = request.args.get("lname")
    for utente in utenti:
        if utente[0].lower()== nome.lower() and utente[1].lower() ==cognome.lower():
            return render_template('index2.html', nome = nome, cognome = cognome)
    return render_template('index3.html')




api.run(host="0.0.0.0", port=8085)