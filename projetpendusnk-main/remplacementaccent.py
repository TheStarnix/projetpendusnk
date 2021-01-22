#programme changement accent
chaine = input("Quel mot? ")
accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â']
sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a']

for i in range(len(chaine)): #pour chaque carctère de la chaine
    chaine = chaine.replace(accent[i], sans_accent[i]) #on replace les mots sans accent

print(chaine.upper()) #on met en majuscules
