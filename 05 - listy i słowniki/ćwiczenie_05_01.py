"""
Utwórz program, który wypisuje listę słów w przypadkowej kolejności.
Program powinien wypisać wszystkie słowa bez żadnych powtórzeń.
"""


tekst = "Litwo! Ojczyzno moja! Ty jesteś jak zdrowie. Ile cię trzeba było widać. Moja zdrowie Litwo jak jesteś ile cię"

tekst_roz = tekst.split()

nowalista = []

for word in tekst_roz:
    if word.lower() not in nowalista:
        nowalista.append(word.lower())

print(nowalista)
