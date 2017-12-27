# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:47:25 2017

@author: joelee
"""

import os
import glob
files= glob.glob('./[0-9].*')

print (str(files)
glob.glob('*.gif')

glob.glob('?.gif')
files=

csvpath = os.path.join('raw_data', 'WWE-Data-2013.csv')



# # Method 1: Plain Reading of CSVs
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module
import csv

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #  Each row is read as a row
    for row in csvreader:
        print(row)
