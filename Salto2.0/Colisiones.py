
class Colisiones:
    def __init__(self, jugador,bloque,screen):
        self.jugador = jugador
        self.bloque = bloque
        self.screen = screen
    def ColisionDetection(self):
        if(self.jugador.x + self.jugador.ancho >= self.bloque.x and self.jugador.x <= self.bloque.x + self.bloque.ancho):
            if(self.jugador.y >= self.bloque.y and self.jugador.y <= self.bloque.y + self.bloque.alto):
                if((self.bloque.x - self.jugador.x) > 0 and self.jugador.callendodelChoque == False):
                    self.jugador.x -= self.jugador.speed
                if((self.bloque.x - self.jugador.x) < 0):
                    self.jugador.x += self.jugador.speed
                print("posicion del jugador en y " + str(self.jugador.y) + "posicion del bloque en y" + str(self.bloque.y))

                if(self.jugador.y < self.bloque.y + self.bloque.alto):
                    self.jugador.saltandoArriba = False
                    self.jugador.saltandoAbajo = True
                    self.jugador.chocandoPorDebajo = True
        if(self.jugador.chocandoPorDebajo == True):
            if(self.jugador.y < self.screen.alto - self.jugador.alto):
                self.jugador.y += self.jugador.speed
                self.jugador.callendodelChoque = True
            else:
                self.jugador.saltandoAbajo = False
                self.jugador.chocandoPorDebajo = False
                self.jugador.callendodelChoque = False

                
                    
        
        
            



