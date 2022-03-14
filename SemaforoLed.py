import pyfirmata
import time

board = pyfirmata.Arduino("COM5")

while True:

    print("Encendiendo luz verde")
    board.digital[11].write(1)
    time.sleep(1)
    board.digital[11].write(0)
    print("Encendiendo luz amarilla")
    board.digital[12].write(1)
    time.sleep(1)
    board.digital[12].write(0)
    print("Encendiendo luz roja")
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
