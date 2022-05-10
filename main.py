from flask import Flask

app = Flask('__main__')

@app.route('/')
def index():
  return '<h1>Olá Mundo!</h1>'

@app.route('/unifran')
def uni():
  return '<h2>Universidade de Franca</h2>'

@app.route('/dashboard/<nome>')
def user(nome):
  return f'Olá, {nome}'

if __name__ == '__main__':
  app.run(host='0.0.0.0')