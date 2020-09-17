#Non-Obfuscated Master Copy 
# JOSH API VERSION 1.2.11

"""JoshAPI Version 1.2.11

Do not use in assessments, exams, or anything that is graded. You are welcome to use it in simple projects & exercises. All copies given out to people other than myself will be obfuscated.

To use in your programs:<br>
- Make sure joshapi.py is in the same directory as your programs<br>
- Have 'import joshapi' at the top of your programs<br>
- To use functions from JoshAPI make sure 'joshapi.' is at the front<br>

For example:

import joshapi

number = joshapi.errorCheckInputInt("Please input a number", "That was not a number!")<br>
print("You inputted %d" % (number))<br>
<br>
FOR MORE INFORMATION:<br>
Run "help(joshapi)"

<br>
<strong>Download JoshAPI</strong><br>
<a href='joshapi.py' download>Click here</a>

Disclaimer:

JoshAPI is registered under the Creative Commons license. Users are permitted to copy,
distribute, display and perform JoshAPI but users are not permitted to distribute modified or
derivative works based on it. On the occasion that a user desires to distribute modified or
derivative works based on JoshAPI then they must file an application with Openic Development
and obtain their express, written and signed permission.

JoshAPI is not permitted to be used in educational assessments or assignments that have an
effect on the outcome of the student’s grade or score without the permission of their lecturer,
instructor or educator.

JoshAPI can be copied, distributed, displayed and performed for commercial purposes provided
relevant references are provided to Joshua Mulik or Openic Development.

There are no warranties provided for JoshAPI. Openic Development does not take responsibility
for any action or event that occurs from JoshAPI. If there is a bug or error, please contact Openic
Development and the error or bug will be rectified in the next release.

If JoshAPI is used in any program, project or application JoshAPI must be appropriately credited. A
link to the license must be created and if there were any changes it must be indicated. Note that
modified versions of JoshAPI cannot be distributed or shared without prior written express
permission from Openic Development.

Openic Development cannot revoke your freedom of sharing JoshAPI by copying, or distributing in
any medium or format, even commercially, as long as the license terms are followed.
JoshAPI is licensed under Creative Commons Attribution-NoDerivatives 4.0 International License.

https://creativecommons.org/licenses/by-nd/4.0/

ANY AMENDMENTS OR CHANGE IN THE LICENSE WILL BE ANNOUNCED IN NEWER
VERSIONS OF JOSHAPI AND ON OPENIC DEVELOPMENT’S PUBLIC WEBSITES AND
FORUMS. OLDER RELEASES OF JOSHAPI WILL USE THEIR ORIGINAL LICENSE

"""
import math
import random
import traceback
import time
import os
import sys
import os.path
import argparse
from urllib.request import urlopen, Request
try:
	from bs4 import BeautifulSoup
except ModuleNotFoundError:
	print("Installing requried modules (beautifulsoup4)...")
	os.system("pip install beautifulsoup4")
	print("Completed.")
	from bs4 import BeautifulSoup
	
from datetime import datetime
try:
	from pynput import keyboard
except ModuleNotFoundError:
	print("Installing requried modules (pynput)...")
	os.system("pip install pynput")
	print("Completed.")
	from pynput import keyboard

VERSION = "1.2.11"

def Info():
	"""Provides the version and basic information for JoshAPI
	"""
	print("Josh API Version %s" %(VERSION))
	print(" ")
	print("Do not use in assessments, exams, or anything that is graded. You are welcome to use it in simple projects & exercises. All copies given out to people other than myself will be obfuscated.")
	print("""
	How To use in your programs:
	- Make sure joshapi.pyc is in the same directory as your programs
	- Have \'import joshapi\' at the top of your programs
	- To use functions from JoshAPI make sure \'joshapi.\' is at the front

	For example:

	import joshapi

	number = joshapi.ErrorCheckInputInt(\"Please input a number\", \"That was not a number!\")
	print(\"You inputted %d\" % (number))
	
	--
	
	FOR MORE INFORMATION:
	Run \"help(joshapi)\"""")
