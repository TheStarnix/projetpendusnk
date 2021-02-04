import pygame
from niveaux import*

#On initialise les librairies.
pygame.init()
pygame.mixer.init()
#On répertorie les différentes musiques.
#Deux musiques disponibles pour tester le programme: "jeu/assets/lvl1.ogg" et "jeu/assets/lvl2.ogg".

def musique():
    'Musique à jouer pour Pygame'
    #générer la fenêtre.
    pygame.display.set_caption("Fenêtre pour tester une musique")
    pygame.display.set_mode((500,300))
    
    #Boucle qui permet de laisser allumé la fenêtre tant que running est vrai.
    Running = True
    
    while Running:
        
        #Evénements qui se déclenchent si le joueur interragit avec la fenêtre:
        for event in pygame.event.get():
            #Si le joueur quitte, les instructions sont lancées afin de fermer le programme.
            if event.type == pygame.QUIT:
                Running = False
                pygame.mixer.quit()
                pygame.quit()
            if event.type != pygame.QUIT:
                #Si la fenêtre n'est pas fermée, on propose à la personne d'ajouter une musique.
                choix=input("Hey ! Quelle musique veux-tu ajouter ? Envoies le lien de celle-ci.")
                #On récupère son choix et on envoie la variable à la fonction en question.
                envoyer_musique(False, choix, pygame.event.get())
                #On propose à la personne de relancer.
                while choix != "N":
                    choix=input("Veux-tu ajouter une autre musique ? Si oui, met le lien ici. Si tu ne veux pas, écris 'N'.")
                    #Si le joueur ne veut pas relancer, le programme s'éteint.
                    if choix == "N":
                        pygame.mixer.quit()
                        pygame.quit()
                        exit()
                        break;
                    else:
                        #On lance la musique demandée.
                        envoyer_musique(True, choix, pygame.event.get())
             
def envoyer_musique(musique_en_cours, choix, event_type):
    'Fonction permettant de jouer une musique.'
    #Si le joueur ouvre la fenêtre & qu'il l'a toujours, la musique se lance.
    if musique_en_cours == True:
        #On stoppe l'ancienne musique.
        pygame.mixer.music.stop()
    pygame.mixer.music.load(choix)
    #On relance automatiquement la musique.
    pygame.mixer.music.play(-1)
        
musique()
