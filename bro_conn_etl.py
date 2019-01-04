import pandas as pd
import numpy as np
import array
import sys, csv

# load dataset
df = pd.read_csv(str(sys.argv[1]), delimiter='\t')
# Or export it in many ways, e.g. a list of tuples
tuples = [tuple(x) for x in df.values]

# or export it as a list of dicts
dicts = df.to_dict().values()

# functions
def extract_px( orig_pkts, resp_pkts):
   temp = orig_pkts + resp_pkts
   return temp

def extract_nnp( px ):
	if(px == 0):
		temp = 1
	else:
		temp = 0
	return temp

def extract_nsp(px):
	if(px >= 63 and px <= 400 ):
		temp = 1
	else:
		temp = 0
	return temp

def extract_psp( nsp, px ):
	if(px == 0.0):
		temp = 0.0
	else:
		temp = nsp / px
	return temp

def extract_iopr( orig_pkts, resp_pkts ):
	if(resp_pkts != 0):
		temp = orig_pkts / resp_pkts;
	else:
		temp = 0
	return temp

def extract_reconnect( history ):
	if history.find("Sr") == -1:
		temp = 0    	
	else:
		temp = 1

	return temp

def extract_fps( orig_ip_bytes, orig_pkts ):
    if(orig_pkts !=0 ):
    	temp = orig_ip_bytes / orig_pkts
    else:
    	temp = 0    
    return temp

def extract_tbt(orig_ip_bytes, resp_ip_bytes):
 	temp = orig_ip_bytes + resp_ip_bytes
 	return temp

def extract_apl(px, orig_ip_bytes, resp_ip_bytes):
    if(px == 0):
        temp = 0             
    else:
        temp = (orig_ip_bytes + resp_ip_bytes )/px
    
    return temp

def extract_pps(duration, orig_pkts, resp_pkts):
	# print(type(duration))
	# print(type(orig_pkts))
	# print(type(resp_pkts))
    if(duration != "-"):
    	duration = float(duration)
    	temp = (orig_pkts + resp_pkts ) / duration
    else:
        temp = 0.0       
    return temp


# Create a list to store the data
label = []
px = []
nnp = []
nsp = []
psp = []
iopr = []
reconnect = []
fps = []
tbt = []
apl = []
pps = []

# proses feature extraction
# set px
for index, row in df.iterrows():
	px.append(extract_px(row['orig_pkts'], row['resp_pkts']))
df['px'] = px

# set nnp
for index, row in df.iterrows():
	nnp.append(extract_nnp(row['px']))
df['nnp'] = nnp

# set nsp
for index, row in df.iterrows():
	nsp.append(extract_nsp(row['px']))
df['nsp'] = nsp

# set psp
for index, row in df.iterrows():
	psp.append(extract_psp(row['nsp'],row['px']))
df['psp'] = psp

# set iopr
for index, row in df.iterrows():
	iopr.append(extract_iopr(row['orig_pkts'],row['resp_pkts']))
df['iopr'] = iopr

# set reconnect
for index, row in df.iterrows():
	reconnect.append(extract_reconnect(row['history']))
df['reconnect'] = reconnect

# set fps
for index, row in df.iterrows():
	fps.append(extract_fps(row['orig_ip_bytes'], row['orig_pkts']))
df['fps'] = fps

# set tbt
for index, row in df.iterrows():
	tbt.append(extract_tbt(row['orig_ip_bytes'], row['resp_ip_bytes']))
df['tbt'] = tbt

# set apl
for index, row in df.iterrows():
	apl.append(extract_apl(row['px'],row['orig_ip_bytes'], row['resp_ip_bytes']))
df['apl'] = apl

# set pps
for index, row in df.iterrows():
	pps.append(extract_pps(row['duration'],row['orig_pkts'], row['resp_pkts']))
df['pps'] = pps


# compare label and dataset
# For each row in the column,
for ip in df['id.orig_h']:
	if ip =="192.168.50.14" :
		label.append("malicious")
	elif ip =="192.168.50.15" :
		label.append("malicious")
	elif ip =="192.168.50.16" :
		label.append("malicious")
	elif ip =="192.168.50.17" :
		label.append("malicious")
	elif ip =="192.168.50.18" :
		label.append("malicious")
	elif ip =="192.168.50.30" :
		label.append("malicious")
	elif ip =="192.168.50.31" :
		label.append("malicious")
	elif ip =="192.168.50.32" :
		label.append("malicious")
	elif ip =="192.168.50.34" :
		label.append("malicious")
	elif ip == "192.168.50.19" :
		label.append("normal")
	elif ip == "192.168.50.50" :
		label.append("normal")
	elif ip == "192.168.50.51" :
		label.append("normal")
	elif ip == "192.168.50.52" :
		label.append("normal")
	elif ip == "192.168.50.54" :
		label.append("normal")
	elif ip == "192.168.50.55" :
		label.append("normal")
	elif ip == "192.168.50.56" :
		label.append("normal")
	elif ip == "192.168.50.57" :
		label.append("normal")
	elif ip == "192.168.50.58" :
		label.append("normal")
	elif ip == "192.168.50.59" :
		label.append("normal")
	elif ip == "192.168.50.60" :
		label.append("normal")
	elif ip == "192.168.50.61" :
		label.append("normal")
	elif ip == "192.168.50.63" :
		label.append("normal")
	elif ip == "192.168.50.64" :
		label.append("normal")
	elif ip == "192.168.50.65" :
		label.append("normal")
	elif ip == "192.168.50.66" :
		label.append("normal")
	elif ip == "192.168.50.67" :
		label.append("normal")
	elif ip == "192.168.50.68" :
		label.append("normal")
	elif ip == "192.168.50.69" :
		label.append("normal")
	else :
		label.append("normal")

# Create a column from the list
df['label'] = label
df['px'] = px
df['nnp'] = nnp
df['nsp'] = nsp
df['psp'] = psp
df['iopr'] = iopr
df['reconnect'] = reconnect
df['fps'] = fps
df['tbt'] = tbt
df['apl'] = apl
df['pps'] = pps

# for index, row in df.iterrows():
	# print(row['id.orig_h'], row['label'],row['duration'], row['pps'])

# create column
# label.append(np.where(df['src_ip']==dfLabel['ip_address'], 'yes', 'no')
# print(df)
df.to_csv("./output/"+str(sys.argv[1]),quoting=csv.QUOTE_ALL)
