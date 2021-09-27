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
<hr>

### Log Format
    <timestamp> - <type> - <message>
    09/25/2021 08:15:39 DEBUG Starting new HTTPS connection (1): jsonplaceholder.typicode.com:443
<hr>
    
### Dependencies
    -
### Marshmallow Schemas
look here: src/schemas.py

    userid = fields.Number(required=True, validate=validate.Range(min=1, max=200))
    title = fields.String(required=True)
    body = fields.String(required=True)
    id = fields.Number(validate=validate.Range(min=101))
