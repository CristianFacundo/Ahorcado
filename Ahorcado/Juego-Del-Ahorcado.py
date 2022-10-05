from ast import Break
import random



menuprincipal = int(input("AHORCADO \n Menu Principal: \n 1-Nivel Facil: \n 2-Nivel Intermedio: \n 3-Nivel Dificil:\n "))

while menuprincipal != 0:

    if menuprincipal == 1:
        print("Nivel Facil")
        w_list = ["libro", "sandia", "sopa" , "auto", "mapa", "teclado","maleta"]

        palabra = random.choice(w_list)

        errores = 0

        progreso = []
        for i in range(len(palabra)):
            progreso.append("_ ")

        palabra_con_espacios = []
        for char in palabra:
            palabra_con_espacios.append(char + ' ')

        letras_usadas = []

        while errores < 7:
            if errores == 0:
                print(' ______ ')
                print(' |   |  ')
                print(' |      ')
                print(' |      ')
                print(' |      ')
                print(' |      ')
                print(' ---    ')
            elif errores == 1:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O   ')
                print(' |      ')
                print(' |      ')
                print(' |      ')
                print(' ---    ')
            elif errores == 2:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O  ')
                print(' |   |  ')
                print(' |      ')
                print(' |      ')
                print(' ---    ')
            elif errores == 3:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O  ')
                print(' |   |  ')
                print(' |  /   ')
                print(' |      ')
                print(' ---    ')
            elif errores == 4:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O  ')
                print(' |   |  ')
                print(' |  / \\  ')
                print(' |      ')
                print(' ---    ')
            elif errores == 5:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O  ')
                print(' |  /|  ')
                print(' |  / \\  ')
                print(' |      ')
                print(' ---    ')
            elif errores == 6:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O  ')
                print(' |  /|\\  ')
                print(' |  / \\  ')
                print(' |      ')
                print(' ---    ')
                print(' Perdiste! ')
                break

            print(''.join(progreso))
            print("Letras usadas: ", letras_usadas)
            print('Elegir una Letra: ')
            letra = input()
            if letra in letras_usadas:
                print('Esta letra ya la usaste...')
            else:
                letras_usadas.append(letra)

                hay_error = True
                for i in range(len(palabra)):
                    if letra == palabra[i]:
                        progreso[i] = letra + ' '
                        hay_error = False

                if hay_error:
                    errores += 1

                if palabra_con_espacios == progreso:
                    print(''.join(progreso))
                    print('Ganaste!')
                    break
    elif menuprincipal == 2:
        print("Nivel Intermedio")

        w_list = ["almohada", "alcohol", "adhesivo"]

        palabra = random.choice(w_list)

        errores = 0

        progreso = []
        for i in range(len(palabra)):
            progreso.append("_ ")

        palabra_con_espacios = []
        for char in palabra:
            palabra_con_espacios.append(char + ' ')

        letras_usadas = []

        while errores < 7:
            if errores == 0:
                print(' ______ ')
                print(' |   |  ')
                print(' |      ')
                print(' |      ')
                print(' |      ')
                print(' |      ')
                print(' ---    ')
            elif errores == 1:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O   ')
                print(' |      ')
                print(' |      ')
                print(' |      ')
                print(' ---    ')
            elif errores == 2:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O  ')
                print(' |   |  ')
                print(' |      ')
                print(' |      ')
                print(' ---    ')
            elif errores == 3:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O  ')
                print(' |   |  ')
                print(' |  /   ')
                print(' |      ')
                print(' ---    ')
            elif errores == 4:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O  ')
                print(' |   |  ')
                print(' |  / \\  ')
                print(' |      ')
                print(' ---    ')
            elif errores == 5:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O  ')
                print(' |  /|  ')
                print(' |  / \\  ')
                print(' |      ')
                print(' ---    ')
            elif errores == 6:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O  ')
                print(' |  /|\\  ')
                print(' |  / \\  ')
                print(' |      ')
                print(' ---    ')
                print(' Perdiste! ')
                break

            print(''.join(progreso))
            print("Letras usadas: ", letras_usadas)
            print('Elegir una Letra: ')
            letra = input()
            if letra in letras_usadas:
                print('Esta letra ya la usaste...')
            else:
                letras_usadas.append(letra)

                hay_error = True
                for i in range(len(palabra)):
                    if letra == palabra[i]:
                        progreso[i] = letra + ' '
                        hay_error = False

                if hay_error:
                    errores += 1

                if palabra_con_espacios == progreso:
                    print(''.join(progreso))
                    print('Ganaste!')
                    break
    elif menuprincipal == 3:
        print("Nivel Dificil")

        w_list = ["vulnerabilidad", "paralelepido","institucionalizacion", "otorrinolaringólogo",""]

        palabra = random.choice(w_list)

        errores = 0

        progreso = []
        for i in range(len(palabra)):
            progreso.append("_ ")

        palabra_con_espacios = []
        for char in palabra:
            palabra_con_espacios.append(char + ' ')

        letras_usadas = []

        while errores < 7:
            if errores == 0:
                print(' ______ ')
                print(' |   |  ')
                print(' |      ')
                print(' |      ')
                print(' |      ')
                print(' |      ')
                print(' ---    ')
            elif errores == 1:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O   ')
                print(' |      ')
                print(' |      ')
                print(' |      ')
                print(' ---    ')
            elif errores == 2:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O  ')
                print(' |   |  ')
                print(' |      ')
                print(' |      ')
                print(' ---    ')
            elif errores == 3:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O  ')
                print(' |   |  ')
                print(' |  /   ')
                print(' |      ')
                print(' ---    ')
            elif errores == 4:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O  ')
                print(' |   |  ')
                print(' |  / \\  ')
                print(' |      ')
                print(' ---    ')
            elif errores == 5:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O  ')
                print(' |  /|  ')
                print(' |  / \\  ')
                print(' |      ')
                print(' ---    ')
            elif errores == 6:
                print(' ______ ')
                print(' |   |  ')
                print(' |   O  ')
                print(' |  /|\\  ')
                print(' |  / \\  ')
                print(' |      ')
                print(' ---    ')
                print(' Perdiste! ')
                break

            print(''.join(progreso))
            print("Letras usadas: ", letras_usadas)
            print('Elegir una Letra: ')
            letra = input()
            if letra in letras_usadas:
                print('Esta letra ya la usaste...')
            else:
                letras_usadas.append(letra)

                hay_error = True
                for i in range(len(palabra)):
                    if letra == palabra[i]:
                        progreso[i] = letra + ' '
                        hay_error = False

                if hay_error:
                    errores += 1

                if palabra_con_espacios == progreso:
                    print(''.join(progreso))
                    print('Ganaste!')
                    break
    else:
        print("por favor digita una opcion correcta")
         
    menuprincipal = int(input("AHORCADO \n Menu Principal: \n 1-Nivel Facil: \n 2-Nivel Intermedio: \n 3-Nivel Dificil:\n 0-Finaliza El Juego \n "))
 