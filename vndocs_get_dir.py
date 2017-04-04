import os, time
from datetime import datetime

SRC = 'L:\\';
#SRC = 'C:\\Slainte_Data\\Python\\python_file_copy\\';
DST = 'C:\\Slainte_Data\\Python\\python_file_copy\\vndocsprd.txt'

with open(DST, 'a', 1) as output:    
    for file in os.scandir(SRC):        
        if file.name.endswith('.xml'):            
            last_modified = os.path.getmtime(SRC+file.name)
            last_modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_modified))
            print('Writing file ' + file.name)
            output.write(file.name + ',' + last_modified+'\n')