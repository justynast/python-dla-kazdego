# Demonstruje postępowanie po osiągnięciu granic ekranu

from livewires import games

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Heart(games.Sprite):
    def update(self):
        """ Po osiągnięciu brzegu ekranu zmień wartość składowej prędkości na przeciwną. """
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx

        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy

def main():
    wall_image = games.load_image("kote.jpg", transparent=False)
    games.screen.background = wall_image

    heart_image = games.load_image("heart.gif")
    heart = Heart(image=heart_image,
                         x=games.screen.width/2,
                         y=games.screen.height/2,
                         dx=1,
                         dy=1)

    games.screen.add(heart)


    games.screen.mainloop()

# wystartuj!
main()
