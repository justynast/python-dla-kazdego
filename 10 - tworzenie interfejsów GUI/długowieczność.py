# długowiezność
# demonstruje widżety text i entry oraz menedżer układu grid

from tkinter import *

class Application(Frame):
    """ aplikacja z GUI, która może ujawnić sekret długowieczności"""
    def __init__(self, master):
        """ inicjalizuje ramkę """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ utwórz widżety typu Button, Text i Entry"""
        # utwórz etykietę z instrukcją
        self.inst_lbl = Label(self, text = "Wprowadź hasło do sekretu długowieczności")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # utwórz etykietę do hasła
        self.pw_lbl = Label(self, text = "Hasło: ")
        self.pw_lbl.grid(row = 1, column = 0, sticky = W)

        # utwórz widżet Entry do przyjęcia hasła
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)

        # utwórz przycisk 'Akceptuj'
        self.submit_bttn = Button(self, text = "Akceptuj", command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)

