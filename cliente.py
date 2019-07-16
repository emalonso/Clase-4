from unidadtiempo import UnidadTiempo
from temporizador import Temporizador

t=Temporizador(UnidadTiempo(23),UnidadTiempo(59),UnidadTiempo(59))
t.iniciar([0,10,5])

for i in range(605):
    t.retroceder()
    print str(t.h.valor) + ":" + str (t.m.valor)+ ":" + str(t.s.valor)
    
for i in range(605):
    t.avanzar()
    print str(t.h.valor) + ":" + str (t.m.valor)+ ":" + str(t.s.valor)
