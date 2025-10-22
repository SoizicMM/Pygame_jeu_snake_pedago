#### ETAPE1 ###
import pygame, sys
from pygame.locals import QUIT
#### ETAPE6 ###
import random
### BONUS ###
import os

#### ETAPE1 ###
pygame.init()
### BONUS ###
# Initialiser le mixer
pygame.mixer.init()

#### ETAPE1 ###
largeur, hauteur = 800, 500
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('NOKIA 3210')

#### ETAPE1 ###
# Définition des couleurs (la fenêtre, le serpent et le pion à manger )
bleu = "#D1FFFB"
orange = "#FFC980"
rose = "#EB6BEF"

#### ETAPE2 ###
# Dimensions des cellules et nombre de cellules
cellule = 20
nb_cellule_x = largeur // cellule
nb_cellule_y = hauteur // cellule


#### ETAPE3 ###
# Horloge pour contrôler la vitesse du jeu
horloge = pygame.time.Clock()

### ETAPE5 ###
# Définir des déplacements du serpent
# Ex : si il va en haut 
# alors il va se déplacer de 0px sur l'axe X, et de -1 sur l'axe Y)
haut = (0, -1)
bas = (0, 1)
gauche = (-1, 0)
droite = (1, 0)

### BONUS ###
# Charger les fichiers audios
son_jeu = pygame.mixer.Sound(os.path.join('melodie.wav'))

### ETAPE4 ###
# Methode pour placer le serpent en début du jeu
def depart_serpent():
    # Jouer le son
    son_jeu.play()
    # Initialiser le serpent avec trois segments
    snake = [(9, 5), (8, 5), (7, 5)]
    # Initialiser la direction du serpent
    direction = droite
    # Initialiser le pion à manger
    pion = (random.randint(0, nb_cellule_x - 1), random.randint(0, nb_cellule_y - 1))



    #### ETAPE1 ###
    while True:  
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            ### ETAPE5 ###
            if event.type == pygame.KEYDOWN:
                # Vérifie si la touche flèche haut est enfoncée 
                # et que la direction actuelle n'est pas bas
                if event.key == pygame.K_UP and direction != bas:
                    # Changer la direction du serpent vers le haut
                    direction = haut
                elif event.key == pygame.K_DOWN and direction != haut:
                    direction = bas
                elif event.key == pygame.K_LEFT and direction != droite:
                    direction = gauche
                elif event.key == pygame.K_RIGHT and direction != gauche:
                    direction = droite

        ### ETAPE4 ###
        # Déplacement du serpent 
        # Position actuelle de la tete du serpent
        deplacement = snake[0]
        # Calculer les nouvelles coordonnées de la tête en ajoutant sa direction
        x, y = deplacement[0] + direction[0], deplacement[1] + direction[1]
        # Insère les nouvelles données et déplace la tête du serpent vers la nouvelle position
        snake.insert(0, (x, y))

        ### ETAPE7 ###
        # Gestion des collisions sur les bords
        if (x < 0 or x >= nb_cellule_x) or (y < 0 or y >= nb_cellule_y) or (snake.count((x, y)) > 1):
            ### BONUS ###
            # Stopper le son
            son_jeu.stop()
            depart_serpent()


        ### ETAPE6 ###
        # Vérifier si la tête du serpent est sur la même position que le pion
        if (x, y) == pion:
            # Si le serpent a mangé le pion, générer un nouveau pion à une position aléatoire
            pion = (random.randint(0, nb_cellule_x - 1), random.randint(0, nb_cellule_y - 1))
        else:
            # Si le serpent n'a pas mangé le pion, supprimer le dernier segment du serpent
            # (Cela garde la longueur du serpent constante sauf lorsqu'il mange!)
            snake.pop()



        #### ETAPE1 ###
        # Affiche la fenêtre avec notre couleur de fond
        fenetre.fill(bleu)

        ### ETAPE5 ###
        # Dessiner le serpent
        for segment in snake:
            pygame.draw.rect(fenetre, orange, (segment[0] * cellule, segment[1] * cellule, cellule, cellule))

        ### ETAPE6 ###
        # Dessiner le pion
        pygame.draw.rect(fenetre, rose, (pion[0] * cellule, pion[1] * cellule, cellule, cellule))



        #### ETAPE3 ###
        # Contrôler la vitesse du jeu
        horloge.tick(5)


        #### ETAPE1 ###
        pygame.display.update()


#### ETAPE4 ###
# Lancer le jeu
depart_serpent()