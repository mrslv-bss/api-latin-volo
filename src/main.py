import os
import json
import re
import argparse
import logging
from defs import env_check
from schemas import validate
from api_request import APIRequest


parser = argparse.ArgumentParser(description='Get input file name.format')

help = "Enter your input file name (Example - data.txt)"
parser.add_argument("-p", "--print_string", help=help)
args = parser.parse_args()

# If run argument is present
if args.print_string is not None:
    format_check = re.search(r"\.txt$|\.log$|.html$", args.print_string)
    if format_check is None:
        print("Incorrect file type, available: .txt, .log, .html")
        print("Terminate Script")
        quit()
    env_check(args.print_string)


if __name__ == "__main__":
    # If run argument is empty
    if args.print_string is None:
        env_check("")

    if os.path.isfile(os.environ.get('HOME_CONFIGFILE')) is False:
        logging.error('Missing config file in your directory')
        logging.info('Terminate Script')
        print("Missing config file in your directory")
        print("Terminate Script")
        quit()

    # Step 1 - Read configuration.json
    with open(os.environ.get('HOME_CONFIGFILE')) as f:
        data = json.load(f)

    # Logging config
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S',
                        filename=data['config'][0]['log'],
                        filemode='w',
                        level=logging.DEBUG)

    # Step 2 - Read input data file and generate JSON format
    if os.path.isfile(os.environ.get('HOME_INPUTFILE')) is False:
        logging.error('Missing input file in your directory')
        logging.info('Terminate Script')
        print("Missing input file in your directory")
        print("Terminate Script")
        quit()

    with open(os.environ.get('HOME_INPUTFILE')) as f:
        letsdoit = f.readline()
        while letsdoit:
            letsdoit = f.readline()

            h = re.split("#", letsdoit)
            e = h[0]
            # Actual view: [131: Title    Body], [other]
            ll = re.sub(r"\s{4}|\t|:", "#", e)
            o = re.sub("#{1,5}", "#", ll)
            # Actual view: 131#Title#Body#
            wo = re.sub(" #", "#", o)
            r = re.sub("# ", "#", wo)
            ld = re.split("#", r)
            # Actual view: ['131', ' ', 'Title', 'Body']

            for remdel in ld:
                if remdel == " ":
                    ld.remove(remdel)
                elif remdel == "\n":
                    ld.remove(remdel)
                elif remdel == "":
                    ld.remove(remdel)
            # Actual view: ['131', 'Title', 'Body']
            if len(ld) <= 2:
                continue

            # Step 3 - Package into JSON format
            JSON_format = ['userid', 'title', 'body']
            JSON_Request = zip(JSON_format, ld)
            JSON_Validate = []
            JSON_Validate.append(dict(JSON_Request))

            # Step 4 - Validate our JSON
            if validate(JSON_Validate):
                logging.info("INPUT DATA: SUCCESS")
            else:
                logging.error("INPUT DATA: ERROR")

            # Step 5 - Using completed input data, make a request to URL
            # E501 line too long (80 > 79 characters)
            prerequest = APIRequest(data['config'][0]['url'], JSON_Validate[0])
            prerequest.request()
