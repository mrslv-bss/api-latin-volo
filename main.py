import re
import subprocess
import os
import json
from marshmallow import Schema, fields, ValidationError, validate, INCLUDE


# Config File
if os.environ.get('HOME_CONFIGFILE') is None:
    print("WARNING | Configuration file-variable is missing") 
    if os.name == 'nt':  # Windows
        exp = 'setx HOME_CONFIGFILE "{}\configuration.json"'.format(os.getcwd())
        subprocess.Popen(exp, shell=True).wait()
        print("WARNING | New configuration.json variable created. Restart script")
else:
    print("Configuration file variable successfully finded: "+os.environ.get('HOME_CONFIGFILE'))

# Input File
if os.environ.get('HOME_INPUTFILE') is None:
    print("WARNING | Input file-variable is missing") 
    print("Enter your input file name (Example - data.txt):")
    INPUTFILE = input("> ")
    if os.name == 'nt':  # Windows
        exp = 'setx HOME_INPUTFILE "{}\{}"'.format(os.getcwd(), INPUTFILE)
        subprocess.Popen(exp, shell=True).wait()
        print("WARNING | New input variable({}) created. Restart script".format(INPUTFILE))
else:
    print("Input file variable successfully finded: "+os.environ.get('HOME_INPUTFILE'))
    
# Read configuration.json
with open(os.environ.get('HOME_CONFIGFILE')) as f:
    data = json.load(f)
print(data['config'][0]['url'])
print(data['config'][0]['log'])


###


class JSONSchema(Schema):
    userid = fields.Integer(required=True,validate=validate.Range(min=1,max=10))
    title = fields.String(required=True)
    body = fields.String(required=True)
    ID = fields.String(validate=validate.Range(min=1,max=100))
    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE


user_data = [
    {"userid": "10", "title": "Mick", "body": "adsads"},
    {"userid": "10", "title": "Mick", "body": "adsads"},
    {"userid": "102", "title": "Mick", "body": "adsads"},
    {"userid": "1", "title": "Mick", "body": "adsads", "hey": "asd"},
]

if __name__ == "__main__":
    try:
        JSONSchema(many=True).load(user_data)
    except ValidationError as err:
        print(err.messages)