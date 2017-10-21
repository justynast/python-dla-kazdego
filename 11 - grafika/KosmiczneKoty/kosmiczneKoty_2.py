# Złap spadające z kosmosu koty zanim spadną na ziemię!

from livewires import games, color
import random

games.init(screen_width = 800, screen_height = 600, fps = 50)
meow_sound = games.load_sound("meow.wav")

class Bed(games.Sprite):
    """ łóżko sterowane myszką gracza służące do łapania spadających kotów"""
    image = games.load_image("bed.png")

    def __init__(self):
        """ Initialize Bed object and create Text object for score. """
        super(Bed, self).__init__(image = Bed.image,
                                  x = games.mouse.x,
                                  bottom = games.screen.height)

        self.score = games.Text(value = 0, size = 25, color = color.pink,
                                top = 5, right = games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        """ Zmień pozycję na wyznaczoną przez współrzędną x myszy. """
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()

    def check_catch(self):
        """ Sprawdź, czy nie zostały złapane jakieś kotki. """
        for kitten in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            kitten.handle_caught()
            meow_sound.play()


class Kitten(games.Sprite):
    """
    Kotek, który spada na ziemię.
    """
    image = games.load_image("kitten.png")
    speed = 1

    def __init__(self, x, y = 90):
        """ Inicjalizuj obiekt klasy Kitten. """
        super(Kitten, self).__init__(image = Kitten.image,
                                    x = x, y = y,
                                    dy = Kitten.speed)

    def update(self):
        """ Sprawdź, czy kotek dosięgnął dołu ekranu. """
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def handle_caught(self):
        """ Destroy self if caught. """
        self.destroy()

    def end_game(self):
        """ Zakończ grę. """
        end_message = games.Message(value = "Koniec gry",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)


class Neil(games.Sprite):
    """
    Inhabitant kosmosu, zrzucający małe kotki na Ziemię.
    """
    image = games.load_image("neil.png")

    def __init__(self, y = 55, speed = 2, odds_change = 200):
        super(Neil, self).__init__(image = Neil.image,
                                   x = games.screen.width / 2,
                                   y = y,
                                   dx = speed)

        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
        """ Ustal, czy kierunek ruchu musi zostać zmieniony na przeciwny. """
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
           self.dx = -self.dx

        self.check_drop()


    def check_drop(self):
        """ Zmniejsz licznik odliczający czas lub zrzuć kotka i zresetuj odliczanie. """
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_kitten = Kitten(x = self.x)
            games.screen.add(new_kitten)

            # ustaw margines na mniej więcej 30% wysokości kotka, niezależnie od prędkości kotka
            self.time_til_drop = int(new_kitten.height * 1.3 / Kitten.speed) + 1


def main():
    """ Uruchom grę. """
    space_image = games.load_image("space.jpeg", transparent = False)
    games.screen.background = space_image

    the_bed = Bed()
    games.screen.add(the_bed)

    the_neil = Neil()
    games.screen.add(the_neil)

    games.mouse.is_visible = False
    games.screen.mainloop()

main()
