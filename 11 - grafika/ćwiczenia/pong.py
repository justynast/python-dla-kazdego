# Utwórz prostą grę Pong dla 1 gracza, w której gracz steruje paletką a piłeczka odbija się od trzech ścian.
# Jeśli piłeczka przejdzie obok paletki następuje koniec gry.

from livewires import games, color
import random

games.init(screen_width = 800, screen_height = 600, fps = 50)

class Bat(games.Sprite):
    """ paletka sterowana myszką gracza"""
    image = games.load_image("bat.png", transparent=False)

    def __init__(self):
        super(Bat, self).__init__(image=Bat.image,
                                  x = games.mouse.x,
                                  bottom=games.screen.height)

    def update(self):
        """ zmień pozycję za pomocą myszy """
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()

    def check_catch(self):
        """ sprawdź czy paletka dotyka piłki"""
        for ball in self.overlapping_sprites:
            ball.handle_caught()

class Ball(games.Sprite):
    image = games.load_image("ball.png")

    def __init__(self):
        super(Ball, self).__init__(image=Ball.image,
                                   x = random.randint(0,games.screen.width),
                                   y = games.screen.height/2,
                                   dy = 2,
                                   dx = 2)

    def update(self):
        """ Po osiągnięciu brzegu ekranu zmień wartość składowej prędkości na przeciwną. """
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx

        if self.top < 0:
            self.dy = -self.dy

        # zakończ grę, jeśli piłka przejdzie obok paletki
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def handle_caught(self):
        """ odbij piłeczkę """
        self.dy = -self.dy

    def end_game(self):
        """ wyświetl wiadomość na koniec gry """
        end_message = games.Message(value = "Koniec gry",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 3 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)

def main():
    """ uruchom grę """

    bat = Bat()
    games.screen.add(bat)

    ball = Ball()
    games.screen.add(ball)

    games.screen.mainloop()

main()
