# API EXAM VOLO
### JSONPlaceholder https://jsonplaceholder.typicode.com/posts

![Image alt](https://img.shields.io/badge/pycodestyle-✔-green)
# Installation 🐍

###### Precondition

>

	# configuration.json
    "config": [
		{
			"url": "https://jsonplaceholder.typicode.com/posts",
			"log": "out.log"
		}
	]
    
>

###### Step 1
      python src/main.py -p data.txt 
      # You directly specify the name of the input file

      python src/main.py 
      # You will need to enter the name of the input file in the console

>      Restart your CMD for environment variables changes to take effect

###### Step 2
    > python src/main.py
    Output:
    Neccessary environment variables successfully found: 
    {dir}\api-latin-volo\configuration.json
    {dir}\api-latin-volo\input.txt
###### Explanations for the log file
	# 09/27/2021 02:26:24 INFO INPUT DATA: SUCCESS
	if validate(JSON_Validate) is True:
            logging.info("INPUT DATA: SUCCESS")
        else:
            logging.error("INPUT DATA: ERROR")
	    
	# 09/27/2021 02:26:24 INFO Response code: 201
	logging.info("Response code: "+str(response.status_code))
	
	""" 09/27/2021 02:26:24 INFO {
  		"userid": "95",
  		"title": "Title example",
  		"body": "Body ",
  		"id": 101
	} """
	logging.info(response.text)
<hr>

### Input line format
    <user_id><split_character><title><split_character><body><optional_comments>
    split_character: ':', 'tab', x4'space', '#'
    110 : Title	Body # It's ok
<hr>
    
### Dependencies
    pip install -r requirements.txt
    marshmallow==3.13.0
    requests==2.26.0

