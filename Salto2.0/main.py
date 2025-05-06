
from Ventana import *;
from Entity import *;
from EntityJugador import *;
from Controles import *;
from Colisiones import *;
pygame.init()
#creando la ventana 
screen = Ventana(800,800)
jugador = Jugador("C:/Users/ignac/Desktop/saltooptimized-main/carpetaSprite/fantasma.png",0,600,4,50,50,15,0.5)
bloque = Entity("C:/Users/ignac/Desktop/saltooptimized-main/carpetaSprite/s.png",300,300,60,200)
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
    
    bloque.pintar(screen.screen)
    colisiones.ColisionDetection()
    jugador.salto()
    
    pygame.display.flip()

    # fill the screen with a color to wipe away anything from last frame
    clock.tick(120) # limits FPS to 60

pygame.quit()