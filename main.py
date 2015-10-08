#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import * 
'''
TP n°2 d'Algorithmes et Complexité
"Diviser pour régner"

Matthieu CARON
Armand BOUR

'''


def fusion(Liste1,Liste2):
    '''
    Fusion de lignes de toits
    '''
    res = []
    x1 = 0
    x2 = 0
    hauteur1 = -1 # Valeur impossible
    hauteur2 = -1 # Valeur impossible
    ligneDessus = -1 # Valeur impossible qui sera plus tard soit 1 soit 2
    # Première fois on dois ajouter le premier point
    if Liste1[0][0] < Liste2[0][0] :
        res.append(Liste1[0])
        hauteur1 = Liste1[0][1]
        ligneDessus = 1
        x1 = x1 + 1
    else :
        res.append(Liste2[0])
        hauteur2 = Liste2[0][1]
        ligneDessus = 2
        x2 = x2 + 1
    while (x1 < len(Liste1) and x2 < len(Liste2)) :
        # On doit choisir un des deux éléments de la liste
        # Donc celui avec la plus petite abscisse
        if(Liste1[x1][0] < Liste2[x2][0]) :
            # On sélectionne l'élément de Liste1[x1]
            if hauteur2 > Liste1[x1][1] :
                if ligneDessus == 2 :
                    hauteur1 = Liste1[x1][1]
                else :
                    res.append((Liste1[x1][0],hauteur2))
                    hauteur1 = Liste1[x1][1]
                    ligneDessus = 1
                x1 = x1 + 1
            else :
                res.append(Liste1[x1])
                hauteur1 = Liste1[x1][1]
                ligneDessus = 1
                x1 = x1 + 1
        else :
            # On sélectionne l'élément Liste2[x2]
            if hauteur1 > Liste2[x2][1] :
                if ligneDessus == 1:
                    hauteur2 = Liste2[x2][1]
                else :
                    res.append( (Liste2[x2][0], hauteur1) )
                    hauteur2 = Liste2[x2][1]
                    ligneDessus = 2
                x2 = x2 + 1
            else :
                res.append(Liste2[x2])
                hauteur2 = Liste2[x2][1]
                ligneDessus = 2
                x2 = x2 + 1
    # A partir d'ici on a probablement une des deux listes qui n'a pas été entièrement parcourue
    while x1 < len(Liste1):
        res.append(Liste1[x1])
        x1 = x1 + 1
    while x2 < len(Liste2) :
        res.append(Liste2[x2])
        x2 = x2 + 1
    return res


# #script de test
# L1 = [(1,10),(5,6),(8,0),(10,8),(12,0)]
# L2 = [(2,12),(7,0),(9,4),(11,2),(14,0)]

# print L1
# print L2

# print fusion(L1,L2)

def creationLigne(listeBatiments,debut,fin) :
    '''
        Première version de création de ligne, utilisant la stratégie 
        diviser pour régner. 
        Version récursive non terminale
    '''
    # L'idée de diviser pour régner :
    # Découper le problème en sous-problèmes pour que celui-ci soit plus simple à résoudre
    # Il est simple de créer un ligne de toit à partir d'un seul bâtiment 
    # Mais aussi si on a pas de bâtiment : ligne vide
    #if listeBatiments == [] :
    if debut > fin :
        return []
    elif debut == fin :
        (a,b,c) = listeBatiments[debut]
        return [(a,b),(c,0)] 
    else :
        m = (debut + fin + 1) / 2 
        return fusion(creationLigne(listeBatiments,debut,m-1),  creationLigne(listeBatiments,m,fin))

# #script de test
# listeBatiments = [(1,11,5),(3,13,9),(3,6,7),(12,7,16),(16,3,25),(19,18,22)]
# print listeBatiments
# print creationLigne(listeBatiments,0,len(listeBatiments)-1)


def randomBatiment(maxLong,maxHaut) :
    c = randint(0,maxLong)
    b = randint(1,maxHaut)
    a = randint(0,c)
    return (a,b,c)

def generateRandomListBuilding(maxLong,maxHaut,nbBuilding) :
    res = []
    for i in xrange(0,nbBuilding):
        res.append(randomBatiment(maxLong,maxHaut))
    return res


# listeBatimentsAlea100 = generateRandomListBuilding(1000,1000,100)
# print listeBatimentsAlea100
# print creationLigne(listeBatimentsAlea100,0,99)

def generateString(ligneToits) :
    chaine = ""
    for (a,b) in ligneToits :
        chaine = chaine + str(a) + "," + str(b) + " "
    return chaine


def svgBatiment(batiment) :
    (x1,h,x2)=batiment
    width = x2 - x1
    return """<rect x =\""""+str(x1)+"""\" y ="0" width =\""""+str(width)+"""\" height=\""""+ str(h) +"""\" transform=" scale(5,-5) " /> \n"""

def generateSVG(listeBatiments,filename) :
    ligneToits = creationLigne(listeBatiments,0,len(listeBatiments)-1)
    chaine = """<svg xmlns="http://www.w3.org/2000/svg" width="300" height="200" viewBox="-10 -150 200 150">\n"""
    for batiment in listeBatiments :
        chaine = chaine + svgBatiment(batiment)
    chaine = chaine + """<polyline points=\""""+ generateString(ligneToits)+""" " stroke="blue" stroke-width="1" fill="none" transform="scale(5,-5)"/></svg>"""
    fichier = open(filename,'w')
    fichier.write(chaine)
    fichier.close()


listeBatiments = [(1,11,5),(3,13,9),(3,6,7),(12,7,16),(16,3,25),(19,18,22)]

generateSVG(listeBatiments,"ligne.svg")

'''
Decomentez pour tester
'''
# listeBatimentsAlea100 = generateRandomListBuilding(1000,1000,100)
# print "Voici la liste de batiments aléatoires de taille 100"
# print listeBatimentsAlea100
# print "Voici sa ligne de toits"
# print creationLigne(listeBatimentsAlea100,0,99)