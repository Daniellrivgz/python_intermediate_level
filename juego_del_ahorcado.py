import os
import random


def normalize(s):
    reemplazar = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        )
    for a, b in reemplazar:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def read_data(filepath="./archivos/data.txt"):
    lista_palabras = []
    with open(filepath, "r", encoding="utf-8") as f:
        for w in f:
            lista_palabras.append(w.strip().upper())
    return lista_palabras


def run():
    data = read_data(filepath="./archivos/data.txt")
    palabra_random = random.choice(data)
    lista_palabra_random = [letra for letra in palabra_random]
    lista_palabra_random_underscores = ["_"] * len(lista_palabra_random)
    indexar_letra_dicc = {}
    for index, letra in enumerate(palabra_random):
        if not indexar_letra_dicc.get(letra):
            indexar_letra_dicc[letra] = []
        indexar_letra_dicc[letra].append(index)
    
    intentos = 10
    
    while True:
        os.system("clear")

        print("Bienvenido/a al juego del ahorcado")
        print("\n")
        print("Tienes: " +str(intentos) + " vidas.")
        print("\n")
        print("la palabra que debes adivinar contiene " + str(len(palabra_random)) + " letras, buena suerte.")
        print("\n")

        for elemento in lista_palabra_random_underscores:
            print(elemento + " ", end="")
        print("\n")

        try:
            print("\n")
            letra = input("Ingrese una letra y presiona Enter: ").strip().upper()
            assert letra.isalpha(), input("¡SOLO PUEDES INGRESAR LETRAS!, Presiona la tecla Enter para continuar.")
            assert len(letra) == 1, input(
                "¡SOLO UNA LETRA POR FAVOR!, Presiona la tecla Enter para continuar.")
        except AssertionError as e:
            print(e)
            continue

        if letra in lista_palabra_random:
            for index in indexar_letra_dicc[letra]:
                lista_palabra_random_underscores[index] = letra
        else:
            intentos-=1
            if intentos == -1:
                os.system("clear")

                print(
                    "Has perdido, mejor suerte la próxima. La palabra correcta era " + palabra_random)
                print("\n")
                perder = input("Presiona la tecla(X) para jugar otra vez, ó presiona cualquier otra tecla para salir").upper()
                if perder == "X":
                    intentos = 10
                    palabra_random = random.choice(data)
                    lista_palabra_random = [letra for letra in palabra_random]
                    lista_palabra_random_underscores = ["_"] * len(lista_palabra_random)
                    indexar_letra_dicc = {}
                    for index, letra in enumerate(palabra_random):
                        if not indexar_letra_dicc.get(letra):
                            indexar_letra_dicc[letra] = []
                        indexar_letra_dicc[letra].append(index)
                    continue
                else:
                    break

        if "_" not in lista_palabra_random_underscores:
            os.system("clear")
            print("Haz ganado, la palabra correcta es " + palabra_random)
            juego_nuevo = input("Presiona la tecla(X) para jugar otra vez, ó presiona cualquier otra tecla para salir").upper()
            if juego_nuevo == "X":
                intentos = 10
                palabra_random = random.choice(data)
                lista_palabra_random = [letra for letra in palabra_random]
                lista_palabra_random_underscores = ["_"] * len(lista_palabra_random)
                indexar_letra_dicc = {}
                for index, letra in enumerate(palabra_random):
                    if not indexar_letra_dicc.get(letra):
                        indexar_letra_dicc[letra] = []
                    indexar_letra_dicc[letra].append(index)
                continue
            else:
                break


if __name__ == '__main__':
    run()