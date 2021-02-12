# Append-all-the-files-in-a-directory-automatically
"""In our official projects, we came across different situations where we have to automate our task to increase its efficiency. One of such task is to read all the files in a directory (including the folders and sub folders in it) and to append all these files. My name is Asif Ahmed and by profession I am a Data Analyst. I have create a code which I am going to share, that will read all the excel files in a directory and then append them and gives us a single output excel file. I have used this code multiple times and it is error free."""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 23:22:59 2021

@author: Asif.Ahmed
"""

import os
import pandas as pd
allLines = []

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   
full_file_paths = get_filepaths("C:/Path to your directory/")

for file in full_file_paths:
   print("S1")
   # Read file one by one
   data = pd.read_excel(file)
   print("S2")
   # Below steps are for manipulation you can ignore them or change accordingly
   data1 = data.dropna(axis=1, how='all')
   print("S3")
   data2 = data1.dropna(subset=['Unnamed: 1'])
   print("S4")
   data2.columns = data2.iloc[0]
   data2 = data2[1:]
   print("S5")
   # Appending dataframes on a list
   allLines.append(data2)

# Concatenate all the dataframes in a list
df = pd.concat(allLines)
# Reset index
df.reset_index(inplace=True, drop=True)
# Save the output to a location
df.to_csv("C:/Users/Path to save the output.csv")

