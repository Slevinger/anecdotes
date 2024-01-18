from flask import Flask, Request, request, jsonify
from middleware.data_validation import DataValidationMiddleware
from middleware.parser_middleware import AttachParserMiddleware

app = Flask(__name__)

app.wsgi_app = DataValidationMiddleware(AttachParserMiddleware(app.wsgi_app))

@app.route('/evidence', methods=['POST'])
def receive_evidence():
    data = request.environ['data']
    parser = request.environ['parser']
    parsed_data = parser.parse_data(data)

    return jsonify({
        "status": "Received and processed evidence list successfully",
        "data": parsed_data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)