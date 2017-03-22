from random import randint
from time import sleep
import matplotlib.pyplot as plt
import math
import pprint
import os

#PARTIE 1: CRÉATION DE LA BASE DE CONNAISSANCE
#Nombre de points a crée dans la base de connaissance
number = 10000

#Le max pour X
minX = number * (-1)
maxX = number

#Je crée une liste dans la quel je vais stoker les points déjà généré pour évite les doublon
listXUse = []
print("Dans un premier temps nous allons crée la base de connaissance")
print("La fonction afine: a*x+b")
# On demande de saisir a
a = input("Saisir a : ")
a = int(a)

# On demande de saisir b
b = input("Saisir b : ")
b = int(b)

print("Génération de 10000 points grâce a la fonction ",a,"*x+",b)

i = 0
#Je stock la base de connaissance dans un dictionnaire  
BaseDeConnaissance = {}
Pointx = []
Pointy = []
#Je genere les points de ma base
while len(listXUse) < number :
	x = randint(minX, maxX)
#On verifie que X est pas un doublon
	if x not in listXUse :
		listXUse.append( x )
		y = a*x+b
		BaseDeConnaissance[str(i)] =  { 'x' : x, 'y' : y }
		Pointx.append(int(x))
		Pointy.append(int(y))
		i += 1

#On affiche la fonction afine
plt.plot(Pointx, Pointy)
plt.axis([-100, 100, -100, 100])
plt.show()

#PARTIE 2: Dans cette partie le neurone vas devoir retrouvé la fonction utilisé pour généré la base de connaissance juste en utilisent les 1000 points crée.
#Défini la valeur maximal et minimal pour l'index de la BaseDeConnaissance
minIndex = 0
maxIndex = 9999

#Liste pour les points deja utilisé
listPointUse = []

#Le pas 
step = 0.2
a = randint(-100, 100)
b = randint(-100, 100)

#Méthode qui retourne un nombre aléatoire qui n'ai pas déjà utilisé
def NombreAleatoire() :
	global listPointUse,minIndex,maxIndex
	NombreAleatoire = randint(minIndex, maxIndex)
	while NombreAleatoire in listPointUse :
		NombreAleatoire = randint(minIndex, maxIndex)
	listPointUse.append(NombreAleatoire)
	return NombreAleatoire

#Méthode pour calculer la somme
def CalculeSomme(a,b,x) :
	return round((a*x+b),1)

#Méthode pour calculer la différence
def calcDifference(a,b,x,y) :
	calc = y-(round(a*x,1)+b)
	return round(abs(calc),1)

#Méthode de comparaison avec Y
def compare(somme, y) : 
	return (somme == y)

find = 0
findBis = 0
iteration = 0
while find == 0 : 
	while findBis == 0 :
		iteration = iteration + 1
		#On prend un points aleatoire dans la basse de connaissance
		index = NombreAleatoire()
		x = BaseDeConnaissance[str(index)]["x"]
		y = BaseDeConnaissance[str(index)]["y"]

		#Calcule de la somme actuel
		actualSum = calcDifference(a,b,x,y)
		#Calcule de la difference avec le pas 
		SommeAvecPas = calcDifference((a+step),b,x,y)
		#Calcule de la difference sans le pas
		SommeSansPas = calcDifference((a-step),b,x,y)
		
		if actualSum > SommeAvecPas:
			#On ajoute le pas a "a"
			a = round((a+step),1)
		elif actualSum > SommeSansPas:
			#on retire le pas a "a"
			a = round((a-step),1)

		actualSum = calcDifference(a,b,x,y)
		SommeAvecPas = calcDifference(a, (b+step) ,x,y)
		SommeSansPas = calcDifference(a, (b-step) ,x,y)

		if actualSum > SommeAvecPas :
			#On ajoute le pas a "b"
			b = round((b+step),1)
		elif actualSum > SommeSansPas :
			#on retire le pas a "b"
			b = round((b-step),1)
		somme = CalculeSomme( a , b , x )
		findBis = compare(somme, y)

	#On reprend un nombre aléatoire pour tester 
	index = NombreAleatoire()
	x = BaseDeConnaissance[ str(index) ]["x"]
	y = BaseDeConnaissance[ str(index) ]["y"]
	somme = CalculeSomme( a,b,x )
	find = compare(somme, y)
	if find == 0 :
		# reset findBis to restart the search for the value of each pod
		findBis = 0

#Résulta
Resulta = "La fonction pour généré les 10000 points de la base de donnée était  " + str(a) + "x"
if b >= 0 :
	Resulta += "+"
Resulta += str(b) + "\n"
print(Resulta)
print("La fonction a été trouvée grace a :", iteration," points dans la base")