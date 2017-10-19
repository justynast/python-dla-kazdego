# Nowe okno graficzne
# Demonstruje tworzenie okna graficznego

from livewires import games

games.init(screen_width=640, screen_height=480, fps=50)

wall_image = games.load_image("kote.jpg", transparent=False)
games.screen.background = wall_image

heart_image = games.load_image("heart.gif")
heart = games.Sprite(image=heart_image,
                     x=games.screen.width/2,
                     y=games.screen.height/2,
                     dx=1,
                     dy=1)

games.screen.add(heart)


games.screen.mainloop()
