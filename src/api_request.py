from requests import *
import logging
from schemas import validate
import json

class API_Request(object):
    
    def __init__(self, apiurl, JSONmain):
        self.apiurl = apiurl
        # self.JSONuserid = JSONuserid
        # self.JSONtitle = JSONtitle
        self.JSONmain = JSONmain
        
    def request(self):
        # print(self.input)
        # response = get(self.input) # request by url
        # queryURL = self.input + f"?userId={self.JSONuserid}&title={self.JSONtitle}" # Search by 'userid' and 'title'
        response = post(self.apiurl,self.JSONmain) # second request by modified url
        # print(queryURL)
        # print(response.text)
        response_native = json.loads(response.text)
        # print(response_native)
        Response_Validate = []
        Response_Validate.append(dict(response_native))
        validate(Response_Validate)
        # data = {}
        # data['people'] = []
        # data['people'].append(response.text)
        # print(data['people'])

        logging.info("Response code: "+str(response.status_code))
        logging.info(response.text)
