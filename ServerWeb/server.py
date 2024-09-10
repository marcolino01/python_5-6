from flask import Flask, render_template

api = Flask("__name__")


@api.route('/abc', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/ciao', methods=['GET'])
def ciao():
    return render_template('index2.html')



api.run(host="0.0.0.0", port=8085)