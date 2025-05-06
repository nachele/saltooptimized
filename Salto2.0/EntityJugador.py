
from Entity import *
from Controles import *
class Jugador(Entity):
    def __init__(self, imagen,posX,posY,speed,transX,transY):
        super().__init__(imagen,posX,posY,transX,transY)
        self.speed = speed
        self.saltandoArriba = False
        self.saltandoAbajo = False
        self.jumpofset = 400
        self.distanciaSalto = 0
        self.ancho = transX
        self.alto = transY
        self.saltando = False
        self.chocandoPorDebajo = False
        self.chocandoPorArriba = False
        self.chocandoPorDerecha = False
        self.chocandoPorIzquierda = False
        self.callendodelChoque = False
    

    def movimiento(self, controles):   
        if(controles.W == True):
            pass           # self.y -= self.speed
        if(controles.A == True):
            self.x  -= self.speed
            
        if(controles.S == True):
            pass
          #  self.y += self.speed

        if(controles.D == True):
            self.x += self.speed
        # espacio
        if(controles.SP == True):
            self.saltando = True

        if(self.saltando == True):
            #si no esta ni saltando hacia arriba ni hacia abajo guarda la distancia hacia arriba a saltar
            if(self.saltandoArriba == False and self.saltandoAbajo == False and self.callendodelChoque == False):
                self.distanciaSalto = self.y - self.jumpofset
                self.saltandoArriba = True
            #cuando esta saltando hacia arriba y ha llegado a la distancia de salto entonces sube asta la distancia de salto es negativo la speed para que suba
            if(self.saltandoArriba == True and self.saltandoAbajo == False and self.y > self.distanciaSalto):
                self.y -= self.speed
            #cuando ha llegado a la distancia de salto
            if(self.y <= self.distanciaSalto and self.saltandoAbajo == False):
                self.saltandoArriba = False
                self.saltandoAbajo = False
            #cuando esta arriba que ni sube ni baja vuelve a almacenar en la variable la distancia de vuelta 
            if( self.saltandoAbajo == False and  self.saltandoArriba == False and self.callendodelChoque == False):
                self.distanciaSalto = self.y + self.jumpofset
                self.saltandoAbajo = True
            #si esta callendo hacia abajo
            if(self.saltandoAbajo == True):
            #si la distancia salto es mayor que la y del muñeco hacia alli seguira moviendo
                if(self.distanciaSalto >= self.y):
                    self.y += self.speed
                else:  
                    self.saltandoArriba = False 
                    self.saltandoAbajo = False
                    self.saltando = False
            
                        