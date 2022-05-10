from flask import Flask, render_template

app = Flask('__main__')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/unifran')
def uni():
  return render_template('unifran.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0')