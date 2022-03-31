import serial
import matplotlib.pyplot as plt
import time

arduino = serial.Serial('COM5', 9600, timeout=0)
point = 0
fig, ax = plt.subplots()
plt.ion()

maxlen = 20
x = []
y = []

while True:
    data = arduino.readline().decode().strip()
    time.sleep(0.2)
    if data:
        data = float(data)
        print("\nVoltios")
        print(data)
        x.append(point)
        y.append(data)
        if len(x) > maxlen:
            x = x[1:]
            y = y[1:]
        plt.plot(x, y, color='r')
        point += 1

        ax.clear()
        plt.ylim([0, 5])
        plt.xlabel('Time')
        plt.ylabel('Voltios')
        plt.title('Potenciometro Voltios VS Time')
        plt.show()

