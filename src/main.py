import os
import json
import requests
from marshmallow import Schema, fields, ValidationError, validate, INCLUDE
from defs import env_check
import argparse
import logging


# Logging config
logging.basicConfig(format = '%(asctime)s %(levelname)s %(message)s',
                    datefmt = '%m/%d/%Y %I:%M:%S',
                    filename = 'app.log',
                    filemode='w',
                    level=logging.DEBUG)

# cmd: 'python main.py -p data.txt'
parser = argparse.ArgumentParser(description='Get input file name.format')
parser.add_argument("-p", "--print_string", help="Enter your input file name (Example - data.txt)")
args = parser.parse_args()

# If argument is present
if args.print_string is not None:
    env_check(args.print_string)

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
# try:
#     JSONSchema(many=True).load(user_data)
# except ValidationError as err:
#     print(err.messages)
    ###


if __name__ == "__main__":
    # If run argument is empty
    if args.print_string is None:
        env_check("")
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

    # Step 1 - Using completed input data, make a request to URL
    response = requests.get(data['config'][0]['url']) # request by url
    queryURL = data['config'][0]['url'] + f"?userId={user_data[0]['userid']}&title={user_data[0]['title']}" # Search by 'userid' and 'title'
    response = requests.get(queryURL) # second request by modified url
    # print(response.text)