import sys
import os
from time import sleep

print("Nombre del script:", sys.argv[0], '\n')
print("Numero de argumentos: ", len(sys.argv)-1)
for argumento in sys.argv[1:]:
    print(argumento)
print('---------------\n')
print("Plataforma: ", sys.platform)
print('---------------\n')
print("Rutas donde python busca módulos:")
for ruta in sys.path:
    print(ruta)
print('---------------\n')

print(f"Lista de archivos en el directorio: {os.getcwd()}")
for archivo in os.listdir():
    print(archivo)

print('---------------\n')
# os.remove(sys.argv[1])
# os.rename(sys.argv[1], sys.argv[2])
os.chdir('..')
print(f"Lista de archivos en el directorio: {os.getcwd()}")
for archivo in os.listdir():
    print(archivo)
print('---------------\n')

sleep(5)
os.system('clear')