info = Info
 

def errorCheckInputInt(out,err):
	"""Returns an error checked input value, ensures it is an integer
	
	Keyword arguments:
	out -- Message to user
	err -- Error message to send to user
	return int
	"""
	ret = None
	while(ret == None):
		try:
			ret = int(input(out))
		except:
			print(err)
	return ret

def errorCheckInputFloat(out,err):
	"""Returns an error checked input value, ensures it is a float
	
	Keyword arguments:
	out -- Message to user
	err -- Error message to send to user
	return int
	"""
	ret = None
	while(ret == None):
		try:
			ret = float(input(out))
		except:
			print(err)
	return ret    

def errorCheckCertainInput(out,err,inputs):
	"""Returns an error checked input value, ensures it is in the list of possible inputs
	
	Keyword arguments:
	out -- Message to user
	err -- Error message to send to user
	inputs -- List of allowed inputs
	return string
	"""
	ret = None
	while(ret == None):
		inp = input(out)
		if(inp in inputs):
			ret = inp
		else:
			print(err)
	return ret

def errorCheckFloatRangeInclusive(out,err,min,max):
	"""Returns an error checked input value, it ensures it is a float and it is between the minimum and maximum ranges inclusive
	
	Keyword arguments:
	out -- Message to user
	err -- Error message to send to user
	min -- Minimum number
	max -- Maximum number
	return float
	"""
	ret = None
	while(ret == None):
		inp = errorCheckInputFloat(out,err)
		if(inp >= min and inp <= max):
			ret = inp
		else:
			print(err)
	return ret


def errorCheckFloatRange(out,err,min,max):
	"""Returns an error checked input value, it ensures it is a float and it is between the minimum and maximum ranges not inclusive
	
	Keyword arguments:
	out -- Message to user
	err -- Error message to send to user
	min -- Minimum number
	max -- Maximum number
	return float
	"""
	ret = None
	while(ret == None):
		inp = errorCheckInputFloat(out,err)
		if(inp > min and inp < max):
			ret = inp
		else:
			print(err)
	return ret  


def errorCheckIntRangeInclusive(out,err,min,max):
	"""Returns an error checked input value, it ensures it is a int and it is between the minimum and maximum ranges inclusive
	
	Keyword arguments:
	out -- Message to user
	err -- Error message to send to user
	min -- Minimum number
	max -- Maximum number
	return int
	"""
	ret = None
	while(ret == None):
		inp = errorCheckInputInt(out,err)
		if(inp >= min and inp <= max):
			ret = inp
		else:
			print(err)
	return ret


def errorCheckIntRange(out,err,min,max):
	"""Returns an error checked input value, it ensures it is a int and it is between the minimum and maximum ranges not inclusive
	
	Keyword arguments:
	out -- Message to user
	err -- Error message to send to user
	min -- Minimum number
	max -- Maximum number
	return int
	"""
	ret = None
	while(ret == None):
		inp = errorCheckInputInt(out,err)
		if(inp > min and inp < max):
			ret = inp
		else:
			print(err)
	return ret      


def makeCaesarCipher(inString,count):
	"""Generates a caesar cipher 
	
	Keyword arguments:
	inString -- String to encrypt
	count -- Encryption distance
	return string
	"""
	minASCII = 33
	maxASCII = 126
	newString = "";
	for i in inString:
		addTo = ord(i)+count
		while(addTo > maxASCII):
			addTo -= maxASCII;
			if(addTo < minASCII):
				addTo += minASCII-1;
		while(addTo < minASCII):
			addTo += minASCII-1;
		newString += chr(addTo)
	return newString


