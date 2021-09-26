from requests import *
import json

class API_Request(object):
    
    def __init__(self, input, JSONuserid, JSONtitle, JSONmain):
        self.input = input
        self.JSONuserid = JSONuserid
        self.JSONtitle = JSONtitle
        self.JSONmain = JSONmain
        
    def request(self):
        # print(self.input)
        response = get(self.input) # request by url
        queryURL = self.input + f"?userId={self.JSONuserid}&title={self.JSONtitle}" # Search by 'userid' and 'title'
        response = post(self.input,self.JSONmain) # second request by modified url
        # print(queryURL)
        print(response.text)