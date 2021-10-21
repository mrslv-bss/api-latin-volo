import subprocess
import os
import re


def env_check(input_arg, env_name_config, env_name_input):
    # Environment variable is missing
    if (os.environ.get(env_name_config) is None or
            os.environ.get(env_name_input) is None):
        print("Neccessary file-variable is missing")
        CONFIGFILE = "configuration.json"

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
            config_save = r'setx {} "{}\{}"'.format(env_name_config,
                                                    os.getcwd(),
                                                    CONFIGFILE)
            subprocess.Popen(config_save, shell=True).wait()
            input_save = 'setx {} "{}\\{}"'.format(env_name_input,
                                                   os.getcwd(),
                                                   INPUTFILE)
            subprocess.Popen(input_save, shell=True).wait()
            print("Success, changes will take effect after restart")
            print("Terminate Script")
            quit()
    else:  # Environment variable is present
        print("Neccessary environment variables successfully found: ")
        print(os.environ.get(env_name_config))
        print(os.environ.get(env_name_input))

def args_check(arg_string):
    # If run argument is present
    if arg_string is not None:
        format_check = re.search(r"\.txt$|\.log$|.html$", arg_string)
        if format_check is None:
            print("Incorrect file type, available: .txt, .log, .html")
            print("Terminate Script")
            quit()
        env_check(arg_string, "HOME_CONFIGFILE", "HOME_INPUTFILE")
    # Elif run argument is empty
    elif arg_string is None:
        env_check("", "HOME_CONFIGFILE", "HOME_INPUTFILE")

    if os.path.isfile(os.environ.get('HOME_CONFIGFILE')) is False:
        print("Missing config file in your directory")
        print("Terminate Script")
        quit()
