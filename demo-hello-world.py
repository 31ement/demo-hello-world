#!/usr/bin/python36

from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    return '''
	Hello, world from {}
	'''.format(socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0')
