# demonstracja wlasciwosci

class Critter(object):
    """wirtualny pupil"""
    def __init__(self, name):
        print("Urodzil sie nowy zwierzak!")
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Pusty łańcuch znaków nie może być imieniem zwierzaka.")
        else:
            self.__name = new_name
            print("Zmiana imienia się powiodła")

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "szczęśliwy"
        elif 5 <= unhappiness <= 10:
            m = "zadowolony"
        elif 11 <= unhappiness <= 15:
            m = "poddenerwowany"
        else:
            m = "wściekły"
        return m

    def talk(self):
        print("Nazywam się", self.name, "i jestem teraz", self.mood)
        self.__pass_time()

    def eat(self, food = 4):
        print("Om nom nom. Dzięki.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Juhu!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def main():
        crit_name = input("Jak chcesz nazwać swojego zwierzaka? ")
        crit = Critter(crit_name)

