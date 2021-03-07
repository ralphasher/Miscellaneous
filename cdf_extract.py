#import Penn State CDF files and save as CSV
#leans heavily on https://towardsdatascience.com/cdfs-using-spacepy-to-read-and-write-your-data-conveniently-9490f0bfee4a

#install CDF library from NASA website to local machine
#https://cdf.gsfc.nasa.gov/html/sw_and_docs.html
#ensure you get 32bit or 64bit CDF library to match 32bit/64bit python
#define library where CDF DLLs live
os.environ["CDF_LIB"] = 'C:\CDF_Distribution\cdf38_0-dist\lib'

import os
from spacepy import pycdf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

#define directory with CDF files
cdf_dir = 'C:/Users/W530/Documents/USMC/MTVR_CBM_CDF_20210301/'
cdf_files = os.listdir(cdf_dir)
outlist = list()

#read in CDFs in loop
for file in cdf_files:
    cdf_file = pycdf.CDF(cdf_dir + file)
    #variables dictionary to pandas dataframe
    cdf_df = pd.DataFrame.from_dict(cdf_file)
    outlist.append(cdf_df)
    

