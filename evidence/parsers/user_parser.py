import json
from pathlib import Path
from evidence.base_parser import BaseParser

class UserParser(BaseParser):
    def __init__(self):
        super().__init__(parser_type='user')

    def detect(self, evidence_payload):
        return "login_name" in evidence_payload and "user_details" in evidence_payload