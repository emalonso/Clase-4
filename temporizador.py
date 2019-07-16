from unidadtiempo import UnidadTiempo
class Temporizador:
    def __init__(self,h,m,s):
        self.h = h 
        self.m = m
        self.s = s

    def iniciar (self, valor_usuario):
        self.h.iniciar (valor_usuario[0])
        self.m.iniciar (valor_usuario[1])
        self.s.iniciar (valor_usuario[2])
        

    def retroceder (self):
        self.s.retroceder()
        if self.s.valor==self.s.tope:
            self.m.retroceder()
            if self.m.valor==self.m.tope:
                self.h.retroceder()
                

    def avanzar (self):
        self.s.avanzar()
        if self.s.valor==0:
            self.m.avanzar()
            if self.m.valor==0:
                self.h.avanzar()
                
    def reiniciar (self,valor_usuario):
        self.h.reiniciar  (valor_usuario[0])
        self.m.reiniciar (valor_usuario[1])
        self.s.reiniciar (valor_usuario[2])
        
