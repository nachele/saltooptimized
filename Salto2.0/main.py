
from Ventana import *;
from Entity import *;
from EntityJugador import *;
from Controles import *;
from Colisiones import *;
pygame.init()
#creando la ventana 
screen = Ventana(800,800)
jugador = Jugador("C:/Users/ignacio/Downloads/carpetaSprite/fantasma.png",0,600,5,50,50,25,1)
bloque = Entity("C:/Users/ignacio/Downloads/carpetaSprite/s.png",300,300,60,200)
colisiones = Colisiones(jugador,bloque,screen)
controles = Controles()
running = True
clock = pygame.time.Clock()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.screen.fill("white")
    controles.KeyDetection()
    jugador.pintar(screen.screen)
    jugador.movimiento(controles)
    jugador.salto()
    bloque.pintar(screen.screen)
    colisiones.ColisionDetection()

    pygame.display.flip()

    # fill the screen with a color to wipe away anything from last frame
    clock.tick(60)  # limits FPS to 60

pygame.quit()