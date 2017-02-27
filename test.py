import os;
import shutil;

dst = 'C:\Python\python_file_copy\Output';
src = 'C:\Python\python_file_copy\Files';

with open('list.txt', 'r') as f:
	for line in f:
		for filename in os.listdir(src):
			# use rstrip() to remove \n and whitespace.
			if line.rstrip() == filename:				
				print(filename + ' Copied to Output directory')			
				shutil.copy(src + '\\' + filename, dst + '\\' + filename);
<<<<<<< HEAD
			
=======
			
>>>>>>> 41bcb0ed792f5c889da6210fabf42cc46a54be6a
