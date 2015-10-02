def fusion(l1, l2):
    res = []

    # Cas terminaux
        # => Deux listes de longueur 1 => comparaison des deux éléments, et retour d'une liste triée
    # Sinon division de la liste en deux
    # Appels récursifs respectifs

    i = j = 0
    
    while i < len(l1) and j < len(l2):
        # Sélection du point à utiliser pour les comparaisons
        if l1[i][0] < l2[j][0]:
            point = l1[i]
            i++
        else:
            point = l2[j]
            j++

        # On vérifie si on a besoin de l'ajouter à la liste résultante

        # Si la liste résultante est vide, on ajoute le point (première itération)
        if not res:
            res.append(point)
        else:
        	if point[1]>res[-1][1]:
        		res.append(point)
        	else: #dans ce cas la le point est moins haut mais il faut sauvegarder sa hauteur
        		#ou bien on deduit le pont suivant pour le comparer
        		
