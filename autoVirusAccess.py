import coronaAccess
import time
from flask import jsonify
import os
import json

os.chdir("/workspace/Canada_COVID19/")
os.system("python application.py &")

def loading():
    print("LOADING FUNC")
    #with open('backup.json', 'w') as outfile:
    #    with open('data.json', 'r') as json_file:
    #        json.dump(json_file, outfile)
    with open('data.json', 'w') as outfile:
        json.dump(coronaAccess.load(), outfile)


while True:
    loading()
    time.sleep(600)


