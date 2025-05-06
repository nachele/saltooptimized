
class Colisiones:
    def __init__(self, jugador,bloque,screen):
        self.jugador = jugador
        self.bloque = bloque
        self.screen = screen
    def ColisionDetection(self):
        #if(self.jugador.y <= self.bloque.y + self.bloque.alto and self.jugador.y >= self.bloque.y + self.bloque.alto - 10):
           # print("chocando por debajo")
            borde = 20
            dentrodeobjeto = 2
            if(self.jugador.y >= self.bloque.y and self.jugador.y <= self.bloque.y + self.bloque.alto or self.jugador.y + self.jugador.alto <= self.bloque.y + self.bloque.alto and self.jugador.y + self.jugador.alto >= self.bloque.y):
                 
                if(self.jugador.x  + self.jugador.ancho >= self.bloque.x + dentrodeobjeto and self.jugador.x + self.jugador.ancho <= self.bloque.x + borde):
                    #print("por la izquierda ")
                    self.jugador.x -= self.jugador.speed
                if(self.jugador.x <= self.bloque.x + self.bloque.ancho - dentrodeobjeto and self.jugador.x >= self.bloque.x + self.bloque.ancho - borde):
                    self.jugador.x += self.jugador.speed
                   # print("por la derecha")
            if(self.jugador.x >= self.bloque.x and self.jugador.x <= self.bloque.x + self.bloque.ancho or self.jugador.x + self.jugador.ancho <= self.bloque.x + self.bloque.ancho and self.jugador.x + self.jugador.ancho >= self.bloque.x): 
                
                if(self.jugador.y  + self.jugador.alto >= self.bloque.y + dentrodeobjeto and self.jugador.y + self.jugador.alto <= self.bloque.y + borde):
                    pass
                   # print("por arriba ")
                if(self.jugador.y <= self.bloque.y + self.bloque.alto - dentrodeobjeto and self.jugador.y >= self.bloque.y + self.bloque.alto - borde):
                    self.jugador.choqueCabeza = True
                  #  print("por debajo")
            
            
            



