def run ():
    # Usando la opcion list comprehension
    # my_list = [1, 4, 5, 6, 9, 13, 19, 21]

    # impares = [i for i in my_list if i % 2 != 0]
    
    # Ahora vamos a usar para ese mismi ejercicio la funcion Lambda y Filter al mismo tiempo
    # my_list = [1, 4, 5, 6, 9, 13, 19, 21]

    # impares = list(filter(lambda x: x%2 !=0, my_list))
    # print(impares)

    # Realizando el ejercicio map utilizando solo list compehension
    # my_list = [1, 2, 3, 4, 5]

    # cuadrado = [i**2 for i in my_list]

    # print(cuadrado)

    # Ahora usamos la funcion map junto con lambda

    # my_list = [1, 2, 3, 4, 5]

    # cuadrado = list(map(lambda x:x**2, my_list))

    # print(cuadrado)

    # Utilizamos el ciclo for para recidir una lista a un solo dato
    # my_list = [2, 2, 2, 2, 2]

    # all_numbers = 1

    # for i in my_list:
    #     all_numbers = all_numbers * i
        
    # print(all_numbers)

    # Por ultimo usamos la funcion Reduce para solicionar el ejercicio
    from functools import reduce

    my_list = [2, 2, 2, 2, 2]

    all_multiplied = reduce(lambda a, b : a * b, my_list)

    print(all_multiplied)


if __name__ == '__main__':
    run()
