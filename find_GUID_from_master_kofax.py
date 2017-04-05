import csv

#SRC1 = 'C:\\Slainte_Data\\Python\\python_file_copy\\vndocsprd_output.txt';
SRC1 = 'C:\\Slainte_Data\\Python\\python_file_copy\\vndocsprd_output_TEST.txt';
#SRC2 = 'C:\\Slainte_Data\\Python\\python_file_copy\\mrn_ep_missing_from_results.txt';
SRC2 = 'C:\\Slainte_Data\\Python\\python_file_copy\\mrn_ep_missing_from_results_TEST.txt';
DST = 'C:\\Slainte_Data\\Python\\python_file_copy\\mrn_ep_missing_from_results_input.csv';

results_set = []
vndocsprod_set = []

with open(SRC2, 'r', 1) as missingResults:
	results_set = [line.strip() for line in missingResults]
	
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
			vndocsprd_indices = [i for i, x in enumerate(vndocsprd_set) if x == key]
			print(vndocsprd_indices)
			for index in vndocsprd_indices:
				print(vndocsprd_setData[index])
			del vndocsprd_set[vndocsprd_set.index(key)]
	

#print(results_set)
#print(vndocsprd_setData)
#for key in vndocsprd_setData:	
#	vndocsprd_indices = [i for i, x in enumerate(vndocsprd_setData)]
#print(vndocsprd_set)
#print(vndocsprd_indices)


			