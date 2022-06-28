from flask import jsonify, abort, make_response 

def error_msg(message, status_code):
    abort(make_response(jsonify(dict(details=message)), status_code))

    
def make_model(cls, data_dict):
    try: 
        model = cls.from_dict(data_dict)
    except KeyError: 
        error_msg("invalid data", 400)

    return model    