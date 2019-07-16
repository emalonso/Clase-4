from temporizador1 import Temporizador
from time import sleep
 
t = Temporizador()

t.iniciar([0,1,15])

while True:
    tiempo = t.mostrar_tiempo()
    print tiempo
    sleep(0.2)
    if tiempo == "00 : 00 : 00":
        break
    t.retroceder()
while True:
    tiempo = t.mostrar_tiempo()
    print tiempo
    sleep(0.2)
    if tiempo == "00 : 01 : 15":
        break
    t.avanzar()