def makeCaesarCipherQuadratic(inString,count):
	"""Generates a caesar cipher 
	
	Keyword arguments:
	inString -- String to encrypt
	count -- Encryption distance
	return string
	"""
	minASCII = 33
	maxASCII = 126
	newString = "";
	for i in inString:
		addTo = ord(i)+count
		addTo = 3*addTo**2 + 2*addTo + 6
		while(addTo > maxASCII):
			addTo -= maxASCII;
			if(addTo < minASCII):
				addTo += minASCII-1;
		while(addTo < minASCII):
			addTo += minASCII-1;
		newString += chr(addTo)
	return newString


def drawAxis(turt,scale):
	"""Using a turtle it draws a 2D Cartesian plane
	
	Keyword arguments:
	turt -- The turtle to draw with
	scale -- Width of the axis
	"""
	turt.clear()
	turt.speed(10)
	turt.up()
	turt.goto(0,scale)
	turt.pencolor('black')
	turt.down()
	turt.goto(0,-scale)
	turt.up()
	turt.goto(scale,0)
	turt.down()
	turt.goto(-scale,0)
	turt.up()
	turt.home()

def drawQuadratic(turt,a,b,c,r,colour,accuracy,scale):
	"""Using a turtle it draws a quadratic graph
	Formula: y = ax^2 + bx + c
	
	Keyword arguments:
	turt -- The turtle to draw with
	a -- a on the formula
	b -- b on the formula
	c -- c on the formula
	r -- Range of the graph (100 is from -100 X to 100 X)
	colour -- What colour to draw the graph
	accuracy -- What scale to draw by (every 1 X, every 0.5 x etc)
	"""
	turt.up()
	turt.pencolor(colour)
	turt.home()
	turt.pensize(scale/75)
	x = -r
	y = a*x**2 + b*x + c
	if(y > scale):
		turt.goto(x,scale)
	else:
		turt.goto(x,y)
	while(x < r):
		y = a*x**2 + b*x + c
		turt.down()
		if(y > scale):
			turt.goto(x,scale)
		else:
			turt.goto(x,y)
		x += accuracy

	turt.up()
	turt.home()


def drawSineWave(turt,a,b,c,r,colour,accuracy,scale):
	"""Using a turtle it draws a sine graph
	Formula: y = a * sin(bx) + c
	
	Keyword arguments:
	turt -- The turtle to draw with
	a -- a on the formula
	b -- b on the formula
	c -- c on the formula
	r -- Range of the graph (100 is from -100 X to 100 X)
	colour -- What colour to draw the graph
	accuracy -- What scale to draw by (every 1 X, every 0.5 x etc)
	"""
	turt.up()
	turt.pencolor(colour)
	turt.home()
	turt.pensize(scale/75)
	x = -r
	y = a*math.sin(b*x) + c 
	if(y > scale):
		turt.goto(x,scale)
	else:
		turt.goto(x,y)
	while(x < r):
		y = a*math.sin(b*x) + c 
		turt.down()
		if(y > scale):
			turt.goto(x,scale)
		else:
			turt.goto(x,y)
		x += accuracy

	turt.up()
	turt.home()   

def drawCosineWave(turt,a,b,c,r,colour,accuracy,scale):
	"""Using a turtle it draws a cosine graph
	Formula: y = a * cos(bx) + c
	
	Keyword arguments:
	turt -- The turtle to draw with
	a -- a on the formula
	b -- b on the formula
	c -- c on the formula
	r -- Range of the graph (100 is from -100 X to 100 X)
	colour -- What colour to draw the graph
	accuracy -- What scale to draw by (every 1 X, every 0.5 x etc)
	"""
	turt.up()
	turt.pencolor(colour)
	turt.home()
	turt.pensize(scale/75)
	x = -r
	y = a*math.cos(b*x) + c 
	if(y > scale):
		turt.goto(x,scale)
	else:
		turt.goto(x,y)
	while(x < r):
		y = a*math.cos(b*x) + c 
		turt.down()
		if(y > scale):
			turt.goto(x,scale)
		else:
			turt.goto(x,y)
		x += accuracy

	turt.up()
	turt.home()       


