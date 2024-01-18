#!/bin/bash

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python ./main.py 
# or if your app is in a specific file, run: python app.py
