# Demonstruje obsługę danych wejściowych z myszy

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Palm(games.Sprite):
    """" Dłoń sterowana myszą"""
    def update(self):
        """ Przejdź do współrzędnych myszy. """
        self.x = games.mouse.x
        self.y = games.mouse.y

def main():
    wall_image = games.load_image("kote.jpg", transparent = False)
    games.screen.background = wall_image

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
