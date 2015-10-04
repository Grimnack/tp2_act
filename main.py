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
    #premiere fois on dois ajouter le premier point
    if Liste1[0][0] < Liste2[0][0] :
        res.append(Liste1[0][0])
        hauteur1 = Liste1[0][1]
        x1++
    else :
        res.append(Liste2[0][0])
        hauteur2 = Liste2[0][1]
        x2++
    while (x1<len(Liste1) && x2<len(Liste2)) :
        #on doit choisir un des deux éléments de la liste
        #donc celui avec le plus petit abscisse
        if(Liste1[x1][0] < Liste2[x2][0]) :
            #on selectionne l'element de Liste1[x1]
            if hauteur2 > Liste1[x1][1] :
                res.append( (Liste1[x1][0], hauteur2) )
                x1++
            else :
                res.append(Liste1[x1])
                hauteur1 = Liste1[x1][1]
                x1++
        else :
            #on selectionne l'element Liste2[x2]
            if hauteur1 > Liste2[x2][1] :
                res.append( (Liste2[x2][0], hauteur1) )
                x2++
            else :
                res.append(Liste2[x2])
                hauteur2 = Liste2[x2][1]
                x2++
    #A partir d'ici on a probablement une des deux liste qui n'a pas été entièrement parcourue

