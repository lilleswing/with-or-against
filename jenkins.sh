#!/bin/bash
rm -rf venv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python simulator.py 8 > results.csv
python plot.py