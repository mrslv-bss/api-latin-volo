import os
import json
import re
import argparse
import logging
from defs import env_check
from schemas import validate
from api_request import API_Request

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
    formatcheck = re.search("\.txt|\.log|.html", args.print_string)
    if formatcheck is None:
        logging.error('Incorrect file type, available: .txt, .log, .html')
        logging.info('Terminate Script')
        print("Incorrect file type, available: .txt, .log, .html")
        print("Terminate Script")
        quit()
    env_check(args.print_string)


if __name__ == "__main__":
    # If run argument is empty
    if args.print_string is None:
        env_check("")

    # Step 1 - Read configuration.json
    with open(os.environ.get('HOME_CONFIGFILE')) as f:
        data = json.load(f)

    # Step 2 - Read input data file and generate JSON format
    with open(os.environ.get('HOME_INPUTFILE')) as f:
        letsdoit = f.readline()
        while letsdoit:
            letsdoit = f.readline()
            
            h = re.split("#",letsdoit)
            e = h[0]
            # Actual view: [131: Title    Body], [other]
            ll = re.sub("\s{4}|\t|:", "#", e)
            o = re.sub("#{1,5}", "#", ll)
            # Actual view: 131#Title#Body#
            
            wo = re.sub(" #", "#", o)
            r = re.sub("# ", "#", wo)
            l = re.split("#",r)
            # Actual view: ['131', ' ', 'Title', 'Body']
            for d in l:
                if d == " ":
                    l.remove(d)
                elif d == "\n":
                    l.remove(d)
                elif d == "":
                    l.remove(d)
            # Actual view: ['131', 'Title', 'Body']
            
            if len(l) <= 2:
                continue
            # print(l)
            
            # Step 3 - Package into JSON format
            JSON_format = ['userid','title','body']
            JSON_Request = zip(JSON_format,l)
            JSON_Validate = []
            JSON_Validate.append(dict(JSON_Request))
            # Step 4 - Validate our JSON
            validate(JSON_Validate)
            # print("TEST:")
            # print(JSON_Validate[0])
            # Step 5 - Using completed input data, make a request to URL
            prerequest = API_Request(data['config'][0]['url'],JSON_Validate[0])
            prerequest.request()

    # Step 3 - Using completed input data, make a request to URL
    # response = requests.get(data['config'][0]['url']) # request by url
    # queryURL = data['config'][0]['url'] + f"?userId={user_data[0]['userid']}&title={user_data[0]['title']}" # Search by 'userid' and 'title'
    # response = requests.get(queryURL) # second request by modified url
    # print(response.text)