def drawTanGraph(turt,a,b,c,r,colour,accuracy,scale):
	"""Using a turtle it draws a tan graph
	Formula: y = a * tan(bx) + c
	
	Keyword arguments:
	turt -- The turtle to draw with
	a -- a on the formula
	b -- b on the formula
	c -- c on the formula
	r -- Range of the graph (100 is from -100 X to 100 X)
	colour -- What colour to draw the graph
	accuracy -- What scale to draw by (every 1 X, every 0.5 x etc)
	"""
	turt.up()
	turt.pencolor(colour)
	turt.home()
	turt.pensize(scale/75)
	x = -r
	y = a*math.tan(b*x) + c 
	if(y > scale):
		turt.goto(x,scale)
	else:
		turt.goto(x,y)
	while(x < r):
		y = a*math.tan(b*x) + c 
		turt.down()
		if(y > scale):
			turt.goto(x,scale)
		else:
			turt.goto(x,y)
		x += accuracy

	turt.up()
	turt.home()          

def drawExpoGraph(turt,a,b,c,r,colour,accuracy,scale):
	"""Using a turtle it draws an exponential curve/s
	Formula: y = a^(bx)+c
	
	Keyword arguments:
	turt -- The turtle to draw with
	a -- a on the formula
	b -- b on the formula
	c -- c on the formula
	r -- Range of the graph (100 is from -100 X to 100 X)
	colour -- What colour to draw the graph
	accuracy -- What scale to draw by (every 1 X, every 0.5 x etc)
	"""
	turt.up()
	turt.pencolor(colour)
	turt.home()
	turt.pensize(scale/75)
	x = -r
	y = a**(b*x) + c 
	if(y > scale):
		turt.goto(x,scale)
	else:
		turt.goto(x,y)
	while(x < r):
		y = a**(b*x) + c 
		print(y,x)
		turt.down()
		if(y > scale):
			turt.goto(x,scale)
		else:
			turt.goto(x,y)
		x += accuracy

	turt.up()
	turt.home() 


def drawStrings(turt,startX,startY,strings,color,fontSize):
	"""Using a turtle it draws a list of strings, each on a new line relative to the font size
	
	Keyword arguments: 
	turt -- The turtle to draw with
	startX -- Where to start drawing the strings on the x axis
	startY -- Where to start drawing the strings on the y axis
	strings -- A list of strings to display
	color -- What colour to display the strings as
	fontSize -- Fontsize of the strings to display
	"""
	turt.up()
	turt.goto(startX,startY)
	turt.pencolor(color)
	turt.speed(10)

	count = 0;
	for i in strings:
		turt.goto(startX,startY+count*fontSize)
		turt.write(i)
		count += 1
	turt.home()


def drawArc(turt,x,y,degrees,rotation,color,pensize):
	"""Using a turtle it draws an arc
	
	Keyword arguments:
	turt -- The turtle to draw with
	x -- X value to draw the arc
	y -- Y value to draw the arc
	degrees - How wide the arc is in degrees
	rotation - Rotating the arc
	color -- What colour the arc is
	pensize -- The width of the pen
	"""
	turt.up()
	turt.goto(x,y)
	turt.pensize(pensize)
	turt.pencolor(color)
	for i in range(degrees):
		turt.down()
		turt.setheading(i+rotation)
		turt.forward(pensize)
	turt.up()


def generateRandomNumber(digits):
	"""Generates a random number with the length of the digits, the seed is based on the current time
	
	Keyword arguments:
	digits -- How long the random number will be
	"""
	random.seed(random.seed(int(round(time.time() * 1000))))
	return random.randrange(1*10**digits)


def generateRandomNumberSeed(digits,seed):
	"""Generates a random number with the length of the digits
	
	Keyword arguments:
	digits -- How long the random number will be
	seed -- Seed to use for the random number generator
	"""
	random.seed(seed)
	return random.randrange(1*10**digits)  

def generateRandomRangeNumber(r1,r2):
	"""Generates a random number between two digits, the seed is based on the current time
	
	Keyword arguments:
	r1 -- Minimum number
	r2 -- Maximum number
	"""
	random.seed(random.seed(int(round(time.time() * 1000))))
	return random.randrange(r1,r2)   


