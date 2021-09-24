import re
import subprocess
import os
import json

# Config File
if os.environ.get('HOME_CONFIGFILE') is None:
    print("WARNING | Configuration file-variable is missing") 
    if os.name == 'nt':  # Windows
        exp = 'setx HOME_CONFIGFILE "{}\configuration.json"'.format(os.getcwd())
        subprocess.Popen(exp, shell=True).wait()
        print("WARNING | New configuration.json variable created. Restart script")
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
        print("WARNING | New input variable({}) created. Restart script".format(INPUTFILE))
else:
    print("Input file variable successfully finded: "+os.environ.get('HOME_INPUTFILE'))
    
# Read configuration.json
with open(os.environ.get('HOME_CONFIGFILE')) as f:
    data = json.load(f)
print(data['config'][0]['url'])
print(data['config'][0]['log'])