"""
Ćwiczenie 4
Utwórz program Farma zwierzaków, konkretyzując kilka obiektów klasy Critter i śledząc ich stan poprzez listę.
Naśladuj program Opiekun zwierzaka, lecz zamiast wymagać od użytkownika zajmowania się pojedynczym zwierzakiem,
zażądaj od niego opieki nad całą farmą.
Każda pozycja menu powinna umożliwić użytkownikowi wykonanie pewnej czynności obejmującej wszystkie zwierzaki.
Aby program był ciekawszy, nadaj każdemu zwierzakowi wybrany losowo poziom głodu i nudy.
"""

import random

class Critter(object):
    """ wirtualny pupil """
    def __init__(self, name, hunger, boredom):
        print("Urodził się nowy zwierzak!")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        obj = "Obiekt klasy Critter\n"
        obj += "imię: " + self.name + "\n"
        obj += "głód: " + str(self.hunger) + "\n"
        obj += "znudzenie: " + str(self.boredom) + "\n"
        obj += "humor: " + self.mood + "\n"
        return obj

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "szczęśliwy"
        elif 5 <= unhappiness <= 10:
            m = "zadowolony"
        elif 11 <= unhappiness <= 15:
            m = "podenerwowany"
        else:
            m = "wściekły"

        return m

    def talk(self):
        print("Nazywam się", self.name, "i jestem teraz", self.mood, "\n")
        self.__pass_time()

    def eat(self, food = 4):
        print(self.name, "mówi: Om nom nom. Dziękuję.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print(self.name, "mówi: Juhu!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name1 = input("Jak chcesz nazwać pierwszego zwierzaka?")
    crit1 = Critter(crit_name1, random.randint(0,10), random.randint(0,10))
    crit_name2 = input("Jak chcesz nazwać drugiego zwierzaka?")
    crit2 = Critter(crit_name2, random.randint(0,10), random.randint(0,10))
    crit_name3 = input("Jak chcesz nazwać trzeciego zwierzaka?")
    crit3 = Critter(crit_name3, random.randint(0,10), random.randint(0,10))

    choice = None

    while choice != "0":
        print \
        ("""
        Opiekun zwierzaka

        0 - zakończ
        1 - słuchaj wszystkich zwierzaków
        2 - nakarm wszystkie zwierzaki
        3 - pobaw się ze wszystkimi zwierzakami

        """)
        choice = input("Wybierasz: ")
        print()

        if choice == "0":
            print("Do widzenia!")

        elif choice == "1":
            crit1.talk()
            crit2.talk()
            crit3.talk()

        elif choice == "2":
            crit1.eat()
            crit2.eat()
            crit3.eat()

        elif choice == "3":
            crit1.play()
            crit2.play()
            crit3.play()

        elif choice == "4":
            print(crit1)
            print(crit2)
            print(crit3)

        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")

main()
input("\n\nAby zakończyć naciśnij klawisz Enter.")
