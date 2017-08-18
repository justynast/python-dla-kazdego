"""
Ćwiczenie 1
Ulepsz program Opiekun zwierzaka, pozwalając użytkownikowi na określenie ilości pożywienia podawanego zwierzakowi
i czasu poświęconego na zabawę z nim.
Wartości te powinny wpływać na szybkość spadku poziomu głodu i nudy u zwierzaka.
"""

class Critter(object):
    """ wirtualny pupil """
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

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
        print("Hunger:", self.hunger)#help
        print("Boredom:", self.boredom)#help
        self.__pass_time()

    def eat(self, food):
        print("Before:", self.hunger) #help
        print("Om nom nom. Dziękuję.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        print("After:", self.hunger)#help
        self.__pass_time()
        print("After:", self.hunger)#help


    def play(self, fun):
        print("Before:", self.boredom)#help
        print("Juhu!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        print("After:", self.boredom)#help
        self.__pass_time()
        print("After:", self.boredom)#help


def main():
    crit_name = input("Jak chcesz nazwać swojego zwierzaka?: ")
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print \
        ("""
        Opiekun zwierzaka

        0 - zakończ
        1 - słuchaj swojego zwierzaka
        2 - nakarm swojego zwierzaka
        3 - pobaw się ze swoim zwierzakiem

        """)
        choice = input("Wybierasz: ")
        print()

        #wyjdź z pętli
        if choice == "0":
            print("Do widzenia.")

        # słuchaj zwierzaka
        elif choice == "1":
            crit.talk()

        # nakarm zwierzaka
        elif choice == "2":
            food = int(input("Jaką ilość jedzenia chcesz podać zwierzakowi?(1-5): "))
            while food not in range(1,6):
                print("Nieprawidłowy wybór.")
                food = int(input("Jaką ilość jedzenia chcesz podać zwierzakowi?(1-5): "))
            crit.eat(food)

        # pobaw się ze swoim zwierzakiem
        elif choice == "3":
            fun = int(input("Jak długo chces bawić się ze zwierzakiem?(1-5): "))
            while fun not in range(1,6):
                print("Nieprawidłowy wybór.")
                fun = int(input("Jak długo chces bawić się ze zwierzakiem?(1-5): "))
            crit.play(fun)

        # nieznany wybór
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")

main()
input("\n\nAby zakończyć naciśnij klawisz Enter.")
