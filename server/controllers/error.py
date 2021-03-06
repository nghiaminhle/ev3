"""Error handling"""

from ev3bot import encode

def value_error_handler(ex, req, resp, params):
    """Error handler for ValueError"""
    resp.body = encode.encode({
        'status': 1,
        'msg': 'Bad Request: ' + str(ex)
    })

def http_error_handler(ex, req, resp, params):
    """Error handler for HTTPError"""
    resp.body = encode.encode({
        'status': 1,
        'msg': 'HTTP error: ' + ex.status
    })
