def run():


    ## Forma tradicional de hacer el ejercicio

    # my_dictionary = {}

    # for i in range(1, 101):
    #     if i %3 != 0:
    #         my_dictionary[i] = i**3

    ## Forma sencilla de hacer el ejecicio

    # my_dictionary = {i:i**3 for i in range(1, 101) if i %3 != 0}

    ## Forma tradicional de hacer el reto

    # my_dictionary = {}

    # for i in range(1, 1001):
    #     my_dictionary[i] = i**2

    my_dictionary = {i : round(i**0.5,2) for i in range(1, 1001)}

    print(my_dictionary)


if __name__ == '__main__':
    run()