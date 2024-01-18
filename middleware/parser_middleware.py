
from flask import jsonify
from utils import load_parsers


parsers = load_parsers()


class AttachParserMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        parser_id = environ.get('parser_id')

        if parser_id not in parsers:
            response = jsonify({"status": f"No suitable parser was found for id: '{parser_id}'"})
            return response(environ, start_response)

        # Attach the parser to the environment
        environ['parser'] = parsers[parser_id]

        # Continue to the next middleware or route
        return self.app(environ, start_response)