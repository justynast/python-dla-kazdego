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
