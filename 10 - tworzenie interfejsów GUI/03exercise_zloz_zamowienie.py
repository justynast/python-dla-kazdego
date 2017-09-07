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
                    text = "Zupa cebulowa - 10zł",
                    variable = self.zupaCebulowa
                    ).grid(row = 1, column = 0, sticky = W)

        self.krazkiCebulowe = BooleanVar()
        Checkbutton(self,
                    text = "Krążki cebulowe - 5zł",
                    variable = self.krazkiCebulowe
                    ).grid(row = 2, column = 0, sticky = W)

        self.cebulaFaszerowana = BooleanVar()
        Checkbutton(self,
                    text = "Cebula faszerowana - 20zł",
                    variable = self.cebulaFaszerowana
                    ).grid(row = 3, column = 0, sticky = W)

        self.cebula = BooleanVar()
        Checkbutton(self,
                    text = "Cebula - 1zł",
                    variable = self.cebula
                    ).grid(row = 4, column = 0, sticky = W)

        # utwórz przycisk akceptacji danych
        Button(self,
               text = "Oblicz rachunek",
               command = self.calculateTotal
               ).grid(row = 5, column = 0, sticky = W)

        # utwórz pole tekstowe do wyświetlenia wyników
        self.results_txt = Text(self, width = 20, height = 3, wrap = WORD)
        self.results_txt.grid(row = 6, column = 0, sticky = W)

    def calculateTotal(self):
        """ oblicz rachunek na podstawie uzyskanych danych """

        total = 0
        if self.zupaCebulowa.get():
            total += 10
        if self.krazkiCebulowe.get():
            total += 5
        if self.cebulaFaszerowana.get():
            total += 20
        if self.cebula.get():
            total += 1

        txt = ""

        if total == 0:
            txt += "Nic nie zamówiłeś, nie masz nic do zapłaty."
        else:
            txt += "Twój rachunek wynosi: "
            txt += str(total)
            txt += " PLN."

        # wyświetl dane
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, txt)


# główna część programu
root = Tk()
root.title("Złóż zamówienie")
app = Application(root)
root.mainloop()
