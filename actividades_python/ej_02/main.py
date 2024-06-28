from gpiozero import RGBLED
from time import sleep 

aca declaro los pines 
ledquique = RGBLED(13,16,26)

aca declaro las funcionesx 
def titilatodo():
    ledquique.color = (1,1,1)
    sleep(0.01)
    ledquique.color = (0,0,0)

def titilaGB():
    ledquique.color = (0,1,1)
    sleep(0.01)
    ledquique.color = (0,0,0)

def titilaG():
    ledquique.color = (0,1,0)
    sleep(0.01)
    ledquique.color = (0,0,0)

aca declaro al bucle 
while True:
    titilatodo()
    sleep(0.25)
    titilaG()
    sleep(0.25)
    titilaGB()
    sleep(0.25)
    titilaG()
    sleep(0.25)
