def recommencer():
    recommencer = True
    while recommencer:
        choix=input("Veux tu rejouer ?")
        if choix not in('yes','oui','ouais','ok'):
            recommencer=False
print(recommencer())

    