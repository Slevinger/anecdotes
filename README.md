# anecdotes
# after unzip execute 
# 1. './run_project.sh'
# or 
# 1. 'python -m venv venv'
# 2. 'source venv/bin/activate'
# 3. 'pip install -r requirements.txt'
# 4. 'python main.py'

this will start a local service that respondes to POST requests
to the path http://10.0.0.20:8000/evidence

to add a new Parser to the system one needs to create 
1. new_parser_config.json
    - this tells the parser how to parse the data from the evidance
    - this tells the parser wat is its payload ID for parsing
2. new_parase_class.py that extends BaseParser
    - a parser without a coresponding cofig file will result in app crash
    - implement the detect function (not really necessary any more assumming we trust the data) for each parser
    - in the begining i didnt know if i can assume payload type based on evidence_id

