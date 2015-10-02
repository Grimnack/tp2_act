'''
Tp diviser pour regner de Matthieu Caron et Armand Bour


'''

'''
   Fusion de lignes de toit
   Premier point c est simple on prend le plus petit abscisse.
   En suite on cherche à monter toujours plus haut,
   On compare donc le y avec le y du dernier point de la 

'''
def fusion(Liste1,Liste2,res):
	#cas init
	if res == [] :
		
