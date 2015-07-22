# for in list 
#numbers = [1,2,3,4,5]
#for i in numbers: 
#	print (i)

#for i in range (0,len(numbers),2): # increment index
#	print (numbers[i])

# 41 tuple  
#number = (1,2,3,4)
#sum = 0 
#for num in numbers: 
#	sum = sum + num 
#print (sum)

#words = ('now','is','time')
#for word in words: 
#	print word 
# max length of word 
#max = 0 
#for i in range (1,len(words)): 
#	if len(words[i]) > len(words[max]):
#	 max = i 
#print max 
# minium length of word 
#n_word = ""
#x_word = words[0]
#for n_word in words: 
#    if len(n_word) < len(x_word): 
#     x_word = n_word
#print x_word 

# 42 dictionary 
#numbers = {'a':1, 'b':2, 'c':3} 
#print (numbers['a'])
#print (numbers.values())
#for key in numbers.keys(): 
#	print key + ":" + str (numbers[key])

# 43 loops with files
#outFile = open("text.txt", 'w')
#print ("line 1")
#print ("line 2") 
#outFile.close() 
#
#inFile = open("text.txt",'r')
#line   = inFile.readline()
#print line 
#for line in open('text.txt'): 
#	print (line)

#45  
#print ("enter number")
#number = int(raw_input()) 
#sum = 1
#
#if number == 1:
#	print "total: 1"
#else: 
#	while number > 1:
#		sum = number * sum
#		number = number - 1 
#print "sum: " + str(sum) 

#46 47 
#numbers = [1,2,3,4,5] 
#it = iter(numbers)
#print (it.next())
#print(next(it))
#open file not neccessary to call iter because file automatically iteration 
# next(openfile()) xxx
 
#import os
#files = os.popen('ls *.py')
#fileit = iter(files)
#print (next(fileit))

#grades  = [71, 81, 77, 84]
#grades = [grade + 5 for grade in grades]
#print grades

#words = ['WORD','IS','BIG']
#words = [word.lower() for word in words]
#print words

#N = range (1 ,101)
#EN = [x for x in N if x % 2 == 0] 


#def square(number): 
#	return number * number
#
#def nunmvowels (string): 
#     string	 = string.lower()
#     count = 0
#     for i in range (len(string)): 
#     	if string[i] == "a" or string[i] == "e": 
#     	    count = count + 1 
#     return count
#
#print ("enter number")
#num = int(raw_input())
#print (square(num)) 


# abstract/construct 
#class Name: 
#	def __init__ (self, first, middle, last): 
#		self.first  = first
#		self.middle = middle
#		self.last   = last 
#	# to-string method 
#	def __str__ (self): 
#		return self.first + self.middle + self.last
#	def last(self, x): 
#	  
#		return 2 * x
#
#
#aName = Name('a','b','c')
#bName = Name('x','y','z')
#
#
#print aName.__str__()
#print bName.__str__()
#print (bName.last(4)) 


#class Student: 
#	grades = []
#
#	def __init__ (self, name, id): 
#	    self.name = name
#	    self.id = id 
#
#	def addGrade (self, grade):
#	    self.grades.append(grade)
#
#	def showGrades(self):
#	    	grds = ''
#	    	for grade in self.grades:
#	    		grds += str(grade)
#	    	return grds

#stu1 = Student('x','3')
#stu1.addGrade('44')
#stu1.addGrade('33')
#print(stu1.showGrades())




#class Shape: 
#	def __init__(self, x, y):
#		self.x = x
#		self.y = y 
#
#	def __str__ (self): 
#		return  str(self.x) + "" + str(self.y)
#	
#	def move(self, x, y): 
#		self.x = self.x + x
#		self.y = self.y + y 
#
#class Rect(Shape): 
#	def __init__(self, x,y,w,l):
#		Shape.__init__(self,x, y)
#		self.w = w
#		self.y = l 

#class Employee: 
#	def __init__(self, name, payRate):
#		self.name = name 
#		self.payRate = payRate
#	def __str__(self):
#		return self.name + ", " + self.payRate
#	def pay(self, hour):
#		return self.payRate * hour 
#class Manager(Employee):
#	"""docstring for Manager"Employeef __init__(self, arg):
#		super(Manager,Employee.__init__()
#		self.arg = arg
#		

#e1 = Employee ('x' , 10)
#print (str(e1.pay(4)))


#def tax(amount): 
#	if amount <= 240: 
#	    return 0
#	elif amount > 240 and amount <= 480: 
#	    return amount * 0.3
#	else:  
#		return amount * 0.4
#print ('enter value\n')
#amount = int(input())
#print str (tax(amount)) 

#def factor (number): 
#	product = 1 
#	for i in range(1, number + 1): 
#		print i
#		product *= i
#	return product
#
#print factor(4)

#def countLetters(words):
#    if len(words) == 1: 
#    	#return words
#    	return 1
#    else: 
#    	#return words[0] +  ' ' + countLetters(words[1:])  
#    	return 1 + countLetters(words[1:])
#
#words = ''
#words = raw_input()
#print len(words)
#print countLetters(words)

class  Person:
	"""docstring for  """
	def __init__(self, name, sex, age):
		self.name = name 
		self.sex  = sex 
		self.age  = age
	def __str__ (self): 
		return self.name + "  " + self.sex + " " + self.age

	def changename (self,name):
	    self.name = name
	    return self.name 
			
	def setName(name):
		self.name = name
	def setSex(sex):
		self.sex = sex
	def selfage(age):
		self.age = age
		


aPerson = Person ('xu','F','1')
print aPerson.__str__()

bPerson = Person('','','')
print ('name')
bPerson.setName = raw_input()
print ('sex')
bPerson.setSex = raw_input()
print ('age')
bPerson.setAge = raw_input()	
print bPerson.__str__()	

print bPerson.changename('se')











