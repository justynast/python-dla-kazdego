"""
Napisz program, który symuluje ciasteczko z wróżbą.
Program powinien wyświetlić jedną z niepowtarzalnych przepowiedni, dokonując losowego wyboru
przy każdym uruchomieniu.
"""

import random

print("Witaj w programie ciasteczko z wróżbą!")
print("\nTwoja wróżba to:")

num = random.randint(1, 5)

if num == 1:
    print("Dopóki kobieta wygląda dziesięć lat młodziej niż jej córka, dopóty jest całkowicie zadowolona.")

elif num == 2:
    print("Jezus zaś rzekł: «Czy nie dziesięciu zostało oczyszczonych? Gdzie jest dziewięciu?»")

elif num == 3:
    print("Lepiej zrezygnować z dziesięciu cudzych myśli, by mieć jedną własną.")

elif num == 4:
    print("Łatwiej ułożyć dziesięć poprawnych sonetów niż dobry tekst ogłoszenia.")

elif num == 5:
    print("Wystarczy urodzić się dziesięć lat wcześniej, by już być kimś innym duchowo.")

else:
    print("Coś poszło nie tak!")


input("\n\nAby zakończyć naciśnij klawisz Enter.")
