# Napisz grę, w której gracz steruje postacią, która musi unikać spadających z nieba szczątków.
# Gracz steruje tą postacią za pomocą myszy, a obiekty spadają z nieba.

from livewires import games, color
import random

games.init(screen_width = 800, screen_height = 450, fps = 50)

class Skeleton(games.Sprite):
    """ kościotrup uciekający przed spadającymi szczątkami """
    image = games.load_image("skl.png")

    def __init__(self):
        super(Skeleton, self).__init__(image = Skeleton.image,
                                       x = games.mouse.x,
                                       bottom = games.screen.height)

    def update(self):
        """ Zmień pozycję na wyznaczoną przez współrzędną x myszy. """
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

    def check_catch(self):
        for remains in self.overlapping_sprites:
            remains.handle_caught()



class Remains(games.Sprite):
    """
    Szczątki, które spadają na ziemię.
    """
    image = games.load_image("handy.png")
    speed = 1

    def __init__(self, x, y=0):
        super(Remains, self).__init__(image = Remains.image,
                                      x = x, y = y,
                                      dy = Remains.speed,
                                      interval=300)

    def update(self):
        if self.bottom > games.screen.height:
            self.destroy()

    def tick(self):
        self.drop()

    def drop(self):
        new_handy = Remains(x=random.randint(0,800))
        games.screen.add(new_handy)


    def handle_caught(self):
        self.destroy()
        self.end_game()

    def end_game(self):
        end_message = games.Message(value = "Koniec gry",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)



def main():
    """ Uruchom grę. """
    cem_image = games.load_image("cem.png", transparent = False)
    games.screen.background = cem_image

    skeleton = Skeleton()
    games.screen.add(skeleton)

    remains = Remains(x=random.randint(0,800))
    games.screen.add(remains)



    games.screen.mainloop()


main()
