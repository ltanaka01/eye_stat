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

# anova
np.unique(data.group)
from scipy.stats import f_oneway

f_oneway(data[data.group == 'AMNESIA'].accuracy,data[data.group == 'AR'].accuracy,data[data.group == 'HOA'].accuracy,df[df.group == 'MCI'].accuracy,df[df.group == 'YA'].accuracy)

# paired ttests - HOA vs patient groups 
from scipy.stats import ttest_ind 

ttest_ind(data[data.group == 'HOA'].accuracy,data[data.group == 'AMNESIA'].accuracy, equal_var=False)   
ttest_ind(data[data.group == 'HOA'].accuracy,data[data.group == 'AR'].accuracy, equal_var=False)  
ttest_ind(data[data.group == 'HOA'].accuracy,data[data.group == 'MCI'].accuracy, equal_var=False)  

# mann whitney 
from scipy.stats import mannwhitneyu

mannwhitneyu(data[data.group == 'HOA'].accuracy,data[data.group == 'YA'].accuracy)
