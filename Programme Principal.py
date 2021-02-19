import pygame
import random

# Déclaration des variables globales à l'extérieur du code de base.
ListeMot = []
mot2 = ""
ListeMot2 = []
MotsTrouve = []
vie = 7
booleanRestart = True


def manage_level():
    """Fonction gérant le système de niveau."""
    liste_possibilites = ['1', '2', '3']
    print("_____Niveaux______")
    print("Niveau 1 - entre 2 et 5 lettres.")
    print("Niveau 2 - entre 6 et 8 lettres.")
    print("Niveau 3 - entre 9 et 12 lettres.")
    print("Pour chaque niveau vous aurez 7 chances.")

    while True:
        # On demande à l'utilisateur quel niveau il souhaite choisir & on incrémente sa réponse à la var niv.
        niv = input("Quel est le niveau ?")
        # On vérifie que la var niv fait bien parti de ce qui est demandé.
        for x in liste_possibilites:
            if niv == x:
                # Si on entre dans cette partie de la boucle c'est que la condition est vraie (donc qu'il a mit 1,
                # 2 ou 3). On termine par renvoyer le niveau qu'il a choisit.
                return niv
        # Si le programme continue c'est qu'il a mal choisit, on l'éclaircit sur ce qu'il doit réecrire avant de
        # revenir au début de la boucle.
        print("Merci de choisir entre le niveau 1 et 3.")


def words_level(niv, count):
    """Fonction qui relance un mot si le nombre de lettres par niveau n"est pas respecté."""
    # On cherche le niveau qu'il a choisi et on vérifie s'il y a bien le nombre de lettres demandé.
    if niv == 1:
        if 2 < count < 6:
            return True
        else:
            return False
    elif niv == 2:
        if 6 < count < 9:
            return True
        else:
            return False
    else:
        if 9 < count < 12:
            return True
        else:
            return False


def file():
    # Ouvrir le fichier dictionnaire contenant 22 740 mots (un mot par ligne).
    f = open("dictionnaire.txt", mode="r", encoding="utf-8")
    # Tirer au sort une ligne de façon aléatoire parmi 0 - 22 740 lignes.
    nombreAleatoire = random.randint(0, 22740)
    # On définit la variable qui va calculer à combien de ligne il en est.
    nombreLigne = 0
    # Il va continuer tant que ligne =/= nombre tiré au hasard.
    while True:
        # Il va lire la ligne et définir la variable line qui sera le mot de la ligne.
        line = f.readline()
        nombreLigne = nombreLigne + 1
        if nombreLigne == nombreAleatoire:
            # Quand tout est fini, il arrêtera de lire le fichier.
            f.close()
            # programme changement accent
            chaine = []
            for x in line:
                chaine.append(x)
            accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
            sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']
            for i in range(len(chaine)):  # pour chaque carctère de la chaine
                for x in accent:
                    if chaine[i] == str(x):
                        chaine[i] = sans_accent[accent.index(x)]
            chaine2 = ""
            for x in chaine:
                chaine2 = chaine2 + x
            # On return le résultat.
            return chaine2.upper()


def count(mot):
    # demande a l'utilisateur de rentrer un mot
    calcul = -1
    # il prend calcul égal à -1 car en mettant à 0, il aurait un total de lettres avec 1 de moins.
    for x in range(len(mot)):
        # il fait pour une valeur dans mot:
        calcul = calcul + 1
        # il rajoutera +1 à chaque lettres
    return calcul
    # retourner la fonction


def remplacement_tirets(mot):
    """Fonction permettant de remplacer chaque lettre d"un mot par un tiret."""
    # On définit une nouvelle variable calcul qui permettra de compter chaque lettre.
    calcul = -1
    # Boucle qui permet de compter chaque lettre dans un mot.
    for x in range(len(mot)):
        # Il incrémente 1 à chaque fois qu'il trouve une nouvelle lettre.
        calcul = calcul + 1
    return "_ " * calcul
    # On multiplie un tiret par le nombre de fois qu'il avait trouvé de lettres dans un mot.


