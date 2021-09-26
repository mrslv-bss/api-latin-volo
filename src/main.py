import os
import json
import re
import requests
from defs import env_check
import argparse
import logging
from schemas import JSONSchema,validate

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


if __name__ == "__main__":
    # If run argument is empty
    if args.print_string is None:
        env_check("")
    # Step 1 - Read configuration.json
    with open(os.environ.get('HOME_CONFIGFILE')) as f:
        data = json.load(f)
    print(data['config'][0]['url'])
    print(data['config'][0]['log'])

    # Step 2 - Read input data file and generate JSON format
    # user_data = [
    #     {"userid": "11", "title": "qui est esse", "body": "adsads"},
    #     {"userid": "5", "title": "Mick", "body": "adsads"},
    #     {"userid": "5", "title": "Mick", "body": "adsads"},
    #     {"userid": "1", "title": "Mick", "body": "adsads"},
    # ]
    # print(user_data)
    with open(os.environ.get('HOME_INPUTFILE')) as f:
        letsdoit = f.readline()
        while letsdoit:
            letsdoit = f.readline()
            
            h = re.split("#",letsdoit)
            e = h[0]
            # [131: Title    Body], [other]
            
            ll = re.sub("\s{4}|\t|:", "#", e)
            o = re.sub("#{1,5}", "#", ll)
            # 131#Title#Body#
            
            w = re.split("#",o)
            # ['131', ' ', 'Title', 'Body']
        
            for orld in w:
                if orld == " ":
                    w.remove(orld)
                elif orld == "\n":
                    w.remove(orld)
                elif orld == "":
                    w.remove(orld)
            # ['131', 'Title', 'Body']
            
            if len(w) <= 2:
                continue
            
            JSON_format = ['userid','title','body']
            JSON_Request = zip(JSON_format,w)
            JSON_Validate = []
            JSON_Validate.append(dict(JSON_Request))
            validate(JSON_Validate)

    # Step 3 - Using completed input data, make a request to URL
    # response = requests.get(data['config'][0]['url']) # request by url
    # queryURL = data['config'][0]['url'] + f"?userId={user_data[0]['userid']}&title={user_data[0]['title']}" # Search by 'userid' and 'title'
    # response = requests.get(queryURL) # second request by modified url
    # print(response.text)