def niveaux():
    'Fonction permettant de return le niveau sélectionné.'
    liste_possibilites = ['1','2','3']
    #On explique les choix possibles.
    print("_____Niveaux______")
    print("Niveau 1 - entre 2 et 5 lettres.")
    print("Niveau 2 - entre 6 et 8 lettres.")
    print("Niveau 3 - entre 9 et 12 lettres.")
    #On créé une boucle qui s'exécute en forme de do while et qui permet de répéter la demande si l'utilisateur ne choisit pas
    #1,2 ou 3.
    while True:
        #On demande à l'utilisateur quel niveau il souhaite choisir & on incrémente sa réponse à la var niv.
        niv=input("Quel est le niveau ?")
        #On vérifie que la var niv fait bien partie de ce qui est demandé.
        for x in liste_possibilites:
            if niv == x:
                #Si on entre dans cette partie de la boucle c'est que la condition est vraie (donc qu'il a mis 1,2 ou 3).
                #On termine par renvoyer le niveau qu'il a choisi.
                return niv
        #Si le programme continue c'est qu'il a mal choisi, on l'éclaircit sur ce qu'il doit réécrire avant de revenir au début de la boucle.
        print("Merci de choisir entre le niveau 1 et 3.")