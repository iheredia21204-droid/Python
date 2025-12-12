import pygame
import sys

# Inicialitzar pygame
pygame.init()

# Mides de la finestra
AMPLADA = 800
ALT = 600
pantalla = pygame.display.set_mode((AMPLADA, ALT))
pygame.display.set_caption("Arkanoid")

# Colors
NEGRO = (0, 0, 0)
BLANC = (255, 255, 255)

# Carregar imatges
# Substitueix els noms dels fitxers segons les teves imatges
barra_img = pygame.image.load("barra.png")
bola_img = pygame.image.load("bola.png")
bloc_img = pygame.image.load("bloc.png")

# Rectangles dels objectes
barra = barra_img.get_rect(midbottom=(AMPLADA//2, ALT-30))
bola = bola_img.get_rect(center=(AMPLADA//2, ALT-50))

# Velocitats
vel_bola = [5, -5]
vel_barra = 7

# Crear blocs
blocs = []
FILES = 5
COLUMNS = 10
for fila in range(FILES):
    for col in range(COLUMNS):
        bloc_rect = bloc_img.get_rect(topleft=(col*80 + 10, fila*30 + 10))
        blocs.append(bloc_rect)

# Control del joc
joc_actiu = False
reloi = pygame.time.Clock()

while True:
    pantalla.fill(NEGRO)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                joc_actiu = True

    # Mou la barra amb les fletxes
    tecles = pygame.key.get_pressed()
    if tecles[pygame.K_LEFT] and barra.left > 0:
        barra.x -= vel_barra
    if tecles[pygame.K_RIGHT] and barra.right < AMPLADA:
        barra.x += vel_barra

    # Mou la bola si el joc ha començat
    if joc_actiu:
        bola.x += vel_bola[0]
        bola.y += vel_bola[1]

        # Col·lisions amb les parets
        if bola.left <= 0 or bola.right >= AMPLADA:
            vel_bola[0] *= -1
        if bola.top <= 0:
            vel_bola[1] *= -1
        if bola.bottom >= ALT:
            print("Has perdut!")
            pygame.quit()
            sys.exit()

        # Col·lisió amb la barra
        if bola.colliderect(barra):
            vel_bola[1] *= -1

        # Col·lisió amb blocs
        for bloc in blocs[:]:
            if bola.colliderect(bloc):
                blocs.remove(bloc)
                vel_bola[1] *= -1
                break

    # Dibuixar blocs
    for bloc in blocs:
        pantalla.blit(bloc_img, bloc)

    # Dibuixar barra i bola
    pantalla.blit(barra_img, barra)
    pantalla.blit(bola_img, bola)

    pygame.display.flip()
    rello = pygame.time.Clock()
    rello.tick(60)  # 60 FPS