def tracer_pendu(vie):
    """Fonction qui permet d"écrire dans la console le bonhomme en fonction de la vie."""
    # Je n'ai pas trouvé de moyen plus simple pour faire le pendu sous forme de console.
    if vie == 0:
        print(" _______")
        print(" |     |")
        print(" |     O")
        print(" |    -I-")
        print(" |    ┘ └")
    elif vie == 1:
        print(" _______")
        print(" |     |")
        print(" |     O")
        print(" |    -I-")
        print(" |      ")
    elif vie == 2:
        print(" _______")
        print(" |     |")
        print(" |     O")
        print(" |      ")
        print(" |      ")
    elif vie == 3:
        print(" _______")
        print(" |     |")
        print(" |      ")
        print(" |      ")
        print(" |      ")
    elif vie == 4:
        print(" _______")
        print(" |      ")
        print(" |      ")
        print(" |      ")
        print(" |      ")
    elif vie == 5:
        print(" ___    ")
        print(" |      ")
        print(" |      ")
        print(" |      ")
        print(" |      ")
    elif vie == 6:
        print(" |      ")
        print(" |      ")
        print(" |      ")
        print(" |      ")
        print(" |      ")
    elif vie == 7:
        print("        ")
        print("        ")
        print("        ")
        print("        ")
        print("        ")


# On initialise les librairies.
pygame.init()
pygame.mixer.init()
# Boucle while pour le relancement de la partie
while booleanRestart is True:
    # Programme principal
    # On propose le niveau & on sélectionne le mot.
    niv = manage_level()
    mot = file()
    # On vérifie que le mot fasse bien la taille demandée.
    condition = words_level(int(niv), count(mot))
    while condition is False:
        mot = file()
        condition = words_level(int(niv), count(mot))
    # On récupère sous forme de chaîne de caractère le mot, l'attribuant à une seconde variable qui sera manipulée
    # par la suite.
    for x in mot:
        if not x.isspace():
            mot2 = mot2 + x
    print("(Débug) Mot à trouver:" + mot + str(count(mot)) + " lettres.")
    # On met créé deux listes distinctes. Une qui aura le mot en entier, l'autre qui aura des lettres qui
    # remplaceront les "_" mis au départ.
    for x in mot2:
        ListeMot.append(x)
    for x in ListeMot:
        ListeMot2.append(x)
    # On créé une boucle qui se repète tant que le joueur n'a pas trouvé le mot ou a encore de la vie (7).
    hasBeenFound = False
    while hasBeenFound is False:
        hasBeenFound2 = False
        # On vérifie si le joueur n'a pas trouvé le mot.
        for x in ListeMot2:
            if x == "_":
                hasBeenFound = True
            else:
                hasBeenFound = False
        # S'il l'a trouvé, c'est gagné
        if hasBeenFound is True:
            break
        # S'il n'a plus de vie, c'est perdu
        elif vie == 0:
            print("Perdu !")
            break
        # Sinon, on continue
        else:
            print("▬▬▬▬▬▬▬▬▬๑۩۞۩๑▬▬▬▬▬▬▬▬▬")
            choix = input("Quelle lettre?")
            choix = choix.upper()
            for x in ListeMot2:
                # On vérifie si la lettre donnée correspond à une lettre du mot.
                if choix == x:
                    ListeMot2[ListeMot2.index(x)] = "_"
                    MotsTrouve.append(choix)
                    hasBeenFound2 = True
        # Si ce n'est pas le cas, on lui retire une vie
        if hasBeenFound2 is False:
            print("Mauvais choix !")
            vie -= 1
        # puis on dessine le pendu.
        tracer_pendu(vie)
        mot2 = ""
        # On manipule la seconde liste afin de lui affiche les lettres qu'il a trouvé sans donner le mot entier.
        for x in range(len(ListeMot2)):
            if str(ListeMot2[x]) == "_":
                mot2 = mot2 + ListeMot[x]
            else:
                mot2 = mot2 + "_"
        print("Vie: " + str(vie))
        print("Mot: " + mot2)
    # S'il a trouvé ou perdu, on lui propose de recommencer.
    if hasBeenFound is True:
        print("Félicitations, vous avez réussi !")
    restart = ""
    while restart.upper() != "O" and restart.upper() != "N":
        restart = str(input("Voulez-vous recommencer ? O/N"))
    if restart.upper() == "O":
        booleanRestart = True
    else:
        booleanRestart = False
