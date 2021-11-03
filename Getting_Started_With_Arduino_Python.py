import serial
import time
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=0.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    num = input("Enter a NUmber:")
    value =  write_read(num)
    print(value)

