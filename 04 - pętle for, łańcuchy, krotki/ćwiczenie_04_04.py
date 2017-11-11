"""
Utwórz grę, w której komputer losowo wybiera słowo, które gracz musi odgadnąć.
Komputer informuje gracza, ile liter znajduje się w wybranym słowie.
Następnie gracz otrzymuje pięć szans na zadanie pytania czy jakaś litera jest zawarta w tym słowie.
Komputer może odpowiedzieć tylko 'tak' lub 'nie'.
Potem gracz będzie musiał odgadnąć słowo.
"""
import random

# utwórz sekwencję słów do wyboru
WORDS = ("python", "anagram", "łatwy", "skomplikowany", "odpowiedź", "ksylofon")
# wybierz losowo jedno słowo z sekwencji
word = random.choice(WORDS)
# utwórz zmienną, by później użyć jej do sprawdzenia, czy odpowiedź jest poprawna
correct = word

# rozpocznij grę
print("""
        Witaj w grze!
        Myślę o pewnym słowie.
        Masz pięć szans na sprawdzenie, czy podana przez Ciebie litera
        jest w słowie, o którym myślę.
        Potem twoim zadaniem jest odgadnąć słowo.
        Do dzieła!
        """)

print("Słowo o którym myślę ma", len(correct), "liter.")
print(correct)

for i in range(5):
    char = input("Sprawdź literę: ")
    if char.lower() in correct:
        print("tak")
    else:
        print("nie")

ans = input("\nTwoja odpowiedź: ")

if ans == correct:
    print("Gratulacje, odgadłeś/aś!")
else:
    print("Niestety, nie udało Ci się. Myślę o słowie:", correct)

print("\nDziękuję za udział w grze.")
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

