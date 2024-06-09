import os
import serial
import time
import re

serial_port = serial.Serial('COM5', 115200)
time.sleep(1)

def add_log(txt):
    dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(dir, 'logs.txt')
    with open(file_path, 'a') as file:
        file.write(f"{txt}\n\n")

str = ""
num_networks = 0

# Leer las primeras líneas para encontrar el número de redes
for _ in range(3):  # Leer las primeras 3 líneas
    data = serial_port.readline().decode('utf-8').strip()
    str += data + "\n"  # Agregar la línea leída a la cadena
    if "networks found" in data:
        # Extraer el número de redes usando una expresión regular
        match = re.search(r"(\d+) networks found", data)
        if match:
            num_networks = int(match.group(1))
            print(num_networks)
            break
        else:
            print("Warning: No se encontró el nmero de redes")

# Leer el resto de las líneas basadas en el nmero de redes encontradas
for i in range(1, num_networks + 1):  # Leer las líneas de las redes y dos líneas adicionales
    data = serial_port.readline().decode('utf-8').strip()
    print(data)
    str += data + "\n"  # Agregar la línea leída a la cadena

# Dividir los datos en líneas
lines = str.split('\n')

# Filtrar las líneas en blanco
filtered_lines = [line for line in lines if line.strip()]

# Unir todas las líneas en una sola cadena con saltos de línea
joined_lines = "\n".join(filtered_lines)

# Imprimir y agregar al log
print("Datos recibidos:")
print(joined_lines)
add_log(joined_lines)
