import os;
import shutil;

dst = 'D:\Python\Python_file_copy\Output';
src = 'D:\Python\Python_file_copy\Files';

f = open('list.txt', 'r')

for line in f:
	for filename in os.listdir(src):
		if line.rstrip() == filename:				
			print('yes ' + filename)			
			shutil.copy(src + '\\' + filename, dst + '\\' + filename);