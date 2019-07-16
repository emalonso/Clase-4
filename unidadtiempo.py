class UnidadTiempo:
    def __init__(self,tope):
        self.tope=tope
        self.valor=0

    def iniciar (self,valor):
        self.valor= valor

    def retroceder (self):
        self.valor-=1
        if self.valor < 0:
            self.valor=self.tope

    def reiniciar (self,valor):
         self.valor= valor

    def avanzar (self):
        self.valor+=1
        if self.valor > self.tope:
            self.valor=0
