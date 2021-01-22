import pygame
from niveaux import*
#NECESSITE ABSOLUMENT niveaux.py !!

#On initialise les librairies.
pygame.init()
pygame.mixer.init()
#On répertorie les différentes musiques.
sounds = {
        '1': "jeu/assets/lvl1.ogg",
        '2': "jeu/assets/lvl2.ogg"
}
#On créé une variable qui servira à ne pas relancer la musique si celle-ci est déjà lancée.
musique_en_cours = False

def musique(musique_en_cours, lvl):
    'Musique à jouer pour Pygame'
    #générer la fenêtre.
    pygame.display.set_caption("Musiques jeu du pendu")
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
            #Si le joueur ouvre la fenêtre & qu'il l'a toujours, la musique se lance 1 fois.
            if event.type == pygame.VIDEOEXPOSE and event.type != pygame.QUIT:
                if musique_en_cours != True:
                    pygame.mixer.music.load(pygame.mixer.Sound(sounds[lvl]))
                    pygame.mixer.music.play(-1)
                    musique_en_cours = True
            
#On demande au joueur quel est le niveau qu'il souhaite
niv = niveaux()
#On lance le programme de musique qui change le son d'ambiance en fonction du niveau.
musique(musique_en_cours, niv)