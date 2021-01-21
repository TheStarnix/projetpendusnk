#définition de la fonction: comptage
def comptage():
    #demande a l'utilisateur de rentrer un mot
    mot=input("Donnes un mot:")
    calcul=0
    #il prend calcul égal à 0 
    for x in mot:
        #il fait pour une valeur dans mot:
        calcul=calcul+1
        #il rajoutera +1 à chaque lettres
    return calcul
    #retourner la fonction
print("_ " * comptage())
#faire la fonction