from requests import *
import logging

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
        # print(response.status_code)
        logging.info("Response code: "+str(response.status_code))
        logging.info(response.text)
