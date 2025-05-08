
class Colisiones:
    def __init__(self, jugador,bloque,screen):
        self.jugador = jugador
        self.bloque = bloque
        self.screen = screen
    def ColisionDetection(self):
        #if(self.jugador.y <= self.bloque.y + self.bloque.alto and self.jugador.y >= self.bloque.y + self.bloque.alto - 10):
           # print("chocando por debajo")
            borde = 20
            dentrodeobjeto = 4
            #choque con el bloque en x 
            if(self.jugador.y <= self.bloque.y + self.bloque.alto - 10 and self.jugador.y + self.jugador.alto >= self.bloque.y + 10):   
                if(self.jugador.x  + self.jugador.ancho >= self.bloque.x + dentrodeobjeto and self.jugador.x + self.jugador.ancho <= self.bloque.x + borde):
                    self.jugador.x -= self.jugador.speed
                    
                if(self.jugador.x <= self.bloque.x + self.bloque.ancho - dentrodeobjeto and self.jugador.x >= self.bloque.x + self.bloque.ancho - borde):
                    self.jugador.x += self.jugador.speed
                    
            
            #choque con el bloque en y
            if(self.jugador.x  + self.jugador.ancho >= self.bloque.x + dentrodeobjeto and self.jugador.x <= self.bloque.x + self.bloque.ancho - dentrodeobjeto):
                self.jugador.enPlataforma = True
                if(self.jugador.y <= self.bloque.y + self.bloque.alto - dentrodeobjeto and self.jugador.y >= self.bloque.y + self.bloque.alto - borde):
                    #chocando cabeza por debajo del bloque
                    self.jugador.y += self.jugador.speed 
                    self.jugador.choqueCabeza = True
                else:
                     self.jugador.choqueCabeza = False
            if(self.jugador.y + self.jugador.alto >= self.bloque.y + dentrodeobjeto + 20 and self.jugador.y + self.jugador.alto <= self.bloque.y  + borde + 20 and self.jugador.x  + self.jugador.ancho >= self.bloque.x + dentrodeobjeto and self.jugador.x <= self.bloque.x + self.bloque.ancho - dentrodeobjeto):
                    #chocando pies por encima del bloque
                self.jugador.enPlataforma = True
                self.jugador.choquePie = True

            else:
                self.jugador.enPlataforma = False
                self.jugador.choquePie = False
                
                    


