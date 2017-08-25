# wybór filmów 2
# demonstruje przyciski opcji

from tkinter import *

class Application(Frame):
    """ Aplikacja z GUI służąca do wyboru ulubionego gatunku filmów """
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # utwórz etykietę z opisem
        Label(self,
              text = "Wybierz swój ulubiony gatunek filmu."
              ).grid(row = 0, column = 0, sticky = W)

        # utwórz etykietę z instrukcją:
        Label(self,
              text = "Wybierz jeden gatunek:"
              ).grid(row = 1, column = 0, sticky = W)
