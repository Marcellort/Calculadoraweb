from flask import Flask
from calc import soma, subtracao, multiplicacao, divisao

app = Flask(__name__)


def exibir(resultado) -> str:
    return f'<h3> O resultado da operação é :{resultado}'


titulo = '<h1> Calculadora </h1> <a href = "/"> Voltar </a>'


@app.route('/')
def index() -> str:
    ol = '''
            <ol>
                <li><a href = "/somar">Somar</a></li>
                <li><a href = "/subtrair" >Subtrair</a></li>
                <li><a href = "/multiplicar" >Multiplicar</a></li>
                <li><a href = "/dividir" >Dividir</a></li>
            </ol>
                
        '''
    return f'{ol}'


@app.route('/somar')
def somar() -> str:
    number1 = 10.0
    number2 = 20.0
    resultado = soma(number1, number2)
    return f'{titulo} {exibir(resultado)}'


@app.route('/subtrair')
def subtrair() -> str:
    number1 = 10.0
    number2 = 20.0
    resultado = subtracao(number1, number2)
    return f'{titulo} {exibir(resultado)}'


@app.route('/multiplicar')
def multiplicar() -> str:
    number1 = 10.0
    number2 = 20.0
    resultado = multiplicacao(number1, number2)
    return f'{titulo} {exibir(resultado)}'


@app.route('/dividir')
def dividir() -> str:
    number1 = 10.0
    number2 = 20.0
    resultado = divisao(number1, number2)
    return f'{titulo} {exibir(resultado)}'


app.run(debug=True)
