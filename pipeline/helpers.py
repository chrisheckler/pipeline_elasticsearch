#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>
import csv

def read_csv(input_file):
    data = {} 
    with open(input_file) as f:
        reader = csv.DictReader(f, delimiter=',')
        data = reader
    return data

def write_csv(data, output_file):
    with open(output_file, 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(data)
