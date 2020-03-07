from flask import Flask
import sys
from flask import request, jsonify
import webAccess

application = Flask(__name__)
application.config["DEBUG"] = True
@application.route("/hello")
def hello():
    return "Hello goorm!"

@application.route('/', methods=['GET', 'POST'])
def getStats():
    return jsonify(webAccess.load())
    
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80)