"""
Program, który symuluje telewizor, tworząc go jako obiekt.
Użytkownik powinien mieć możliwość wprowadzenia numeru kanału oraz zwiększania/zmniejszania głośności.
Zastosuj mechanizm zapewniający utrzymywanie numeru kanału we właściwych zakresach.
"""

class Television(object):
    def __init__(self, channel = 1, volume = 5):
        self.channel = channel
        self.volume = volume

    def changeChannel(self, new_channel):
        self.channel = new_channel

    def changeVolume(self, new_volume):
        self.volume = new_volume

    def getStatus(self):
        print("Jesteś na kanale:", self.channel)
        print("Aktualna głośność:", self.volume)

tv = Television()

def main():
    choice = None
    while choice != "3":
        print(
            """
            Wybierz co chcesz zrobić:
            0 - sprawdzić aktualny kanał i głośność
            1 - zmienić kanał
            2 - zmienić głośność
            3 - wyłączyć telewizor
            """
        )
        choice = input("Wybierasz: ")
        print()

        # wyjdź z pętli
        if choice == "3":
            print("Do widzenia!")

        # sprawdź status
        elif choice == "0":
            tv.getStatus()

        # zmień kanał
        elif choice == "1":
            new_channel = int(input("Wybierz kanał od 1 do 10: "))
            while new_channel not in range(1, 11):
                print("Nieprawidłowy wybór. Wybierz jeszcze raz.")
                new_channel = int(input("Wybierz kanał od 1 do 10: "))

            tv.changeChannel(new_channel)

        # zmień głośność
        elif choice == "2":
            new_volume = int(input("Wybierz poziom głośności od 1 do 10: "))
            while new_volume not in range(1, 11):
                print("Nieprawidłowy wybór. Wybierz jeszcze raz.")
                new_volume = int(input("Wybierz poziom głośności od 1 do 10: "))

            tv.changeVolume(new_volume)

        else:
            print(choice, "jest nieprawidłowym wyborem. Spróbuj jeszcze raz.")

main()
