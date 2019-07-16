from unidadtiempo import UnidadTiempo
from temporizador import Temporizador

t=Temporizador(UnidadTiempo(23),UnidadTiempo(59),UnidadTiempo(59))
t.iniciar([1,10,5])

for i in range(1000):
    t.retroceder()
    print str(t.h.valor) + ":" + str (t.m.valor)+ ":" + str(t.s.valor)
    
