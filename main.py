from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import os
from pathlib import Path
from utils import load_parsers, transform_object

app = Flask(__name__)


# Load all parsers dynamically
parsers = load_parsers()


@app.route('/evidence', methods=['POST'])
def receive_evidence():
    request_data = request.get_json()
    successfully_parsed = {};
    if "evidence_data" in request_data:
        evidence_list = request_data["evidence_data"]

        for evidence_payload in evidence_list:
            # Iterate over parsers until one is found that can handle the evidence
            for parser in parsers:
                if parser.detect(evidence_payload):
                    # Process the evidence using the identified parser
                    parsed_data = parser.parse(evidence_payload)
                    if parsed_data is not None:
                        successfully_parsed[parser.type] = successfully_parsed.get(parser.type,[]) + [parsed_data]
                        
                    else:
                        parsed_data = default_parser.parse(evidence_payload)
                        successfully_parsed['unknown'] = successfully_parsed.get('default',[]).append(parsed_data)
                    
            else:
                return jsonify({"status": "No suitable parser found for the evidence"})

        return jsonify({"status": "Received and processed evidence list successfully","data":transform_object(successfully_parsed)})
    else:
        return jsonify({"status": "No evidence list provided in the request"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