def checkFunction(func):
	"""If an error is thrown in the function provided it will explain in more detail what happened (And in simpleton terms) so you can actually understand what happened.
	
	<br>
	How to use:<br>
	-Make a function:<br>
	def aFunction():<br>
		doThis()<br>
	-Run the function with this function:<br>
	joshapi.CheckFunction(aFunction)<br>
	-Success!<br>
	<br>
	
	Kryword arguments:
	func -- Function
	"""
	try:
		func()
	except SyntaxError:
		print("There is a syntax error in your function. Are you missing brackets, colons, things like that?")
		print("Full traceback:")
		traceback.print_exc()
	except FileNotFoundError:
		print("The file you tried to read or append to was not found. Make sure you are accessing the correct file.")
		print("Full traceback:")
		traceback.print_exc()
	except ZeroDivisionError:
		print("You cannot divide by zero!")
		print("Full traceback:")
		traceback.print_exc()
	except ImportError:
		print("You are importing a module that does not exist! Make sure if you are importing another python file, have it in the running directory as this program.")
		print("Full traceback:")
		traceback.print_exc()
	except AssertionError:
		print("Raised when an assert statement fails.")
		print("Full traceback:")
		traceback.print_exc()
	except AttributeError:
		print("Raised when attribute assignment or reference fails.")
		print("Full traceback:")
		traceback.print_exc()
	except EOFError:
		print("Raised when the input() function hits end-of-file condition. Have you put enough tabs in your program, did you close all your if statements and brackets.")
		print("Full traceback:")
		traceback.print_exc()
	except FloatingPointError:
		print("A floating point operator failed.")
		print("Full traceback:")
		traceback.print_exc()
	except GeneratorExit:
		print("Your generator was closed.")
		print("Full traceback:")
		traceback.print_exc()
	except IndexError:
		print("That index is not in the list, is it too big? Is it not assigned to anything?")
		print("Full traceback:")
		traceback.print_exc()
	except KeyError:
		print("That key is not in your dictionary, is it too big? Is it not assigned?")
		print("Full traceback:")
		traceback.print_exc()
	except KeyboardInterrupt:
		print("The user force quit the program")
		print("Full traceback:")
		traceback.print_exc()
	except MemoryError:
		print("Your program ran out of memory, assign more memory or reduce the amount of operations.")
		print("Full traceback:")
		traceback.print_exc()
	except NameError:
		print("You have incorrectly named your variables or it is not in the correct local or global scope.")
		print("Full traceback:")
		traceback.print_exc()
	except NotImplementedError:
		print("That function does not exist!")
		print("Full traceback:")
		traceback.print_exc()
	except OSError:
		print("Your OS has thrown an error")
		print("Full traceback:")
		traceback.print_exc()
	except OverflowError:
		print("The number you are trying to do arithmetic on is too large!")
		print("Full traceback:")
		traceback.print_exc()
	except ReferenceError:
		print("Raised when a weak reference proxy is used to access a garbage collected referent.")
		print("Full traceback:")
		traceback.print_exc()
	except RuntimeError:
		print("Unknown runtime error occured.")
		print("Full traceback:")
		traceback.print_exc()
	except IndentationError:
		print("You have incorrectly indented your code!")
		print("Full traceback:")
		traceback.print_exc()
	except TabError:
		print("Make sure you only use either tabs or spaces. Not both!")
		print("Full traceback:")
		traceback.print_exc()
	except SystemError:
		print("An internal interpreter error occured.")
		print("Full traceback:")
		traceback.print_exc()
	except TypeError:
		print("You are trying to do operations to a variable that is the incorrect type!")
		print("Full traceback:")
		traceback.print_exc()
	except UnicodeError:
		print("There was an error processing your unicode")
		print("Full traceback:")
		traceback.print_exc()
	except ValueError:
		print("The variable is of correct type but it was given an improper value")
		print("Full traceback:")
		traceback.print_exc()
	except:
		print("An undocumented error occured.")
		print("Full traceback:")
		traceback.print_exc()

