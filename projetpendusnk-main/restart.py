#définir la fonction recommencer
def recommencer():
    recommencer = True
    #recommencer est vrai 
    while recommencer:
        choix=input("Veux tu rejouer ?")
        #demande a l'utilisateur si il veut rejouer
        if choix not in('yes','oui','ouais','ok'):
            #si le mot qu'il a donné n'est pas dans cette liste
            recommencer=False
            #alors ne pas recommencer
print(recommencer())

    
