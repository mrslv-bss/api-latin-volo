from marshmallow import Schema, fields, ValidationError, validate, INCLUDE
import logging


class JSONSchema(Schema):
    # E501 line too long (82 > 79 characters)
    userid = fields.Number(required=True, validate=validate.Range(min=1, max=200))
    title = fields.String(required=True)
    body = fields.String(required=True)
    id = fields.Number(validate=validate.Range(min=101))

    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE


def validate(user_data):
    try:
        JSONSchema(many=True).load(user_data)
        return True
    except ValidationError as err:
        logging.warning(err.messages)
        return False
