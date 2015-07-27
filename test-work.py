# continue/break
#i = 0 
#while i < 10: 
#  i = i + 1	
#  print(str(i)) 
#  if i == 5: 
#  	print("continue statement")
#  	#continue
#  	break
#  print("test %d" %(i) )

#write file 1.1
#outFile = open('text.txt', 'w')
#outFile.write ('this line\n')
#outFile.write ('this line2\n')
#outFile.write ('this line3\n')
#outFile.close()

#write file 1.2
#outFile = open('text.txt', 'w')
#grade = 0 
#i = 1
#summary = 0
#
#while (i < 4): 
#  grade = int(raw_input())
#  outFile.write ("grade: %d\n" % (grade))
#  i = i + 1 
#  summary = summary + grade 

#outFile.write ("totol: %d" % (summary))
#outFile.close()

#read file
#inFile = open('text.txt','r')
#line = inFile.readline() 
#print(line)
#line = inFile.readline() 
#print(line)

#inFile = open('text.txt','r')
#count = 0 
#summary = 0 
#grade = inFile.readline()
#list1 = []
#while (grade) :
#    list1 = [int(s) for s in grade.split() if s.isdigit()]
#    summary = summary + int(list1[0])
#
#    count = count + 1
#    print(str(count) + ": "+ str(list1[0])) 
#
#    grade = inFile.readline()
#    
#print  summary   
#print  float (float(summary)/float(count))    

#calculator exercise
#ope1 = 0.0 
#ope2 = 0.0
#oper = "" 
#print ("Ener first number") 
#ope1  = float(raw_input())
#print ("Ener second number") 
#ope2 = float(raw_input())
#print ("Ener operator") 
#oper = raw_input()
#
#while True: 
#  if oper == "+": 
#  	print (ope1 + ope2)
#  	break; 
#  elif oper == "-": 
#  	print (ope1 - ope2)
#  	break; 
#  elif oper == "*": 
#  	print (ope1 * ope2)
#  	break; 
#  elif oper == "/": 
#   	print  float(float(ope1) / float(ope2))
#  	break; 
#  else: 
#    print ("no match")
#    break;  


#for 
#for i in[1,2,3,4,5]: 
#	 print (i)
#numbers = [1,2,3,4,5]
#for i in numbers: 
#	print i

#word = "hello"
#for letter in word:
#	print(letter)

#words = "now is the time for all"
#count = 0
#for letter in words: 
#	if letter == "o" or \
#	   letter == "a" or \
#	   letter == "e" or \
#	   letter == "i" : 
#	   count = count + 1 
#
#print (count)

#61 

#def fact(number): 
#	if number <= 1: 
#		return 1
#	else: 
#		return  number * fact(number-1)
#
#print "Enter number"
#number = int(input()) 
#
#print fact(number)

#62

#def explode (word): 
#	if len(word) == 1: 
#		return word
#	else:
#	    return word[0] + " " + explode(word[1:])

#def removedup (word): 
#	if len(word) <= 1: 
#	    print word
#	elif word [0] == word[1]: 
#	    return removedup(word[1:])
#	else: 
#		print (word[0])
#		return removedup(word[1:])
#
#
#removedup('aaaaaaabbcc')

#63

#def square(number): 
#	return number * number
#sqnumber = square
#sqnum = sqnumber (2)
#print sqnum
#numbers = [1,2,3,4]
#print list( map (square, numbers))

#64

#square = lambda x:x*x
#print square(2) 
#numbers = [1,2,3,4]
#print list(map(lambda x:x*x, numbers))
 
 #65
 # map filter reduce

def square(number): 
 	return number * number 
print list(map(square, [1,2]))

def even (number): 
	if number % 2 == 0:
	    return True
	else:
	    return False 
def sum (x,y):
    return x + y

numbers = list (range (1,11))
print list(filter(even, numbers))

import functools
numbers1 = list (range (1,11))
sum = functools.reduce(sum,numbers1)
print sum
