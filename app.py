from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! apps running in port 80 on jenkins server'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 