import pygame
from niveaux import*

pygame.init()
pygame.mixer.init()
sounds = {
        'lvl1': pygame.mixer.Sound("jeu/assets/lvl1.ogg"),
}

def musique():
    'Musique à jouer pour Pygame'
    #générer la fenêtre.
    pygame.display.set_caption("Musiques jeu du pendu")
    pygame.display.set_mode((500,300))
    
    #Boucle qui permet de laisser allumé la fenêtre tant que running est vrai.
    Running = True
    
    while Running:
        
        #si le joueur ferme la fenêtre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
                pygame.quit()
                pygame.mixer.quit()
            if event.type == pygame.VIDEOEXPOSE and event.type != pygame.QUIT:
                pygame.mixer.music.load("jeu/assets/lvl1.ogg")
                pygame.mixer.music.play(-1)
            
    
niv = niveaux()
if niv == "1":
    musique()