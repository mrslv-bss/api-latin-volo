import subprocess
import os
import json
import requests
from marshmallow import Schema, fields, ValidationError, validate, INCLUDE


# Config File
if os.environ.get('HOME_CONFIGFILE') is None:
    print("WARNING | Configuration file-variable is missing") 
    if os.name == 'nt':  # Windows
        exp = 'setx HOME_CONFIGFILE "{}\configuration.json"'.format(os.getcwd())
        subprocess.Popen(exp, shell=True).wait()
        print("WARNING | New configuration.json variable created. Please, restart script!")
        print("Terminate script? Y/N")
        terminate = input("> ").upper()
        if terminate == 'Y':
            quit()
        elif terminate == 'N':
            print("Environment variables changes will take effect after reload.")
        else:
            print("Incorrect input, terminate script :)")
            quit()
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
        print("WARNING | New input variable({}) created. Please, restart script!".format(INPUTFILE))
        print("Terminate script? Y/N")
        terminate = input("> ").upper()
        if terminate == 'Y':
            quit()
        elif terminate == 'N':
            print("Environment variables changes will take effect after reload.")
        else:
            print("Incorrect input, terminate script :)")
            quit()
else:
    print("Input file variable successfully finded: "+os.environ.get('HOME_INPUTFILE'))
    
# Read configuration.json
with open(os.environ.get('HOME_CONFIGFILE')) as f:
    data = json.load(f)
print(data['config'][0]['url'])
print(data['config'][0]['log'])


# Read input data file and generate JSON format
user_data = [
    {"userid": "1", "title": "qui est esse", "body": "adsads"},
    {"userid": "5", "title": "Mick", "body": "adsads"},
    {"userid": "5", "title": "Mick", "body": "adsads"},
    {"userid": "1", "title": "Mick", "body": "adsads"},
]
with open(os.environ.get('HOME_INPUTFILE')) as f:
    line = f.readline()
    while line:
        line = f.readline()
        print(line)
    ###

# Creating schemas
class JSONSchema(Schema):
    userid = fields.Integer(required=True,validate=validate.Range(min=1,max=10))
    title = fields.String(required=True)
    body = fields.String(required=True)
    ID = fields.String(validate=validate.Range(min=1,max=100))
    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE

# Validate by marshmallow our JSON
try:
    JSONSchema(many=True).load(user_data)
except ValidationError as err:
    print(err.messages)
    ###


if __name__ == "__main__":
    # Step 1 - Using completed input data, make a request to URL
    response = requests.get(data['config'][0]['url']) # request by url
    queryURL = data['config'][0]['url'] + f"?userId={user_data[0]['userid']}&title={user_data[0]['title']}" # Search by 'userid' and 'title'
    response = requests.get(queryURL) # second request by modified url
    # print(response.text)