def binaryToDecimal(bi):
	"""Converts binary to decimal
	
	Keyword arguments:
	bi -- Binary number
	return int
	"""
	return int(bi,2)

def decimalToBinary(de):
	"""Convert decimal to binary
	
	Keyword arguments:
	de - Decimal number
	return bin
	"""
	return bin(de)

def octalToDecimal(oc):
	"""Convert octal to decimal
	
	Keyword arguments:
	oc - Octal number
	return int
	"""
	return int(oc,8)

def decimalToOctal(de):
	"""Converts decimal to octal
	
	Keyword arguments:
	de - Decimal number
	return octal
	"""
	return oct(de)

def hexToDecimal(he):
	"""Converts hex to decimal
	
	Keyword arguments:
	he - Hex number
	return int
	"""
	return int(he,16)

def decimalToHex(de):
	"""Converts decimal to hex
	
	Keyword arguments:
	de - Decimal number
	return hex
	"""
	return hex(de)
   
def binaryToOctal(bi):
	"""Converts binary to octal
	
	Keyword arguments:
	bi - Binary number
	return octal
	"""
	return oct(binaryToDecimal(bi))
	
def binaryToHex(bi):
	"""Converts binary to hex
	
	Keyword arguments:
	bi - Binary number
	return hex
	"""
	return hex(binaryToDecimal(bi))

def octalToBinary(oc):
	"""Converts octal to binary
	
	Keyword arguments:
	oc - Binary number
	return bin
	"""
	return bin(octalToDecimal(oc))

def octalToHex(oc):
	"""Converts octal to hex
	
	Keyword arguments:
	oc - Binary number
	return hex
	"""
	return hex(octalToDecimal(oc))
	
def hexToOctal(he):
	"""Converts hex to octal
	
	Keyword arguments:
	he -- Hex number
	return oct
	"""
	return oct(hexToDecimal(he))

def hexToDecimal(he):
	"""Converts hex to octal
	
	Keyword arguments:
	he -- Hex number
	return int
	"""
	return int(he,16)
	
def hexToBinary(he):
	"""Converts hex to obinary
	
	Keyword arguments:
	he -- Hex number
	return bin
	"""
	return bin(hexToDecimal(he))

def is_ascii(s):
	"""Returns true if the given string is an appropriate ascii string
	
	Keyword arguments:
	s -- String in
	return boolean
	"""
	return all(ord(c) < 128 for c in s)
	
def listToString(li):
	"""Turns a list of strings to a large single ASCII list.
	
	Keyword arguments:
	li - List in
	return string
	"""
	ret = ""
	for i in li:
		if(is_ascii(str(i))):
			ret += str(i)
	return ret
	
def addToWordList(url,saveTo):
	"""Reads a website and generates a file of all the different words in that website
	   
	   Keyword arguments:
	   url -- URL in
	   saveTo -- File to save to (do not include the txt file)
	"""
	allWords = []
	saveTo = saveTo+".txt"

	exist = os.path.isfile(saveTo)
	if(exist):
		file = open(saveTo,'r')
	
		while True:
			line = file.readline()
			allWords += [line]
			if(line == ""):
				break
	
		file.close()

	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html,'html.parser')
	
	for script in soup(["script", "style"]):
		script.extract()
	
	text = soup.get_text()
	lines = (line.strip() for line in text.splitlines())
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	text = '\n'.join(chunk for chunk in chunks if chunk)
	
	for i in text.split(' '):
		if(i.isalpha()):
			allWords += [i + "\n"]
	
	allWords = list(dict.fromkeys(allWords))
	
	file = open(saveTo,'a')
	
	file.write(listToString(allWords))
	
	file.close()
	
