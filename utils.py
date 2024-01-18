import importlib
from pathlib import Path


def custom_title(s):
    return ''.join(word.capitalize() for word in s.split('_'))

def load_parsers():
    parsers = []
    parsers_folder = Path(__file__).resolve().parent / "evidence" / "parsers"
    
    for parser_file in parsers_folder.glob("*_parser.py"):
        parser_module = parser_file.stem
        parser_class = custom_title(parser_module)
        module_path = f"evidence.parsers.{parser_module}"
        
        try:
            parser_module = importlib.import_module(module_path)
            parser_class = getattr(parser_module, parser_class)
            cls = parser_class()
            parsers.append(cls)
        except ImportError as e:
            print(f"Error importing {module_path}: {e}")
    
    parser_dict = {parser.id: parser for parser in parsers}
    return parser_dict

def transform_object(obj):
    result = {}
    for key, value in obj.items():
        result[key] = {"count": len(value), "data": value}
    return result