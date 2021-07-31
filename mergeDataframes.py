#!/usr/bin/env python3

import pandas as pd

df1_orig = pd.read_csv('file1.list', delim_whitespace=True, header=None, names=['ip','hostname'])
df2_orig = pd.read_csv('file2.list', delimiter=':', header=None, names=['hostname', 'os'])

print("\n--- Original dataframes (As it has read from the files) ---\n")

print("\nDataframe1 from file1.list:")
print(df1_orig.to_string())

print("\nDataframe2 from file2.list:")
print(df2_orig.to_string())

print("\n--- Convert all values into lowercase in Dataframe1 ---\n")

print("\nModified Dataframe1:")
df1_modified = df1_orig.applymap(lambda s:s.lower() if type(s) == str else s) # Convert dataframe1 values into lowercase
df1_modified = df1_modified.sort_values(by='hostname', ascending=True) # Sort dataframe1 by hostname
print(df1_modified.to_string())

print("\nDataframe2:")
print(df2_orig.to_string())

print("\n--- Merge dataframe2 into dataframe1 ---\n")
df1_modified = df1_modified.merge(df2_orig, how='outer', left_on='hostname', right_on='hostname')
print(df1_modified.to_string())

answer = input('Would you like to export the merged datafarame? (Type "yes", if you wanted to export): ')

if answer == "yes":
    df1_modified.to_csv('cleared_data.csv')