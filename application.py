from flask import Flask
import sys
from flask import request, jsonify
import coronaAccess
import newsAccess
import json

application = Flask(__name__)
application.config["DEBUG"] = True


@application.route("/hello")
def hello():
    return "Hello goorm!"

@application.route('/', methods=['GET'])
def getStats():
    with open('data.json') as json_file:
        data = json.load(json_file)
        #if data == "":
        #    with open('backup.json') as backup:
       #         data = json.load(backup)
        return jsonify(data)


@application.route('/news', methods=['GET'])
def getNews():
    return jsonify(newsAccess.spider())

    
    
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80)
