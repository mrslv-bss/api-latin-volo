# API EXAM VOLO
    # Run as 'python main -p <input_data_file>'
    > python main.py -p data.txt
### API JSONPlaceholder
* https://jsonplaceholder.typicode.com/posts

### Log Format
    <timestamp> - <type> - <message>
    09/25/2021 08:15:39 DEBUG Starting new HTTPS connection (1): jsonplaceholder.typicode.com:443
    
### Dependencies
    -
### Marshmallow Schemas
look here: src/schemas.py

    userid = fields.Integer(required=True,validate=validate.Range(min=1,max=10))
    title = fields.String(required=True)
    body = fields.String(required=True)
    ID = fields.String(validate=validate.Range(min=1,max=100))
