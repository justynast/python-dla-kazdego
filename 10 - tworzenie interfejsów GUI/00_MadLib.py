# Mad Lib
# Tworzy opowiadanie oparte na szczegółach wprowadzonych przez użytkownika

from tkinter import *

class Application(Frame):
    """
    Aplikacja z GUI, która tworzy opowiadanie oparte na danych
    wprowadzonych przez użytkownika.
    """
    def __init__(self, master):
        """ Inicjalizuj ramkę. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """
        Utwórz widżety potrzebne do pobrania informacji podanych
        przez użytkownika i wyświetlenia opowiadania.
        """
        # utwórz etykietę z instrukcją
        Label(self, text = "Wprowadź informacje do nowego opowiadania"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # utwórz etykietę i pole znakowe służące do wpisania imienia osoby
        Label(self,
              text = "Osoba: "
              ).grid(row = 1, column = 1, sticky = W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column = 1, sticky = W)