def generateWordList(saveTo):
	"""Generates a wordlist of approximately 432000 different words based on the top 10 wikipedia articles
	   
	   Keyword arguments:
	   saveTo -- File to save to (do not include the txt file)
	"""
	
	print("Generating word list for "+saveTo+".txt")
	print("Clearing previous...")
	sv = saveTo+".txt"
	file = open(sv,'w')
	
	file.write("")
	
	file.close()
	
	print("Article one...")
	addToWordList('https://en.wikipedia.org/wiki/Spanish_colonization_of_the_Americas',saveTo)
	print("Article two...")
	addToWordList('https://en.wikipedia.org/wiki/Pet%C3%A9n',saveTo)
	print("Article three...")
	addToWordList('https://en.wikipedia.org/wiki/Guatemala',saveTo)
	print("Article four...")
	addToWordList('https://en.wikipedia.org/wiki/Maya_civilization',saveTo)
	print("Article five...")
	addToWordList('https://en.wikipedia.org/wiki/Nojpet%C3%A9n',saveTo)
	print("Article six...")
	addToWordList('https://en.wikipedia.org/wiki/Air_raids_on_Japan',saveTo)
	print("Article seven...")
	addToWordList('https://en.wikipedia.org/wiki/Operation_Matterhorn',saveTo)
	print("Article eight skipped...")
	#addToWordList('https://en.wikipedia.org/wiki/Maya_civilization',saveTo) DUPLICATE (fixed 1.2.9)
	print("Article nine...")
	addToWordList('https://en.wikipedia.org/wiki/Michael_Jackson',saveTo)
	print("Article ten...")
	addToWordList('https://en.wikipedia.org/wiki/Byzantine_navy',saveTo)
	print("Article eleven...")
	addToWordList('https://en.wikipedia.org/wiki/Pope_Pius_XII',saveTo)
	print("Article twelve...")
	addToWordList('https://en.wikipedia.org/wiki/Military_history_of_Puerto_Rico',saveTo)
	print("Article thirteen...")
	addToWordList('https://en.wikipedia.org/wiki/History_of_Poland_(1945%E2%80%9389)',saveTo)
	print("Article fourteen...")
	addToWordList('https://en.wikipedia.org/wiki/Manhattan_Project',saveTo)
	print("Article fifteen...")
	addToWordList('https://en.wikipedia.org/wiki/Elvis_Presley',saveTo)
	print("Loaded 15 articles to wordlist.")
	
def updateJoshAPI():

	headers = {"User-Agent": "Mozilla//5.0 (Windows NT 6.1) AppleWebKit//537.36 (KHTML, like Gecko) Chrome//41.0.2228.0 Safari//537.3"}
	reg_url = "https://github.com/JoshyDEWstive/joshapi/blob/master/joshapi.py?raw=true"
	req = Request(url=reg_url, headers=headers) 
	
	paList = []
	usePath = ""
	for p in sys.path:
		strList = p.split("\\")
		toCheck = strList[len(strList)-1]
		print(toCheck)
		print(p)
		if(toCheck == "lib"):
			usePath = p 
			break
	
	if(os.path.isfile(usePath + "\\joshapi.py")):
		print("Old version of JoshAPI has been saved")
		backup = open(usePath + "\\joshapi.py.old",'w')
		thisProgram = open(usePath + "\\joshapi.py",'r')
		backup.write(thisProgram.read());
		backup.close()
		thisProgram.close()

	html = urlopen(req).read()
	fi = open(usePath + "\\joshapi.py",'w')
	fi.write(html.decode("utf8"))
	fi.close()
	print(usePath)

def checkIfUpdateRequired():
	headers = {"User-Agent": "Mozilla//5.0 (Windows NT 6.1) AppleWebKit//537.36 (KHTML, like Gecko) Chrome//41.0.2228.0 Safari//537.3"}
	reg_url = "https://github.com/JoshyDEWstive/joshapi/blob/master/version.txt?raw=true"
	req = Request(url=reg_url, headers=headers) 
	
	html = urlopen(req).read().decode("utf8")
	ret = False
	if(html != VERSION):
		print("""
		Update Required
		Version differences found.
		Installed version is %s 
		Online version is %s
		""" % (VERSION,html))
		ret = True
	return ret
	
