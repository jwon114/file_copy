# Using the difference in mrn_ep keys from Vitro DB and the matching result set, find the data [mrn_ep, guid, dt]
# from the KOFAX drive extraction [mrn_ep, guid, last_modified_dt]

import csv

#SRC1 = 'C:\\Slainte_Data\\Python\\Data\\vndocsprd_output.txt';
SRC1 = 'C:\\Slainte_Data\\Python\\Data\\vndocsprd_output_TEST.txt';
#SRC2 = 'C:\\Slainte_Data\\Python\\Data\\mrn_ep_missing_from_results.txt';
SRC2 = 'C:\\Slainte_Data\\Python\\Data\\mrn_ep_missing_from_results_TEST.txt';
DST = 'C:\\Slainte_Data\\Python\\Data\\mrn_ep_missing_from_results_input.csv';

results_set = []
vndocsprod_set = []

# Missing results set (Vitro DB - matching result) [mrn_ep]
with open(SRC2, 'r', 1) as missingResults:
	results_set = [line.strip() for line in missingResults]

# Create key set [mrn_ep] and data set [mrn_ep, guid, dt]
with open(SRC1, 'r', newline='') as vndocsprd:
	vndocsprd_in = csv.reader(vndocsprd, delimiter=',')	
	vndocsprd_setData = []
	vndocsprd_set = []
	for key in vndocsprd_in:
		vndocsprd_setData.append(key)
		vndocsprd_set.append(key[0])

with open(DST, 'a', 1) as missingOutput:
	for key in results_set:
		if key in vndocsprd_set:
			vndocsprd_indices = [index for index, value in enumerate(vndocsprd_set) if value == key]						
			for index in vndocsprd_indices:
				missingOutput.write(','.join(map(str,(vndocsprd_setData[index])))+'\n')								
			
			# Remove found values from the key set and data set for repeat searches
			vndocsprd_set = [value for index, value in enumerate(vndocsprd_set) if index not in vndocsprd_indices]
			vndocsprd_setData = [value for index, value in enumerate(vndocsprd_setData) if index not in vndocsprd_indices]
			