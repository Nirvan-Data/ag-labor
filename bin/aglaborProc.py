"""
Filename: aglaborProc.py
Author: Nirvan Sengupta
Date: May 28 2021
"""

###GENERAL TODO ### 
# 1. python env
# 2. git branching, merging. 2fa
# 3. numba, profiling

### aglaborProc.py TODO ###
# 1. Codebook --> columns --> data --> tidy data 
#   a. which column which variable
#   b. processing, harmonizing, cross-walk, review variable variants
# 2. Variables 
#   a. YEAR 
#   b. RACE
#        i. isPOC
#   c. isAGLABOR
#   d. WEIGHT

import pandas as pd
import os

directory = '/media/ubuntu/D/ag-labor/data/year'
os.chdir(directory)

for file in os.listdir():

    with open(file,'r') as f:
        raw = [line.rstrip() for line in f.readlines()]
        
        keys   = ['YEAR','PERWT','RACE','RACED','HISPAN','HISPAND','IND','IND1950','IND1990','INDNAICS','IND1930']
        items = [[1,4],[72,81],[82,82],[83,85],[86,86],[87,89],[90,93],[94,96],[97,99],[100,107],[108,111]]
        procDict = dict(zip(keys,items))
        
        data = {}
        for var in procDict.keys():
            start, end = procDict[var]
            data[var] = [line[start -1 : end] for line in raw]    
        df = pd.DataFrame(data)    
        print(df)
    