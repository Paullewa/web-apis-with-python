import re
from flask import Flask, jsonify,request


# Intitialise the app
app = Flask(__name__)

# Define what the app does

@app.route("/greet",methods=['GET'] )
def index():
    fname = request.args.get('fname')
    lname = request.args.get("lname")
    if not fname and not lname:
        return jsonify({ "status" : "error" })
    elif lname and not fname:
        
        return jsonify({"data":f" Hello Mr {lname}!"})
    elif  not lname and fname:
        return jsonify({'data':f'Hallo  {fname}'})
    else:
        return jsonify({'data':f'Is your name {fname} {lname}?'})
