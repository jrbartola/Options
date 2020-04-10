from flask import jsonify

class BadRequest(Exception):
    status_code = 400

    def __init__(self, message, missing_value=None, invalid_value=None):
        Exception.__init__(self)
        self.message = message
        self.missing_value = missing_value
        self.invalid_value = invalid_value

    def to_dict(self):
        rv = {'message': self.message,
              'missing_value': self.missing_value,
              'invalid_value': self.invalid_value}
        return rv