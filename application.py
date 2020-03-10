from flask import Flask
import sys
from flask import request, jsonify
import coronaAccess
import newsAccess


application = Flask(__name__)
application.config["DEBUG"] = True


@application.route("/hello")
def hello():
    return "Hello goorm!"

@application.route('/', methods=['GET'])
def getStats():
    return jsonify(coronaAccess.load())

@application.route('/news', methods=['GET'])
def getNews():
    return jsonify(newsAccess.spider())

    
    
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80)
