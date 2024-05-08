from gpiozero import LED, Button
from signal import pause

led = LED(26) #declaro pin 26 para enencer el led
button = Button(18) #declaro pin 18 como entrada

button.when_pressed = led.on #declaro funcion on como encendido 
button.when_released = led.off #declaro funcion off como apagado

pause() #declaro pause para  pausar el programa
