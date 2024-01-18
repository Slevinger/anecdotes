# default_parser.py

from evidence.base_parser import BaseParser;
from pathlib import Path
import json

class DefaultParser(BaseParser):
    def __init__(self):
        super().__init__('default')
        self.load_config()

    def load_config(self):
        config_path = Path(__file__).resolve().parent.parent / "configurations" / f"{self.type}_config.json"

        if config_path.exists():
            with open(config_path, 'r') as config_file:
                self.config = json.load(config_file)
        else:
            self.config = {}  # Configuration is optional for the default parser, set to an empty dictionary

    def detect(self, evidence_payload):
        # The default parser always returns True, as it accepts any evidence type
        return True

    def parse(self, evidence_payload):
        # The default parser simply returns the evidence payload without any changes
        return evidence_payload
