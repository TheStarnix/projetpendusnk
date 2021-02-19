import pygame
import random

def manage_level():
    'Fonction gérant le système de niveau.'
    liste_possibilites = ['1','2','3']
    print("_____Niveaux______")
    print("Niveau 1 - entre 2 et 5 lettres.")
    print("Niveau 2 - entre 6 et 8 lettres.")
    print("Niveau 3 - entre 9 et 12 lettres.")
    
    while True:
        #On demande à l'utilisateur quel niveau il souhaite choisir & on incrémente sa réponse à la var niv.
        niv=input("Quel est le niveau ?")
        #On vérifie que la var niv fait bien parti de ce qui est demandé.
        for x in liste_possibilites:
            if niv == x:
                #Si on entre dans cette partie de la boucle c'est que la condition est vraie (donc qu'il a mit 1,2 ou 3).
                #On termine par renvoyer le niveau qu'il a choisit.
                return niv
        #Si le programme continue c'est qu'il a mal choisit, on l'éclaircit sur ce qu'il doit réecrire avant de revenir au début de la boucle.
        print("Merci de choisir entre le niveau 1 et 3.")

def words_level(niv, count, mot):
    'Fonction qui relance un mot si le nombre de lettres par niveau n"est pas respecté.'
    #On cherche le niveau qu'il a choisi et on vérifie s'il y a bien le nombre de lettres demandé.
    if niv == 1:
        if count>2 and count<6:
            return True
        else:
            return False
    elif niv == 2:
        if count>6 and count<9:
            return True
        else:
            return False
    else:
        if count>9 and count<12:
            return True
        else:
            return False

def file():
    #Ouvrir le fichier dictionnaire contenant 22 740 mots (un mot par ligne).
    f = open("dictionnaire.txt", mode="r", encoding="utf-8")
    #Tirer au sort une ligne de façon aléatoire parmi 0 - 22 740 lignes.
    nombreAleatoire = random.randint(0, 22740)
    #On définit la variable qui va calculer à combien de ligne il en est.
    nombreLigne = 0
    #Il va continuer tant que ligne =/= nombre tiré au hasard.
    while(True):
        #Il va lire la ligne et définir la variable line qui sera le mot de la ligne.
        line = f.readline()
        nombreLigne = nombreLigne + 1
        if nombreLigne == nombreAleatoire:
            
            #Il va renvoyer le mot et casser la boucle.
            return line
            break
    #Quand tout est fini, il arrêtera de lire le fichier.
    f.close

    #Instanciation de la fonction permettant d'ouvrir le fichier et de return un mot aléatoire.
    chaine = fichier()
    #programme changement accent
    accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
    for i in range(len(chaine)): #pour chaque carctère de la chaine
        chaine = chaine.replace(accent[i], sans_accent[i]) #on replace les mots sans accent
        
    #On return le résultat.
    return chaîne.upper()

def count(mot):
    #demande a l'utilisateur de rentrer un mot
    calcul=-1
    #il prend calcul égal à -1 car en mettant à 0, il aurait un total de lettres avec 1 de moins.
    for x in mot:
        #il fait pour une valeur dans mot:
        calcul=calcul+1
        #il rajoutera +1 à chaque lettres
    return calcul
    #retourner la fonction

def remplacement_tirets(mot):
    'Fonction permettant de remplacer chaque lettre d"un mot par un tiret.'
    #On définit une nouvelle variable calcul qui permettra de compter chaque lettre.
    calcul=-1
    #Boucle qui permet de compter chaque lettre dans un mot.
    for x in mot:
        #Il incrémente 1 à chaque fois qu'il trouve une nouvelle lettre.
        calcul=calcul+1
    return ("_ " * calcul)
    #Il renvoie la var calcul qui permettra de recevoir le résultat.
    print()
    #On multiplie un tiret par le nombre de fois qu'il avait trouvé de lettres dans un mot.


#On initialise les librairies.
pygame.init()
pygame.mixer.init()
    
#Programme principal
niv = manage_level()
mot = file()
condition = words_level(int(niv), count(mot), mot)
while condition == False:
    mot = file()
    condition = words_level(int(niv), count(mot), mot)
print("Mot à trouver:" + mot + str(count(mot)) + " lettres.")
print(remplacement_tirets(mot))
