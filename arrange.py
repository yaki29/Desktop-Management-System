import os

fileset = []						# List of files with their destination directories

movingadd = 'directory'				# Moving address (eg. Documents)
address = 'directory'				# Test working address (eg. Desktop)
dnames = set()						# Using set for Directory names to remove Duplicates

for x in os.listdir(address):			# Lists all everything in the directory
	if os.path.isfile(os.path.join(address, x)):		# Works only on files NO links NO directories

		flag = False
		name = ""
		for c in x:								# Extract out the extension
			if flag==True:
				name+=c
			if c=='.':
				flag = True
			
		temp = []
		temp.append(x)
		temp.append(name)
		fileset.append(temp)					# Store file name and where to put it

		dnames.add(name)						# Unique Directories to be created

for name in dnames:
	os.mkdir(os.path.join(address, name))		# Make directories

for i in range(0, len(fileset)): 				# Moving files
	os.rename(os.path.join(address, fileset[i][0]), os.path.join(movingadd, os.path.join(fileset[i][1], fileset[i][0])))
