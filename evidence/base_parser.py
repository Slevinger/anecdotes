from abc import ABC, abstractmethod
from pathlib import Path
import json


class BaseParser(ABC):
    def __init__(self, parser_type):
        self.type = parser_type
        self.load_config()

    @abstractmethod
    def detect(self, evidence_payload):
        pass


    def evaluate_exp(self, expressions, payload=None):
            try:
                # Initialize an empty result string
                result_str = ''

                for expression in expressions:
                    # Split the expression into nested properties
                    properties = expression.split('.')
                    current_value = payload

                    for prop in properties:
                        current_value = current_value.get(prop, '')
                    
                    # Concatenate the result with a space if it's not the first expression
                    if result_str:
                        result_str += ' '
                    
                    # Append the current value to the result string
                    result_str += str(current_value)

                return result_str
            except Exception as e:
                # Handle any exceptions that may occur during concatenation
                return f"Error concatenating expressions '{expressions}': {e}"
            

        
    def parse(self, payload):
        row = {}
        if not self.detect(payload):
            return {"status": "error", "message": f"Failed to parse with {self.type}, data: {str(payload)}"}
        for field in self.config["fields"]:
            field_name = field["name"]
            try:
                # Traverse the attribute access path
                row[field_name] = self.evaluate_exp(field["source"],payload)
                
            except Exception as e:
                return {"status": "error", "message": f"Failed to parse data: {str(e)}"}
        # self.save_parsed_row(row)
        return row
    
   
    def parse_data(self, evidence_payload):
        
            structured_table = []

            # Example: Extract data from evidence_payload based on the config
            for entry in evidence_payload:
                row = self.parse(entry)
                structured_table.append(row)

            return structured_table
       

    def load_config(self):
        config_path = Path(__file__).resolve().parent.parent / "evidence" / "parsers" / "configurations" / f"{self.type}_config.json"

        if not config_path.is_file():
            raise FileNotFoundError(f"Configuration file not found for parser type '{self.type}'")

        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)
            self.id = self.config["id"]

