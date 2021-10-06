import subprocess
import os
import re


def env_check(input_arg):
    # Config File
    if os.environ.get('HOME_CONFIGFILE') is None:
        print("Configuration file-variable is missing")
        CONFIGFILE = "configuration.json"
        if os.name == 'nt':  # Windows / Enter data to env
            e = r'setx HOME_CONFIGFILE "{}\{}"'.format(os.getcwd(), CONFIGFILE)
            subprocess.Popen(e, shell=True).wait()
            print("New configuration.json var created. Please, restart me")
    else:
        print("Configuration file variable successfully found: ")
        print(os.environ.get('HOME_CONFIGFILE'))

# Input File
    if os.environ.get('HOME_INPUTFILE') is None:
        print("Input file-variable is missing")
        if input_arg != "":  # If run argument isn't empty
            INPUTFILE = input_arg
        else:  # If run argument is empty
            print("Enter your input file name (Example - data.txt):")
            INPUTFILE = input("> ")
            format_check = re.search(r"\.txt$|\.log$|.html$", INPUTFILE)
            if format_check is None:
                print("Incorrect file type, available: .txt, .log, .html")
                print("Terminate Script")
                quit()
        if os.name == 'nt':  # Windows / Enter data to env
            e = 'setx HOME_INPUTFILE "{}\\{}"'.format(os.getcwd(), INPUTFILE)
            subprocess.Popen(e, shell=True).wait()
            print("New input variable {} created.".format(INPUTFILE))
            print("Terminate script? Y/N")
            terminate = input("> ").upper()
            if terminate == 'Y':
                print("Terminate Script")
                quit()
            elif terminate == 'N':
                print("Environment var changes will take effect after reload")
            else:
                print("Incorrect input, terminate script :)")
                print("Terminate Script")
                quit()
    else:
        print("Input file variable successfully found: ")
        print(os.environ.get('HOME_INPUTFILE'))
