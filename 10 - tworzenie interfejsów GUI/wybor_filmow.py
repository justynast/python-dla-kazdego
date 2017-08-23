# Wybór filmów
# Demonstruje pola wyboru

from tkinter import *

class Application(Frame):
    """ Aplikacja z GUI służąca do wyboru ulubionych gatunków filmów """
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
