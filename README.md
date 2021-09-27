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
    Configuration file variable successfully finded:
    {dir}\api-latin-volo\configuration.json
    Input file variable successfully finded:
    {dir}\api-latin-volo\input.txt
###### Explanations for the log file
	# 09/27/2021 02:26:24 INFO INPUT DATA: SUCCESS
	if validate(JSON_Validate) is True:
            logging.info("INPUT DATA: SUCCESS")
        else:
            logging.error("INPUT DATA: ERROR")

	# 09/27/2021 02:26:24 INFO Validation status: SUCCESS
	if validate(Response_Validate) is True:
            logging.info("Validation status: SUCCESS")
        else:
            logging.error("Validation status: ERROR")
	    
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
    -
### Marshmallow Schemas
look here: src/schemas.py

    userid = fields.Number(required=True, validate=validate.Range(min=1, max=200))
    title = fields.String(required=True)
    body = fields.String(required=True)
    id = fields.Number(validate=validate.Range(min=101))
