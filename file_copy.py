import os, shutil, time

start = time.time()

src = 'C:\\Python\\python_file_copy\\Test Files\\';
dst = 'C:\\Python\\python_file_copy\\Test Output\\'
   
with open('list.txt', 'r') as list_test:
    print('Opening list file for reading')
    with open('log.txt', 'a', 1) as log:
        for filename in list_test:
            print('Searching for file ' + filename)
            log.write('Searching for file ' + filename + '\n')
            filename = filename.rstrip() + '.xml'
            if os.path.isfile(src + filename):
                print(filename + ' File found, copying to new location')
                log.write(filename + ' File found, copying to new location\n')
                shutil.copy(src + filename, dst + filename);                
            
end = time.time()
print(end - start)