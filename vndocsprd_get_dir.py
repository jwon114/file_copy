# Gets all files and their date modified from a location
# Outputs a csv file with format MRN_EP, GUID, DATETIME

import os, time, csv
from datetime import datetime

SRC = 'L:\\';
#SRC = 'C:\\Slainte_Data\\Python\\python_file_copy\\';
#DST = 'C:\\Slainte_Data\\Python\\Data\\vndocsprd.txt'
DST = 'C:\\Slainte_Data\\Python\\Data\\test.txt'

with open(DST, 'a', 1, newline='') as csv_output:
    for file in os.scandir(SRC):        
        if file.name.endswith('.xml'):            
            last_modified = os.path.getmtime(SRC+file.name)
            last_modified = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(last_modified))
            last_modified = datetime.strptime(last_modified, '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
            mrn = file.name.split('_')[0]
            ep = file.name.split('_')[1]
            mrn_ep = mrn + '_' + ep
            print('Writing file ' + file.name)
            output = csv.writer(csv_output, delimiter=',')
            output.writerow([mrn_ep] + [file.name.strip('.xml')] + [last_modified] + '\n')