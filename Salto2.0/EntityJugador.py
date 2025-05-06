
from Entity import *
from Controles import *
import time
class Jugador(Entity):
    def __init__(self, imagen,posX,posY,speed,transX,transY,fuerzaSalto,deceleracion):
        super().__init__(imagen,posX,posY,transX,transY)
        self.speed = speed

        self.saltandoArriba = False
        self.saltandoAbajo = False
        self.jumpofset = 500
        self.distanciaSalto = 0
        self.ancho = transX
        self.alto = transY
        self.saltando = False
        self.choque = False
        self.suelo = posY + transY
        self.fuerzaSaltoInicial = fuerzaSalto
        self.fuerzaSalto = fuerzaSalto #20
        self.deceleracion = deceleracion #1
        self.choqueCabeza = False

    def movimiento(self, controles):   
        if(controles.W == True):
           self.y -= self.speed
        if(controles.A == True):
            self.x  -= self.speed

        if(controles.S == True):
            self.y += self.speed

        if(controles.D == True):
            self.x += self.speed
        # espacio
        if(controles.SP == True):
            self.saltando = True
    def salto(self):
        if(self.saltando == True and self.choqueCabeza == False):
            self.y -= self.fuerzaSalto
            self.fuerzaSalto -= self.deceleracion
            if(self.fuerzaSalto < - self.fuerzaSaltoInicial ):
                self.fuerzaSalto = self.fuerzaSaltoInicial
                self.saltando = False
        if(self.choqueCabeza == True):
                self.saltando = False
                if(self.y + self.alto < self.suelo):
                    self.y += self.fuerzaSalto
                    self.fuerzaSalto + self.deceleracion
                elif(self.y + self.alto > self.suelo ):
                    self.y = self.suelo
                    self.choqueCabeza = False
                    self.saltando = False
                    self.fuerzaSalto = self.fuerzaSaltoInicial
                    
                

                 



       
            
                        