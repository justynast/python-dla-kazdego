# Demonstruje wykrywanie kolizji duszków

from livewires import games
import random

games.init(screen_width = 1000, screen_height = 562, fps = 50)

class Palm(games.Sprite):
    """" Dłoń sterowana za pomocą myszy. """
    def update(self):
        """ Przesuń do pozycji myszy. """
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()

    def check_collide(self):
        """ Sprawdź, czy nie doszło do kolizji z kociakiem. """
        for kitten in self.overlapping_sprites:
            kitten.handle_collide()

class Kitten(games.Sprite):
    """" Nieuchwytny kociak. """
    def handle_collide(self):
        """ Przemieść się w przypadkowe miejsce ekranu. """
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)


def main():
    background_image = games.load_image("kociaki.png", transparent = False)
    games.screen.background = background_image

    kitten_image = games.load_image("kociak.png")
    kitten_x = random.randrange(games.screen.width)
    kitten_y = random.randrange(games.screen.height)
    the_kitten = Kitten(image = kitten_image, x = kitten_x, y = kitten_y)
    games.screen.add(the_kitten)

    palm_image = games.load_image("hand.png")
    the_palm = Palm(image = palm_image,
                  x = games.mouse.x,
                  y = games.mouse.y)
    games.screen.add(the_palm)

    games.mouse.is_visible = False

    games.screen.event_grab = True

    games.screen.mainloop()

# wystartuj!
main()
