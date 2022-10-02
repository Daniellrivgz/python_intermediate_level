from optparse import Values


def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Daniel", "lastname": "Rivera"} 

    super_list = [
        {"firstname": "Daniel"},
        {"firstname": "Juan"},
        {"firstname": "Pedro"},
        {"firstname": "Juanita"},
        {"firstname": "Andres"},
    ]

    Super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "intefer_nums": [-1, -2, 0, 1, 2],
        "floating_num": [1.1, 4.5, 6.43],
    }

    for values in super_list:
        for key, value in values.items():
            print(key, "-", value)


if __name__ == '__main__':
    run()