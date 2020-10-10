from flask import Flask
from flask import request
import json
from LinkedList import LinkedList

app = Flask(__name__)

@app.route('/api/v1/auto-insert')
def auto_insert():
    ll = LinkedList()
    json_data = None
    with open("data.json") as dt_json:
        json_data = json.load(dt_json)
    
    for index, dt in enumerate(json_data['list']):
        ll.insert(dt)
        
    return ll.print_vals()

ll1 = LinkedList()
json_data = None

@app.route('/api/v1/insert', methods=['POST'])
def post_insert():
    data = json.loads(request.data.decode('utf-8'))
    ll1.insert(data['data'])
    return ll1.print_vals()

@app.route('/api/v1/get')
def get_ll():    
    return ll1.print_vals()