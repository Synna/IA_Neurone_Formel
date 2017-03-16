
from random import randint
import math
import pprint

#PARTIE 1: CREATION DE LA BASE DE CONNAISSANCE
# Nombre de points a cree dans la base de connaissance
number = 1000

# Le max pour X
minRange = number * (-1)
maxRange = number

# Je cree une liste pour evité les doublon lors de la creation des point
listXUse = []

print("Nous allons crée la base de connaissance")
print("La fonction afine a*x+b")
# On demande de saisire a
a = input("Saisire a : ")
a = int(a)

# On demande de saisire b
b = input("Saisire b : ")
b = int(b)

i = 0

#Je stock la base de connaissance dans une liste / tableau 
BaseDeConnaissance = []

#Je genere les points de ma base
while len(listXUse) < number :
	x = randint(minRange, maxRange)

#On verifie que il y a pas de doublon
	if x not in listXUse :
		listXUse.append( x )
		y = a*x+b

		PointGenere = ""
		PointGenere += "("+str(x)+","+str(y)+")"
#Si c'est pas un doublon je l'ajoute a la base de connaissance
		BaseDeConnaissance.append(PointGenere)

	i += 1

print(BaseDeConnaissance)
print("OK")
print("1000 points genere !")

#PARTIE 2: Le neurone 




# Initalisation
modeOpenFile = "r"
fileAffine = "kdb/affine.txt"

# object contain all the point written in the file
dataList = {}
# use to create the dataList
index = 0

# get file content
with open(fileAffine) as f:
	content = f.readlines()

# each line into a array
content = [x.strip() for x in content]

# get each point
for i in range(0, len(content) ):
	array = content[i].split( "," )
	#Remove the first char
	x = int( str( array[0] )[1:] )
	#Remove the last char
	y = int( str( array[1] )[:-1] )
	dataList[ str(index) ] =  { 'x' : x, 'y' : y }
	index += 1

# Define range for the random to get the index of hte dataList array
minNumber = 0
maxNumber = len(content)-1

# list contain all point already use
listPointUse = []

# Begin
step = 0.2

# Take randomly a value for a
a = randint(-100, 100)
# Take randomly a value for b
b = randint(-100, 100)


# Function

# Global

# find a random number not already used
def randNumber() :
	global listPointUse,minNumber,maxNumber

	number = randint(minNumber, maxNumber)

	while number in listPointUse :
		if maxNumber - len(listPointUse) < 20 :
			# when we have use all points take the last
			lastpoint = listPointUse[ len(listPointUse)-1 ]
			# clean the list
			listPointUse = []
			# put again the last to not use the same twice
			listPointUse.append( lastpoint )
		number = randint(minNumber, maxNumber)

	listPointUse.append( number )

	return number


# return a*x + b for the a,b and x parameter
def calcSomme(a,b,x) :
	return round( ( a * x + b ) , 1 )

# return a y - a * x + b for the corresponding parameter
def calcDiff(a,b,x,y) :
	calc = y - ( round( a * x , 1 ) + b )
	return round( abs(calc) ,1 )

# compare somme with y
def compare(somme, y) : 
	return ( somme == y )


# Pods A

# Increase A with step
def increaseA() :
	global a, step
	a = round( (a+step) , 1 )

# Decrease A with step
def decreaseA() :
	global a, step
	a = round( (a-step) , 1 )


# Pod B

# Increase B with step
def increaseB() : 
	global b, step
	b = round( (b+step) , 1 )

# Decrease B with step
def decreaseB() : 
	global b,step
	b = round( (b-step) , 1 )


# Begin
find = 0 # first while
findBis = 0 # second wile

while find == 0 : 
	while findBis == 0 :
		# Take a point
		index = randNumber()

		x = dataList[ str(index) ]["x"]
		y = dataList[ str(index) ]["y"]

		# Pods a :
		# actualSum : y - a*x+b
		actualSum = calcDiff(a,b,x,y)

		# sumWithStep : y - (a+step)*x+b
		sumWithStep = calcDiff( (a+step) ,b,x,y)

		# sumWithoutStep : y - (a-step)*x+b
		sumWithoutStep = calcDiff( (a-step), b,x,y)
		
		if actualSum > sumWithStep :
			# increase a
			increaseA()
		elif actualSum > sumWithoutStep :
			# decrease a
			decreaseA()

		# Pods b :
		# actualSum (if a has change) : y - a*x+b
		actualSum = calcDiff(a,b,x,y)

		# sumWithStep : y - a*x+(b+step)
		sumWithStep = calcDiff(a, (b+step) ,x,y)
		
		# sumWithoutStep : y - a*x+(b-step)
		sumWithoutStep = calcDiff(a, (b-step) ,x,y)

		if actualSum > sumWithStep :
			# increase b
			increaseB()
		elif actualSum > sumWithoutStep :
			# decrease b
			decreaseB()

		somme = calcSomme( a , b , x )

		findBis = compare(somme, y)

	# Check

	# Take a point
	index = randNumber()

	x = dataList[ str(index) ]["x"]
	y = dataList[ str(index) ]["y"]

	somme = calcSomme( a,b,x )

	find = compare(somme, y)

	if find == 0 :
		# reset findBis to restart the search for the value of each pod
		findBis = 0

#Result
result = "The function is " + str(a) + "x"

if b >= 0 :
	result += "+"

result += str(b) + "\n"

print(result)