from marshmallow import Schema, fields, ValidationError, validate, INCLUDE
import logging

class JSONSchema(Schema):
    userid = fields.Number(required=True,validate=validate.Range(min=1,max=200))
    title = fields.String(required=True)
    body = fields.String(required=True)
    id = fields.Number(validate=validate.Range(min=101))
    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE
        
def validate(user_data):
    # Validate by marshmallow our JSON
    try:
        JSONSchema(many=True).load(user_data)
    except ValidationError as err:
        # print(err.messages)
        logging.warning(err.messages)
    ##
