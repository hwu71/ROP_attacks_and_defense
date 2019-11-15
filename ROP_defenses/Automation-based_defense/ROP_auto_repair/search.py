import sys
TYPE = [
	'strcpy',
	'strncpy',
	'memcpy',
	'memmove',
	'memset',
	'strcat',
	'strncat',
	'fgets',
	'fread',
	'read'
]
if len(sys.argv)!=2:
	print "Usage: python search.py filename"
	sys.exit(1)

infile = open(sys.argv[1],'r')
outfile = open('report_BO.txt','w')
for (num,value) in enumerate(infile):
	for i in TYPE:
		if value.find(i+'(') > 0:
			outfile.write('%s_%d %s\n'%(infile.name,num+1,i))
infile.close()
outfile.close()
