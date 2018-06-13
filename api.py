
import flask
import simplejson
import contacts
import config

from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# CONNECT SQL SERVER
server = config.DATABASE_CONFIG['server']
database = config.DATABASE_CONFIG['database']
username = config.DATABASE_CONFIG['username']
password = config.DATABASE_CONFIG['password']


@app.route('/', methods=['GET'])
def home():
    contact_lst = contacts.list_contacts(server, database, username, password)
    return simplejson.dumps(contact_lst)


@app.route('/contacts', methods=['GET'])
def api_contact():
    if 'name' in request.args:
        contact_lst = contacts.find_contact(server, database, username, password, request.args['name'])
    else:
        contact_lst = contacts.list_contacts(server, database, username, password)
    return simplejson.dumps(contact_lst)


@app.route('/hello', methods=['GET'])
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'


app.run()