#programme système de vie
mot = "yoyo" #choix du mot (à modifier)
vie = 7 #nombre de vies

for i in range(30): #possibiltés max de propositions (à modifier peut-être)
    lettredonnée = input("Quelle lettre? ") #demande de la lettre
    compteur = len(mot) #compteur est le moyen de savoir si toutes les lettres sont fausses il est donc égal au nombre de lettre du mot
    if vie==0:
        print("c'est la mort") #animation de mort
    for y in range(len(mot)): #pour chaque lettre du mot
        if lettredonnée==mot[y]:
            print("c'est bien") #si la lettre est égale à une du mot
        if lettredonnée!=mot[y]: #si c'est pas le cas 
            print("")
            compteur = compteur-1 #il y a donc une erreur donc on enlève 1 au compteur 
    if compteur==0: #truc pour enlever une vie
        vie=vie-1
        print("une vie en moins")