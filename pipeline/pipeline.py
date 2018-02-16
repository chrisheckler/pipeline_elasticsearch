#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

from ruffus import *
from elasticsearch import Elasticsearch
from pathlib import Path
from helpers import *
import json
import csv


DATA_SCHEMA = {
    "Person": {
        "Name": [],
        "Address": [],
        "Balance": []
    }
} 

INFILE = ['data.csv']
es = Elasticsearch([{"host": "10.88.164.71", "port": 9200}])

#
# STAGE 1  - Read in file and convert to json
#

@transform(INFILE,
            suffix(".csv"),
            ".json")

def read_convert(input_file, output_file):
   data = read_csv(input_file)
   Path(output_file).write_text(json.dumps(data))
    
#
# STAGE 2 - Add 1500 to the Balance of each Person
#

@transform(read_convert,
            suffix(".json"),
            ".json")

def add_num(input_file, output_file):
    data = [1500+int(bal) for bal in input_file['Person']['Balance']]
    print(data)
    Path(out_file).write_text(json.dumps(DATA_SCHEMA))
    """
#
# STAGE 3 - Find Mean, Min and Max
#

@transform(add_num,
            suffix(".json"),
            ".json")

def index_elastic(input_file, output_file):
    out_file.write_text(json.dumps(input_file))
"""
pipeline_run()
