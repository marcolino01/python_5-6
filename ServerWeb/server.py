from flask import Flask, render_template, request

api = Flask("__name__")

@api.route('/ciao', methods=['GET'])
def ciao():
    return render_template('index2.html')

@api.route('/abc', methods=['GET'])
def secondoindex():
    nome = request.args.get("fname")
    cognome = request.args.get("lname")
    return render_template('index.html', nome = nome, cognome = cognome)

api.run(host="0.0.0.0", port=8085)