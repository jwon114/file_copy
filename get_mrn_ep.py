# Reads in csv file with the format: 000009_000000_26ba5965-d91c-4af3-9db6-a6f3010d6657.xml,2017-01-10 15:45:03
# Parses line and re-writes to a new csv file with format MRN_EP, GUID, DATETIME

from datetime import datetime
import csv

SRC = 'C:\\Slainte_Data\\Python\\Data\\vndocsprd.txt'
#SRC = 'C:\\Slainte_Data\\Python\\Data\\get_mrn_ep_test_input.txt'
DST = 'C:\\Slainte_Data\\Python\\Data\\vndocsprd_output.txt'

with open(SRC, 'r', 1, newline='') as csv_input:
    csv_in = csv.reader(csv_input, delimiter=',')
    with open(DST, 'a', 1, newline='') as csv_output:
        for line in csv_in:            
            mrn = line[0].split('_')[0]
            ep = line[0].split('_')[1]
            guid = line[0].strip('.xml')
            mrn_ep = mrn + '_' + ep            
            last_modified = datetime.strptime(line[1], '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')            
            output = csv.writer(csv_output, delimiter=',')
            print(guid)
            output.writerow([mrn_ep] + [guid] + [last_modified])