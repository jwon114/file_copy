import os;
import shutil;

#dst = 'C:\Python\python_file_copy\Output';
#src = 'C:\Python\python_file_copy\Files';
dst = 'C:\Slainte_Data\Python\python_file_copy\Output';
src = 'L:\\';

with open('list.txt', 'r') as f:
	print('Opened file successfully')
	for line in f:
		for filename in os.listdir(src):
			# use rstrip() to remove \n and whitespace.			
			if line.rstrip() == filename.replace('.xml', ''):				
				print(filename + ' Copied to Output directory')			
				shutil.copy(src + '\\' + filename, dst + '\\' + filename);