#!/usr/bin/env python3
# Copyright (c) 2018 Chris Heckler <hecklerchris@hotmail.com>

def read_csv(input_file):
    data = []
    with open(input_file) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            data = [int(num) for num in row]
    return data

def write_csv(data, output_file):
    with open(output_file, 'w') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(data)
