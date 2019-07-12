import os, glob, fnmatch, re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# read analyzed file 

data = pd.read_csv('VGS_analyzed.csv')

data = pd.read_csv('MGS_analyzed.csv')

data = pd.read_csv('GAP_analyzed.csv')

# get mean latency values for each group 
groupby_group = data.groupby('group')
	
	for group, value in groupby_group['latency']:
    	
    	print((group, value.mean()))

    	# print(df.groupby('group').mean().to_string())

# get mean accuracy values for each group 
groupby_group = data.groupby('group')
	
	for group, value in groupby_group['accuracy']:
    	
    	print((group, value.mean()))	

# get standard deviation 
groupby_group = data.groupby('group')
	
	for group, value in groupby_group['accuracy']:
    	
    	print((group, value.std()))	