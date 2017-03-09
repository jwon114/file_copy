import os

path = 'C:\\Python\\python_file_copy\\Test Files'

for x in range(1, 4001):
    filename = str(x) + '.xml'
    open(os.path.join(path, filename), 'a').close()