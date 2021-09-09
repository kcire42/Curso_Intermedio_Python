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
        'name': 'Héctor',
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
        'age': 90,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 15,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def main():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python" ]
    print(all_python_devs)
    all_python_devs_filter = list(filter(lambda worker: worker["language"] == "python",DATA))
    all_python_devs_filter_map = list(map(lambda worker: worker["name"],all_python_devs_filter))
    print(all_python_devs_filter_map)
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    print(all_platzi_workers)
    adultos_list = [worker["name"] for worker in DATA if worker["age"] >= 18]
    print(adultos_list)
    adultos_filter = list(filter(lambda worker: worker["age"] >= 18, DATA))
    #print(adultos_filter)
    adultos_map = list(map(lambda worker: worker["name"], adultos_filter))
    print(adultos_map)
    #SUMAR DICCIONARIOS SE USA EL SIMBOLO |
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    print(old_people)




if __name__ == "__main__":
    main()