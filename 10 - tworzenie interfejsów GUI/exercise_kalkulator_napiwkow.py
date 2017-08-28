from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # utwórz etykietę do wprowadzenia kwoty rachunku
        Label(self,
              text = "Kwota rachunku:"
              ).grid(row = 0, column = 0, sticky = W)
        self.bill = Entry(self)
        self.bill.grid(row = 0, column = 1, sticky = W)


        # utwórz pole instrukcji
        Label(self,
              text = "Wybierz rodzaj napiwku"
              ).grid(row = 1, column = 0, sticky = W)

        # utwórz zmienną reprezentująca rodzaj tipa
        self.tip = IntVar()
        self.tip.set(None)

        # utwórz pola wyboru tipów
        Radiobutton(self,
                    text = "15%",
                    variable = self.tip,
                    value = 15,
                    command = self.update_txt
                    ).grid(row = 2, column = 0, sticky = W)

        Radiobutton(self,
                    text = "20%",
                    variable = self.tip,
                    value = 20,
                    command = self.update_txt
                    ).grid(row = 2, column = 1, sticky = W)

        # utwórz pole tekstowe do wyświetlenia wyników
        self.results_txt = Text(self, width = 15, height = 3, wrap = WORD)
        self.results_txt.grid(row = 3, column = 0, sticky = W)

    def update_txt(self):
        bill = self.bill.get()
        tip = self.tip.get()

        try:
            bill = int(bill)
            total = bill + bill * tip/100

            message = "Twój rachunek z napiwkiem wynosi: " + str(total) + "."

        except:
            "Wystąpił błąd. Spróbuj jeszcze raz."


        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)




# główna część programu
root = Tk()
root.title("Jaka to liczba?")
app = Application(root)
root.mainloop()
