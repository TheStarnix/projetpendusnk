def remplacement_tirets():
    'Fonction permettant de remplacer chaque lettre dun mot par un tiret.'
    #On demande à l'utilisateur de rentrer un mot.
    mot=input("Donnes un mot:")
    #On définit une nouvelle variable calcul qui permettra de compter chaque lettre.
    calcul=0
    #Boucle qui permet de compter chaque lettre dans un mot.
    for x in mot:
        #Il incrémente 1 à chaque fois qu'il trouve une nouvelle lettre.
        calcul=calcul+1
    return calcul
    #Il renvoie la var calcul qui permettra de recevoir le résultat.
print("_ " * remplacement_tirets())
#On multiplie un tiret par le nombre de fois qu'il avait trouvé de lettres dans un mot.
