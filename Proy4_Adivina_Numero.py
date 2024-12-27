from random import randint

nombre = input('Dime tu nombre: ')
print(f"{nombre}, he pensado un número entre 1 y 100, \ny tienes solo ocho intentos para adivinar cuál crees que es el número.")
numero_aleatorio = randint(1,100)
oportunidades = 0
numero = 0
while oportunidades < 8:
    numero = int(input('Por favor, dime un número: '))
    oportunidades += 1
    if numero < 1 or numero > 100 : ###if numero not in range(1,101)
        print('El número que ha elegido no está permitido')
    elif numero > numero_aleatorio :
        print('Respuesta incorrecta. Ha elegido un número mayor al número secreto')
    elif numero < numero_aleatorio :
        print('Respuesta incorrecta. Ha elegido un número menor al número secreto')
    else:
        print(f'Enhorabuena. Has ganado. Te ha llevado {oportunidades} oportunidades conseguirlo')
        break
if numero != numero_aleatorio:
    print(f"Game over. Se han agotado los intentos. El número secreto era {numero_aleatorio}")












