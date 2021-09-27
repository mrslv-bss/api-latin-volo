from requests import *
import logging
from schemas import validate
import json


class API_Request(object):

    def __init__(self, apiurl, JSONmain):
        self.apiurl = apiurl
        self.JSONmain = JSONmain

    def request(self):
        response = post(self.apiurl, self.JSONmain)  # POST Request
        response_native = json.loads(response.text)  # Response as JSON
        # Validation
        Response_Validate = []
        Response_Validate.append(dict(response_native))
        if validate(Response_Validate) is True:
            logging.info("Validation status: SUCCESS")
        else:
            logging.error("Validation status: ERROR")
        logging.info("Response code: "+str(response.status_code))
        logging.info(response.text)
