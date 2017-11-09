"""
Napisz program sprzedawca samochodów, w którym użytkownik wprowadza podstawową cenę samochodu.
Program powinien dodać szereg dodatkowych opłat, takich jak:
    1) podatek,
    2) opłatę rejestracyjną,
    3) prowizję przygotowawczą dealera,
    4) opłatę za dostarczenie.
Oblicz 1 i 2 jako pewien procent ceny podstawowej. 3 i 4 mają stałe wartości.
Wyświetl faktyczną cenę samochodu po doliczeniu wszystkich dodatków.
"""

cena_podstawowa = input("Wprowadź cenę podstawową samochodu: ")
cena_podstawowa = int(cena_podstawowa)
podatek = cena_podstawowa * 0.15
op_rej = cena_podstawowa * 0.10
prowizja = 200
op_dos = 100
cena_koncowa = cena_podstawowa + podatek + op_rej + prowizja + op_dos

print("Faktyczne cena samochodu po doliczeniu dodatkowych opłat:", cena_koncowa, "złotych.")

input("\n\nAby zakończyć naciśnij klawisz Enter.")
