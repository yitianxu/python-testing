outFile = open ('text.txt', 'w')
outFile.write ('this is file \n')
outFile.write ('this is second line\n')
i = 4
for i in range(1, 4): 
	outFile.write ('this is line %d\n' % (i)) 

outFile.close()

print ('test')

outputFile = open('text.txt','r')

print outputFile.read ()
print outputFile.readline()

while (line): 
	print (line, end='')
