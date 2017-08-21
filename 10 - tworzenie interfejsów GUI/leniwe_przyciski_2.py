# leniwe przyciski 2
# demonstruje użycie klasy w programie wykorzystującym Tkinter

from tkinter import *

class Application(Frame):
    """ aplikacja oparta na GUI z trzema przyciskami """
    def __init__(self, master):
        """ inicjalizuj ramkę """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

