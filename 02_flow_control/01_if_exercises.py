###
# EJERCICOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
# num1 = input('Enter one number: ')
# num2 = input('Enter another number: ')

# if num1 > num2:
#     print(f"El {num1} es mayor")
# elif num2 > num1:
#     print(f"El {num2} es mayor")
# else:
#     print('Los numeros son iguales')


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
# num1 = int(input('Enter one number: '))
# num2 = int(input('Enter another number: '))
# operator = input('Enter one operand (+, -, *, /): ')

# if operator == '+':
#     print( num1 + num2)
# elif operator == '-':
#     print( num1 - num2)
# elif operator == '*':
#     print( num1 * num2)
# elif operator == '/':
#     if num2 == 0:
#         print(0)
#     else:
#       print( num1 / num2)
# else:
#     print('Operand no supported')

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, 
# excepto si es divisible por 100 pero no por 400.

# year = int(input('Enter one year: '))

# if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):          
#       print('Leap Year')
# else:
#     print('Not Leap Year')

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

age = int(input('Enter your age: '))

if(age >= 65):
     print('Adulto mayor')
elif(age >= 18):
     print('Adulto')
elif(age >= 13):
     print('Adolescente')
elif(age >= 3):
     print('Nino')
else:
     print('Bebé')