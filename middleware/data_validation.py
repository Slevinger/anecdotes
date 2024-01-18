
from flask import Request, jsonify


class DataValidationMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)  # Create a Request object using the WSGI environment
        try:
            request_data = request.get_json(force=True)
        except Exception as e:
            response = jsonify({"status": "Invalid JSON data"})
            return response(environ, start_response)

        if "evidence_id" not in request_data or "evidence_data" not in request_data:
            response = jsonify({"status": "Invalid request data"})
            return response(environ, start_response)

        parser_id = request_data["evidence_id"]
        
        environ['data'] = request_data["evidence_data"]
        environ['parser_id'] = parser_id;

        # Continue to the next middleware or route
        return self.app(environ, start_response)


