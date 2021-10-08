from marshmallow import Schema, fields, ValidationError, validate, INCLUDE
import logging


class JSON_Schema(Schema):
    userid = fields.Number(required=True,
                           validate=validate.Range(min=1, max=200))
    title = fields.String(required=True)
    body = fields.String(required=True)
    id = fields.Number(validate=validate.Range(min=101))

    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE


def validate(user_data):
    try:
        JSON_Schema(many=True).load(user_data)
        return True
    except ValidationError as err:
        logging.warning(err.messages)
        return False
