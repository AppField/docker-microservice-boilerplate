from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Dockerino'

@app.route('/resource')
def hello_docker():
    return 'Hello resource'

if __name__ == '__main__':
    app.run(host='0.0.0.0')