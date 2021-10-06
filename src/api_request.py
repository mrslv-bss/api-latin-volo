from requests import *
import logging
from schemas import validate
import json


class API_Request(object):

    def __init__(self, api_url, JSON_main):
        self.api_url = api_url
        self.JSON_main = JSON_main

    def request(self):
        response = post(self.api_url, self.JSON_main)
        response_native = json.loads(response.text)  # Response as JSON
        # Validation
        Response_Validate = []
        Response_Validate.append(dict(response_native))
        if validate(Response_Validate):
            logging.info("Validation status: SUCCESS")
        else:
            logging.error("Validation status: ERROR")
        logging.info("Response code: "+str(response.status_code))
        logging.info(response.text)
