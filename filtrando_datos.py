DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Hector',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():

    # Buscando las personas que trabajan con el lenguaje Python
    # all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

    # for worker in all_python_devs:
    #     print(worker)

    # Buscando todas las personas que trabajan para la organizacion Platzi
    # all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    # for worker in all_platzi_workers:
    #     print(worker)

    # Buscando las edades con list compehension
    # all_workers_adult = [worker["name"] for worker in DATA if int(worker["age"]) >= int("18")]

    # for worker in all_workers_adult:
    #     print(worker)

    # Buscando las personas mayores de edad con filter
    # all_workers_adult = list(filter(lambda worker: worker["age"] >= 18, DATA))

    # for worker in all_workers_adult:
    #     print(worker["name"])

    # En esta ocasion usamos la high funtion map para buscar las personas mayores a 70 años, pero le añadimos algo nuevo que se llama: sumar diccionario y se utiliza con el simbolo |
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    for worker in old_people:
        print(worker)


if __name__ == '__main__':
    run()