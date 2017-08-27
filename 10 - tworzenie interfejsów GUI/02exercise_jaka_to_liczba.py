# ćwiczenie 2
# napisz wersję programu jaka to liczba z rozdziału 3, wykorzystując interfejs GUI

from tkinter import *
import random

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
        self.random_number = random.randint(1, 100)

    def get_random_number(self):
        self.random_number = random.randint(1,100)
        self.answer_txt.delete(0.0, END)

    def create_widgets(self):
        # utwórz etykietę z instrukcją
        Label(self,
              text = "Odganij liczbę z przedziału od 1 do 100."
              ).grid(row = 0, column = 0, columnspan = 3)

        # utwórz etykietę i pole znakowe służące do wpisania liczby
        Label(self,
              text = "Twoja odpowiedź:"
              ).grid(row = 1, column = 0, sticky = W)
        self.guess = Entry(self)
        self.guess.grid(row = 1, column = 1, sticky = W)

        # utwórz przycisk akceptacji danych
        Button(self,
               text = "Sprawdź odpowiedź",
               command = self.check_answer
               ).grid(row = 1, column = 2, sticky = W)

        # utwórz pole do wyświetlenia odpowiedzi
        self.answer_txt = Text(self, width = 43, height = 2, wrap = WORD)
        self.answer_txt.grid(row = 3, column = 0, columnspan = 3, sticky = W)

        # utwórz przycisk losowania liczby
        Button(self,
               text = "Losuj inną liczbę",
               command = self.get_random_number
               ).grid(row = 4, column = 2, sticky = E)

    def check_answer(self):
        guess = self.guess.get()
        random_number =  self.random_number

        try:
            guess = int(guess)
            if guess == random_number:
                answer = "Odgadłeś! Liczba o której myślę to " + str(random_number) + "."
            elif guess > random_number:
                answer = "Za duża!"
            elif guess < random_number:
                answer = "Za mała!"
        except:
            answer = "To nie jest liczba!"

        self.answer_txt.delete(0.0, END)
        self.answer_txt.insert(0.0, answer)


# główna część programu
root = Tk()
root.title("Jaka to liczba?")
app = Application(root)
root.mainloop()
