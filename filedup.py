import os
import sys
import shutil

def getdirsize(start_path = '.'):
	total_size = 0
	for dirpath, dirnames, filenames in os.walk(start_path):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			total_size += os.path.getsize(fp)
	return total_size

def getfilesize(filename):
	return os.path.getsize(filename)

infile = sys.argv[1]
outfile = infile + ".dup."
expectedsize = int(sys.argv[2])

infilesize = getfilesize(infile)
currentdirsize = getdirsize()
totalnewfile = round((expectedsize - currentdirsize)/infilesize)

print("Expected size: " + str(expectedsize))
print("Input file size: " + str(infilesize))
print("Total number of file created: " + str(totalnewfile))

print("*****************************")
key = input("confirm to create: [Y]es, [N]o. (default is Yes):")
if key.upper() == "Y" or key == "":
	print("run")
	for i in range(0, totalnewfile):
		shutil.copy2(infile, outfile + str(i))

else:
	print("cancelled")