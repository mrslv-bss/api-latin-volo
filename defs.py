import subprocess
import os


def env_check(inputarg):
    # Config File
    if os.environ.get('HOME_CONFIGFILE') is None:
        print("WARNING | Configuration file-variable is missing")
        CONFIGFILE = "configuration.json"
        if os.name == 'nt':  # Windows
            e = r'setx HOME_CONFIGFILE "{}\{}"'.format(os.getcwd(), CONFIGFILE)
            subprocess.Popen(e, shell=True).wait()
            print("New configuration.json var created. Please, restart me")
    else:
        print("Configuration file variable successfully finded: ")
        print(os.environ.get('HOME_CONFIGFILE'))

# Input File
    if os.environ.get('HOME_INPUTFILE') is None:
        print("WARNING | Input file-variable is missing")
        # If run argument isn't empty
        if inputarg != "":
            INPUTFILE = inputarg
        else: # If run argument is empty
            print("Enter your input file name (Example - data.txt):")
            INPUTFILE = input("> ")
        if os.name == 'nt':  # Windows / Enter data to env
            e = 'setx HOME_INPUTFILE "{}\\{}"'.format(os.getcwd(), INPUTFILE)
            subprocess.Popen(e, shell=True).wait()
            print("New input variable {} created.".format(INPUTFILE))
            print("Terminate script? Y/N")
            terminate = input("> ").upper()
            if terminate == 'Y':
                quit()
            elif terminate == 'N':
                print("Environment var changes will take effect after reload")
            else:
                print("Incorrect input, terminate script :)")
                quit()
    else:
        print("Input file variable successfully finded: ")
        print(os.environ.get('HOME_INPUTFILE'))