"""
Napisz program Kreator postaci do gry z podziałem na role. Gracz powinien otrzymać pulę 30 punktów,
którą może spożytkować na cztery atrybuty: siła, zdrowie, mądrość, zręczność.
Gracz powinien mieć możliwość przeznaczania punktów z puli na dowolny atrybut, jak również możliwość odbierania
punktów przypisanych do atrybutu i przekazywania ich z powrotem do puli.
"""

punkty = 30
atrybuty = {"Siła":0,
            "Zdrowie":0,
            "Mądrość":0,
            "Zręczność":0}


choice = None
while choice != "0":
    print("""
    Kreator Postaci
    0 - wyjdź z programu
    1 - zmień wartości atrybutów
    2 - wyświetl wartości atrybutów
    3 - wyzeruj wartości atrybutów
    """)

    choice = input("Twój wybór: ")

    if choice == "0":
        print("Do widzenia!")

    elif choice == "1":
        print("Masz", punkty, "punktów.")
        for at in atrybuty:
            print(at)
            val = int(input("Wprowadź wartość: "))
            while val > punkty:
                print("Nieprawidłowa wartość!")
                val = int(input("Wprowadź wartość: "))
            atrybuty[at] = val
            punkty -= val
            print("Pozostało:", punkty, "punktów.")

    elif choice == "2":
        for at in atrybuty:
            print(at, atrybuty[at])
        print("Pozostałe punkty:", punkty)

    elif choice == "3":
        for at in atrybuty:
            atrybuty[at] = 0

        punkty = 30

# for at in atrybuty:
#     print(atrybuty[at]) <--- wartości
