import pandas as pd
import numpy as np
import array
import sys, csv

# load dataset
df = pd.read_csv(str(sys.argv[1]), delimiter=',')
# Or export it in many ways, e.g. a list of tuples
tuples = [tuple(x) for x in df.values]

# or export it as a list of dicts
dicts = df.to_dict().values()

# Create a list to store the data
label2 = []

# compare label and dataset
# For each row in the column,
for label in df['label']:
	if label =="normal" :
		label2.append("0")
	elif label =="malicious" :
		label2.append("1")

# Create a column from the list
df['label2'] = label2

# for index, row in df.iterrows():
# 	print(row['label2'])

# create column
# label.append(np.where(df['src_ip']==dfLabel['ip_address'], 'yes', 'no')
# print(df)
df.to_csv("./output/"+str(sys.argv[1]),quoting=csv.QUOTE_ALL)
