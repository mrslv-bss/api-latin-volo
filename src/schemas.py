from marshmallow import Schema, fields, ValidationError, validate, INCLUDE


# Creating schemas
class JSONSchema(Schema):
    userid = fields.Integer(required=True,validate=validate.Range(min=1,max=10))
    title = fields.String(required=True)
    body = fields.String(required=True)
    ID = fields.String(validate=validate.Range(min=1,max=100))
    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE
        
def validate(user_data):
    # Validate by marshmallow our JSON
    try:
        JSONSchema(many=True).load(user_data)
    except ValidationError as err:
        print(err.messages)
    ##