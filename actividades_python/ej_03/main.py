from gpiozero import RGBLED, Buzzer

#declaro los pines 
ledquique = RGBLED(13,19,26)
bz = Buzzer(22)

#creo el bucle para el funcionamiento
while True: 
    mensaje = input("ingrese comando: ")
    if mensaje == 'buzz on':
        bz.on()
    if mensaje == 'buzz off':
        bz.off()
    if mensaje == 'rgb red':
        ledquique.color = (1,0,0)
    if mensaje == 'rgb green':
        ledquique.color = (0,1,0)
    if mensaje == 'rgb blue':
        ledquique.color = (0,0,1)
    if mensaje == 'quit':
        break
