#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Tp diviser pour regner de Matthieu Caron et Armand Bour


'''


def fusion(Liste1,Liste2):
    '''
    Fusion de lignes de toits
    '''
    res = []
    x1 = 0
    x2 = 0
    hauteur1 = -1 #valeur impossible
    hauteur2 = -1 #valeur impossible
    ligneDessus = -1 #valeur impossible qui sera plus tard soit 1 soit 2
    #premiere fois on dois ajouter le premier point
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
    while (x1<len(Liste1) and x2<len(Liste2)) :
        #on doit choisir un des deux éléments de la liste
        #donc celui avec le plus petit abscisse
        if(Liste1[x1][0] < Liste2[x2][0]) :
            #on selectionne l'element de Liste1[x1]
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
            #on selectionne l'element Liste2[x2]
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
    #A partir d'ici on a probablement une des deux liste qui n'a pas été entièrement parcourue
    while x1 <len(Liste1):
        res.append(Liste1[x1])
        x1 = x1 +1
    while x2 < len(Liste2) :
        res.append(Liste2[x2])
        x2 = x2 + 1
    return res


#script de test
L1 = [(1,10),(5,6),(8,0),(10,8),(12,0)]
L2 = [(2,12),(7,0),(9,4),(11,2),(14,0)]

print L1
print L2

print fusion(L1,L2)