def convert_keystroke_string(keyIn):
	"""Converts a keystroke value into a read able string
	   
	   Keyword arguments:
	   keyIn - Keystroke to convert
	"""
	keystrokeDictionary = {
		"space":" ",
		"ctrl_l":"",
		"ctrl_r":"",
		"shift":"",
		"ctrl_l":"",
		"zero":"0",
		"one":"1",
		"two":"2",
		"three":"3",
		"four":"4",
		"five":"5",
		"six":"6",
		"seven":"7",
		"eight":"8",
		"nine":"9",
		"backspace":"[-]",
		"caps_lock":"[C]"
		}
	return keystrokeDictionary.get(keyIn,keyIn)

sl_listener = None
sl_options = ["down","up","enter"]
sl_selectList = []
sl_modifiers = {}
sl_currentSelect = 0
sl_out = ''

def sl_display_selectors():
	global sl_modifiers
	global sl_currentSelect
	global sl_selectList

	clear_screen()
	
	if("top" in sl_modifiers): #Print display modifier
		print(sl_modifiers["top"]);

	count = 0
	selectionTab = "> "

	if("tab" in sl_modifiers): #If required, change the selection tab
		selectionTab = sl_modifiers["tab"]

	while(count < len(sl_selectList)):
		if(count == sl_currentSelect):
			print("%s[%s]" % (selectionTab, sl_selectList[count]))
		else:
			print("%s%s" % (selectionTab, sl_selectList[count]))
		count += 1

	if("bottom" in sl_modifiers): #Print bottom modifier
		print(sl_modifiers["bottom"]);


def clear_screen():
	"""Clears the current command prompt screen, works in Linux, Mac and Windows.
	"""
	from os import system, name

	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
		
		
def sl_on_press(key):
	"""Private utlitiy function for select_list(). Listens for keystrokes and adapts table to demonstrate that change.

	Keyword arguments:
	key - key that has been inputted
	"""
	global sl_currentSelect
	global sl_out

	try:
		k = key.char  
	except:
		k = key.name  

	if(k == 'esc'): #Escape the user input list
		sl_out = "None"
		return False

	if(k in sl_options):
		if(k == "down"): #If moving down, increase current select
			if((sl_currentSelect+1) < len(sl_selectList)):
				sl_currentSelect += 1
			else:
				sl_currentSelect = 0
		elif(k == "up"): #If moving up, decrease current select
			if((sl_currentSelect-1) >=  0):
				sl_currentSelect -= 1
			else:
				sl_currentSelect = len(sl_selectList) - 1          
		elif(k == "enter"): #If enter pressed, return key out
			sl_out = sl_selectList[sl_currentSelect]
			return False

	sl_display_selectors()
				  
def select_list(modifiers,selectList):
	"""Displays a select list to the user, use DOWN and UP arrows to control and press ESCAPE to escape the list. ENTER selects the option
	"""
	global sl_modifiers
	global sl_selectList

	sl_modifiers = modifiers
	sl_selectList = selectList
	
	sl_display_selectors()
			
	with keyboard.Listener(on_press=sl_on_press) as sl_listener:
		sl_listener.join()
	
	a = input("") #catch the enter
	return sl_out

parser = argparse.ArgumentParser(description='JOSHAPI Module')
parser.add_argument('--version',type=bool,default=False,
				   help='Checks version and updates if needed')


args = parser.parse_args()

if(__name__ == "__main__" and args.version == True):
	print("Updating...")
	updateJoshAPI()
	print("Done!")
	
elif(__name__ == "__main__"):

	print("You cannot run this by itself! It is a module!\n")
	if(checkIfUpdateRequired()):
		print("""
		A version of JOSHAPI is available.
		Please run 'python joshapi.py --version true' to update JoshAPI.
		
		""")
	else:
		print("JoshAPI version " + VERSION)
	
