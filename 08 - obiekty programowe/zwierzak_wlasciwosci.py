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

    def talk(self):
        print("Cześć! Nazywam się", self.name)

# część główna
crit = Critter("Franek")
crit.talk()

print("\nImię mojego zwierzaka to:", crit.name)
print("Próbuję zmienić imię mogego zwierzaka na Olek...")
crit.name = "Olek"
print("\nImię mojego zwierzaka to:", crit.name)
print("Próbuję zmienić imię mogego zwierzaka na pusty łańcuch znaków...")
crit.name = ""
print("\nImię mojego zwierzaka to:", crit.name)

input("\n\nAby zakończyć naciśnij klawisz enter")
