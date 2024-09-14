from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prever', methods=['POST'])
def prever():
    # Coletar os dados do formulário e rodar o modelo
    time_casa = request.form['time_casa']
    time_fora = request.form['time_fora']
    # Use seu modelo aqui para fazer a previsão
    return "Probabilidade de vitória: XX"

if __name__ == '__main__':
    app.run(debug=True)
