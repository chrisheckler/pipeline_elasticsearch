#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

from ruffus import *
from elasticsearch import Elasticsearch
from pathlib import Path
from helpers import *
import json
import csv


DATA_SCHEMA = {
    "name": {
        "address": [],
        "salary": []
    }
} 

INFILE = 'data.csv'
es = Elasticsearch([{"host": "10.88.164.71", "port": 9200}])

#
# STAGE 1  - Read in file and convert to json and add 1500 to salary
# 
@transform(INFILE,
            suffix(".csv"),
            ".json")

def read_convert_add(input_file, output_file):
    data = json.loads(Path(input_file).read_text())
    data_sal = [int(x)+1500 for x in data['person']['salary']]    
    data["person"]["salary"] = data_sal
    Path(output_file).write_text(json.dumps(data))
    
#
# STAGE 2 - Index into elasticsearch
#

@transform(read_convert_add,
            suffix(".json"),
            ".json")

def add_es_index(input_file, output_file):
    data = json.loads(Path(input_file).read_text())

    if es.indices.exists('persons'):
        res = es.indices.delete(index='persons')
        print(" response: {} ".format(res))
    print('creating persons index ...')
    es.indices.create(index='persons', body=DATA_SCHEMA)
    with open(data) as f:
        helpers.bulk(es, data, index='persons', doc_type='person')
    Path(output_file).write_text(json.dumps(data))
    
    

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
