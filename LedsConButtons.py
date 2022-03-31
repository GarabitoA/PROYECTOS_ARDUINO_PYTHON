import keyboard
import serial,time #Importo libreria serial para leer datos del puerto serial
import pyfirmata
from pynput.keyboard import Listener #Listener va ser la funcion que va estar escuchando el teclado para ver que pulsamos nosotros
from tkinter import * #import tkinter as tk #Para botones en la interfaz

# PARA BOTONES EN LA INTERAZ DE PYTHON
placa = pyfirmata.Arduino("COM5")

# CREANDO FUNCIONES PARA BOTONES
def buttonA():
    print("Boton A pulsado")
    valor = int(lbl['text'])
    lbl["text"] = f"{valor + 1}"

    if valor % 2 != 0:
        placa.digital[12].write(1)
        print("Boton A pulsado dos veces - MANDANDO SEÑAL A LED ROJA 10 seg")
        time.sleep(10)
        placa.digital[12].write(0)
    else:
        placa.digital[12].write(0)



def buttonB():
    print("Boton B pulsado")
    valorB = int(lblB['text'])
    lblB["text"] = f"{valorB + 1}"

    if valorB % 2 != 0:
        placa.digital[8].write(1)
        print("Boton B pulsado dos veces - MANDANDO SEÑAL A LED VERDE 10 seg")
        time.sleep(10)
        placa.digital[8].write(0)
    else:
        placa.digital[8].write(0)

def buttonExit():
    quit()


"""

#comunicacion con puerto serial para mandar señal de python al puerto serial de arduino
arduino = serial.Serial("COM5",9600)
time.sleep(2)

print("ENCENDER LED CON PUSHBOTTON")
print("Desea iniciar el programa?")
start = input('1. Si     2. No -> ')#Capturo el ingreso del usuario pero como es input se captura como string
a = int(start)#convierto el dato capturado como string a entero para manejo de if

if a == 1:
    print("INICIADO")
    while 1:
        lectura = arduino.readline().decode("UTF-8")  # Capturo lo que se muestra en el puerto serial de arduino y decodifico para que salga sin caracteres extra el texto
        print(lectura)  # muestro en pantalla lo que estoy guardando en variable lectura osea, el estado del boton encendido o apagado
        time.sleep(2)
    else:
        quit() #funcion para salir del programa

"""

#AL PRESIONAR TECLA A y Y de la computadora que se enciendan los leds de manera indefinida intermitentemente
while True:
    if keyboard.is_pressed("a") and keyboard.is_pressed("y"):
        while 1:
            placa.digital[12].write(1)
            time.sleep(1)
            placa.digital[12].write(0)
            placa.digital[8].write(1)
            time.sleep(1)
            placa.digital[8].write(0)

# CREACION DE BOTONES QUE ENVIARAN SEÑAL A ARDUINO Y ENCENDERAN UN LED DURANTE 10 Seg
#CREANDO INTERFAZ
ventana = Tk() #se crea la ventana
ventana.title("BOTONES PARA ENVIO DE SEÑAL ARDUINO") #Definimos el nombre de nuestra ventana
ventana.geometry('500x350') #El primer numero es el ancho y el segundo es el alto de la ventana
ventana.configure(background='slate gray') #Le damos a nuestra ventana un color de fondo negro

# CREANDO LABEL QUE LLEVARA CONTROL DE PULSACIONES DE LOS BOTONES
# LABEL BOTON A
lbl = Label(ventana, text="0")
lbl.place(x=120, y=60)

# LABEL BOTON B
lblB = Label(ventana, text="0")
lblB.place(x=400, y=60)

#CREANDO BOTONES
# BOTON A
botonA = Button(ventana, text="BOTON A", fg="black", command=buttonA) #El command llama la accion del boton, en este caso una funcion que muestra un resultado en especifico
botonA.config(width=20, height=3) #Defino anchura y altura del boton
botonA.place(x=80, y=110) #coordenadas donde quiero que este el boton en la ventana

# BOTON B
botonB = Button(ventana, text="BOTON B", fg="black", command=buttonB)
botonB.config(width=20, height=3)
botonB.place(x=300, y=110)

# BOTON EXIT
botonExit = Button(ventana, text="EXIT", fg="black", command=buttonExit)
botonExit.config(width=20, height=3)
botonExit.place(x=180, y=210)

ventana.mainloop()
