# Repaso lectura de variables
# Por asignación directa
a = 10

# Por entrada de usuario:
# variable = input("Mensaje para el usuario...")

# Repaso concatenación de valores
b = "hola"
c = "a todos"
d = b + " " + c  # El valor de d seria "hola a todos"

# Repaso type casting
entero = 123
# cadena ahora contiene '123' que no es lo mismo que el numero 123 que contiene la variable entero
cadena = str(entero)

# Repaso control de flujo -> :
# Operadores aritmeticos: +, -, *, /, %
# Opreadores relacionales: >, <, >=, <=, ==, !=
# Operadores lógicos booleanos: True, False

# if - else
'''
if condición :
    #Se ejecuta si condición == verdadero
else:
    #Se ejecuta si condicion == falso
'''
# elif
'''
if condición:
    # Se ejecuta si condición == verdadero
elif otra_condición:
    # Se ejecuta si otra_condicion == verdadero
else:
    #Se ejecuta si ninguna condicion fue verdadera
'''

# match - case
'''
match valor:
    case 'a':
        #código si valor == 'a'
    case 'b':
        #código si valor == 'b'
    case _ :
        #código si ninguna condición fue verdadera

'''


# bucle while
'''
num = int(input("Ingrese un numero positivo entre (0-50): "))

if 0 <= num <= 50:
    while num != 0:
        print("contador = ", num)
        num = num - 1
        # num -= 1
else:
    print("El valor ingresado no esta dentro del rango.")
'''

# Ejemplo bucle for
'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for elemento in lista:
    print(elemento)

'''
# Ejercicio bucle for
'''
num = int(input("Ingrese un valor entre 1 y 100: "))

while num < 0 or num > 100: #Se puede usar la expresion not(100 > num > 0)
    print("Ingrese un numero valido.\n")
    num = int(input("Ingrese un valor entre 1 y 100: "))

suma_pares = 0

for i in range(2, num + 1, 2):
    print(i)
'''

# Listas por comprehensión
# Requiere de un objeto iterable como una lista, tupla, o diccionario

# lista = [expresion for elemento in iterable if condición ]
# la condicional if es opcional

# Ejemplo listas por comprehensión
numeros = [4, 6, 8, 16, 20, 25]
cuadrados = [numero**2 for numero in numeros if numero >= 15]

# Es equivalente a hacer:
for numero in numeros:
    if numero >= 15:
        cuadrados.append(numero**2)
