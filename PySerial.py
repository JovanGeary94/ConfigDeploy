import serial
import os

command = '\n'
command1 = 'exit\n'
command2 = 'do show ver\n'

ser = serial.Serial(
    port='COM3',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

#ser.write(command.encode('utf-8'))
ser.write(command1.encode('utf-8'))
ser.write(command2.encode('utf-8'))


while True:
    
    for line in ser.read().decode('utf-8'):
        
        print(line, end="")
