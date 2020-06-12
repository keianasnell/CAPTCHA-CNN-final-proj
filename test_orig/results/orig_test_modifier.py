#!/usr/bin/env python
import pandas
import csv

some_dict = {}
with open('test_labels.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        temp = some_dict.get(row[0], "")
        some_dict[row[0]] = temp+row[1] if temp else row[1]
print some_dict
