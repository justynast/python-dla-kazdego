# Demonstruje obracanie duszka

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Panda(games.Sprite):
    """ Poruszająca i obracająca się panda. """
    def update(self):
        """ obróć w zależności od naciśniętych klawiszy"""
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += 1
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= 1

        #Kieruj ruchem pandy na podstawie wciśniętych klawiszy.
        if games.keyboard.is_pressed(games.K_w):
            self.y -= 1
        if games.keyboard.is_pressed(games.K_s):
            self.y += 1
        if games.keyboard.is_pressed(games.K_a):
            self.x -= 1
        if games.keyboard.is_pressed(games.K_d):
            self.x += 1

def main():
    nebula_image = games.load_image("nebula.jpg", transparent = False)
    games.screen.background = nebula_image

    panda_image = games.load_image("panda.png")
    the_panda = Panda(image = panda_image,
                    x = games.screen.width/2,
                    y = games.screen.height/2)
    games.screen.add(the_panda)

    games.screen.mainloop()

main()
