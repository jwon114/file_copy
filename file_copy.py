import os, shutil, time, csv

start = time.time()

#SRC = 'L:\\';
SRC = 'C:\\Slainte_Data\\Python\\python_file_copy\\file_copy.csv';
#DST = 'C:\\Slainte_Data\\Python\\python_file_copy\\Output\\'
DST = 'C:\\Slainte_Data\\Python\\python_file_copy\\OutputTest\\'
   
with open('file_copy.csv', 'r', newline='') as file_csv:
    print('Opening list file for reading')
    with open('log.txt', 'a', 1) as log:
        results = csv.reader(file_csv, delimiter=',')
        for line in results:
            filename = line[1].rstrip() + '.xml'                        
            if os.path.isfile(SRC + filename):
                print(filename + ' File found, copying to new location')
                log.write(filename + ' File found, copying to new location\n')
                shutil.copy(SRC + filename, DST + filename);
            else:
                log.write('ERROR! File ' + filename + ' not found\n')
            
end = time.time()
print(end - start)