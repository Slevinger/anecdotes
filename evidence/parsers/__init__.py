from abc import ABC, abstractmethod

class ParserBase(ABC):
    def __init__(self, parser_type):
        self.type = parser_type

    @abstractmethod
    def detect(self, evidence_payload):
        pass

    @abstractmethod
    def parse(self, evidence_payload):
        pass
