from flask import Flask
from flask_cors import CORS
import logging

#####################
import psycopg2
import json

# pg_host = 'localhost'
# pg_dbname = 'postgres'
# pg_user = 'postgres'
# pg_password = 'mysecretpassword'
# conn = psycopg2.connect("host=" + pg_host + " user=" + pg_user +" dbname=" + pg_dbname +" password=" + pg_password)

#conn.close()
#####################

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    print('hello_world start ...')
    return "im woring on docker container.(python Flask.2)"

@app.route("/hello")
def hello_hello():
    return "<p>Hello, Hello</p>"

@app.route("/tasks")
def tasks():
    # cur = conn.cursor()
    # cur.execute('SELECT id, name FROM tasks;')
    # results = cur.fetchall()
    # print(results)
    # print(type(results))  
    # mydata = json.dumps(results)
    # cur.close()
    return "mydata"

if __name__ == "__main__":
    app.run(host="0.0.0.0")