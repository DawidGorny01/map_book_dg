def read_friends(users: list)->None:
    print("informacje o twoich znajomych: ")
    for user in users:
        print(f'\tTwój znajomy {user["name"]} {user["surname"]} opublikował {user["posts"]} postów.')

def add_user(lista: list) -> None:
    imie = input("Podaj imie: ")
    nazwisko = input("Podaj nazwisko: ")
    liczba_postow = int(input("Podaj liczbę postów użytkonika: "))
    new_user = {"name": imie, "surname": nazwisko, "posts": liczba_postow }
    lista.append(new_user)

def search_user(users: list):
    imie = input("Podaj imię: ")
    for user in users:
        if user["name"] == imie:
            print(user)

def remove_user(users: list):
    imie = input("Podaj imię: ")
    for user in users:
        if user["name"] == imie:
            users.remove(user)

def update_user(users: list):
    imie = input("Wprowadź imię uzytkownika, którego dane chcesz zmienić: ")
    for user in users:
        if user["name"] == imie:
            user["name"] = input("Podaj nowe imię: ")
            user["surname"] = input("Podaj nowe nazwsiko: ")
            user["posts"] = int(input("Podaj nowa liczbę postów: "))