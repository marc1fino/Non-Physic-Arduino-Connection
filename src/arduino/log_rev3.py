import os
import serial
import time

def read_log():
    dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(dir, 'logs.txt')
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip().split('\n\n')
            if content:
                return content[-1]
            else:
                return None
    except FileNotFoundError:
        return None

serial = serial.Serial('COM4', 9600)
serial.write(read_log().encode('utf-8'))

