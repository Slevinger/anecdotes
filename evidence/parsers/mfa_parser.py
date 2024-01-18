from evidence.base_parser import BaseParser

class MfaParser(BaseParser):
    def __init__(self):
        super().__init__(parser_type='mfa')

    def detect(self, evidence_payload):
        return "name" in evidence_payload and "priority" in evidence_payload
