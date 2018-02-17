#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>
import csv
import json

def read_csv(input_file):
    data = [] 
    with open(input_file) as f: 
        reader = csv.DictReader(f, delimiter=',')
        for line in reader:
            data.append(line)
    return json.dumps(data)

def write_csv(data, output_file):
    with open(output_file, 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(data)


        
