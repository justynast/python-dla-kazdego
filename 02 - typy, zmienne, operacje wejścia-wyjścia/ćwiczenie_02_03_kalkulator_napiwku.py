# Napisz program Kalkulator napiwku, w którym użytkownik wprowadza sumę ogólną z rachunku.
# Program powinien potem wyświetlić dwie kwoty napiwku - w wysokości 15 i 20 procent.

rachunek = int(input("Ile wynosi rachunek? "))

tip_15 = rachunek + rachunek * 0.15
tip_20 = rachunek + rachunek * 0.20

print("\nRachunek razem z napiwkiem 15% wynosi:", tip_15)
print("\nRachunek razem z napiwkiem 20% wynosi:", tip_20)

input("\n\nAby zakończyć naciśnij klawisz Enter.")
