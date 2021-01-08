import random

def fichier():
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

#On affiche le résultat.
print(chaine.upper())
