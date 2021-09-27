import subprocess
import os
import logging
import re

def env_check(inputarg):
    # Config File
    if os.environ.get('HOME_CONFIGFILE') is None:
        logging.warning('Configuration file-variable is missing')
        CONFIGFILE = "configuration.json"
        if os.name == 'nt':  # Windows
            e = r'setx HOME_CONFIGFILE "{}\{}"'.format(os.getcwd(), CONFIGFILE)
            subprocess.Popen(e, shell=True).wait()
            logging.info('New configuration.json var created. Please, restart me')
    else:
        logging.info('Configuration file variable successfully finded: ')
        logging.info(os.environ.get('HOME_CONFIGFILE'))

# Input File
    if os.environ.get('HOME_INPUTFILE') is None:
        logging.warning('Input file-variable is missing')
        # If run argument isn't empty
        if inputarg != "":
            INPUTFILE = inputarg
        else: # If run argument is empty
            print("Enter your input file name (Example - data.txt):")
            INPUTFILE = input("> ")
            formatcheck = re.search("\.txt$|\.log$|.html$", INPUTFILE)
            if formatcheck is None:
                logging.error('Incorrect file type, available: .txt, .log, .html')
                logging.info('Terminate Script')
                print("Incorrect file type, available: .txt, .log, .html")
                print("Terminate Script")
                quit()
        if os.name == 'nt':  # Windows / Enter data to env
            e = 'setx HOME_INPUTFILE "{}\\{}"'.format(os.getcwd(), INPUTFILE)
            subprocess.Popen(e, shell=True).wait()
            logging.info("New input variable {} created.".format(INPUTFILE))
            print("Terminate script? Y/N")
            terminate = input("> ").upper()
            if terminate == 'Y':
                logging.info('Terminate Script')
                quit()
            elif terminate == 'N':
                print("Environment var changes will take effect after reload")
            else:
                print("Incorrect input, terminate script :)")
                logging.info('Terminate Script')
                quit()
    else:
        logging.info('Input file variable successfully finded: ')
        logging.info(os.environ.get('HOME_INPUTFILE'))