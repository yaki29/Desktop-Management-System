import os

files = []
for path, dnames, fnames in os.walk('directory'):	# os.walk() uses BFS to traverse the directory tree
	for x in fnames:								# Enter the address of the directory to be traversed
		temp = []
		temp.append(os.path.getsize(os.path.join(path, x))/(1024*1024))	# appends files' sizes (Bytes -> MB)
		temp.append(x)				# appends files' names
		temp.append(path)			# appends files' addresses
		files.append(temp)

files.sort(reverse=True)	# sort in decreasing order

for i in range(0,10):	# Top 10 files with maximum size
	print files[i][1], 		# Name
	print files[i][0],		# Size
	print "MB",
	print files[i][2]		# Folder in which they exist


