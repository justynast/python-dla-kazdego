"""
Napisz program, który "rzuca" 100 razy monetą a następnie podaje użytkownikowi liczbę orzełków i reszek.
"""
import random

count = 0
orzelek = 0
reszka = 0

while count < 100:
    count +=1
    y = random.randint(1,2)
    if y == 1:
        orzelek += 1
    else:
        reszka += 1

print("Orzełków:", orzelek)
print("Reszek:", reszka)


input("\n\nAby zakończyć naciśnij klawisz Enter.")
