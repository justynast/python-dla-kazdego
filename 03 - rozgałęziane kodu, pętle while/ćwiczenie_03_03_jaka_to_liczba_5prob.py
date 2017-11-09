"""
Zmodyfikuj program 'Jaka to liczba?' tak, aby gracz dysponował ograniczoną liczbą prób odgadnięcia wybranej
przez komputer liczby. Gdy graczowi nie uda się odgadnąć tej liczby w wyznaczonej liczbie prób,
program powinien wyświetlić odpowiedni komunikat z reprymendą.
"""

import random

print("Witaj w grze 'Jaka to liczba?'")
print("\nMam na myśli pewną liczbę z zakresu od 0 do 100.")
print("\nSpróbuj ją odgadnąć, masz na to pięć prób.")

the_number = random.randint(1, 100)
guess = int(input("Ta liczba to: "))
tries =  1

while guess != the_number and tries < 5:
    if guess > the_number:
        print("Za duża...")

    else:
        print("Za mała...")


    guess = int(input("Ta liczba to: "))
    tries += 1

if guess == the_number:
    print("\nOdgadłeś! Ta liczba to", the_number)
    print("Ilość prób:", tries)

else:
    print("Nie udało ci się odgadnąć liczby!")
    print("Liczba o której myślę to", the_number)

input("\n\nAby zakończyć naciśnij klawisz Enter.")
