"""
Napisz program, który liczy za użytkownika. Umożliw użytkownikowi wprowadzenie liczby początkowej, liczby końcowej
i wielkości odstępu między kolejnymi liczbami.
"""

x = int(input("Liczba początkowa: "))
y = int(input("Liczba końcowa: "))
z = int(input("Odstęp między liczbami: "))

print("Liczenie: ")
for i in range(x, y+1, z):
    print(i, end=" ")

input("\n\nAby zakończyć naciśnij klawisz Enter.")
