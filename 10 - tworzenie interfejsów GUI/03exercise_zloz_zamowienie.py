"""
Ćwiczenie 3
Utwórz program z interfejsem GUI o nazwie "Złóż zamówienie", który przedstawia użytkownikowi
proste restauracyjne menu, które wymienia pozycje i ich ceny. Pozwól użytkownikowi na wybranie różnych pozycji
a potem pokaż końcowy rachunek.
"""

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        # utwórz etykietę z instrukcją
        Label(self,
              text = "Wybierz co chciałbyś zamówić:"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # utwórz pola wyboru
        self.zupaCebulowa = BooleanVar()
        Checkbutton(self,
                    text = "Zupa cebulowa",
                    variable = self.zupaCebulowa
                    ).grid(row = 1, column = 0, sticky = W)

        self.krazkiCebulowe = BooleanVar()
        Checkbutton(self,
                    text = "Krążki cebulowe",
                    variable = self.krazkiCebulowe
                    ).grid(row = 2, column = 0, sticky = W)

        self.cebulaFaszerowana = BooleanVar()
        Checkbutton(self,
                    text = "Cebula faszerowana",
                    variable = self.cebulaFaszerowana
                    ).grid(row = 3, column = 0, sticky = W)

        self.cebula = BooleanVar()
        Checkbutton(self,
                    text = "Cebula",
                    variable = self.cebula
                    ).grid(row = 4, column = 0, sticky = W)

        # utwórz przycisk akceptacji danych
        Button(self,
               text = "Oblicz rachunek",
               command = self.calculateTotal
               ).grid(row = 5, column = 1, sticky = W)

        # utwórz ramkę do prezentacji danych
        self.txtFrame = Text(self,
                             width = 20,
                             height = 2,
                             wrap = WORD
                             ).grid(row = 6, column = 0, columnspan = 2, sticky = W)

