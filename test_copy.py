import os, shutil, time

start = time.time()

src = 'C:\\Python\\python_file_copy\\Test Files\\';
dst = 'C:\\Python\\python_file_copy\\Test Output\\'
   
with open('list_test.txt', 'r') as list_test:
    print('Opening list file for reading')
    for filename in list_test:
        filename = filename.rstrip() + '.xml'
        if os.path.isfile(src + filename):
            print(filename + ' File found, copying to new location')
            shutil.copy(src + filename, dst + filename);
            
end = time.time()
print(end - start)