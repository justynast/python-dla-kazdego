# pogromca obcych
# demonstruje współdziałanie obiektów

class Player(object):
    """Gracz w grze strzelance"""
    def blast(self, enemy):
        print("Gracz razi wroga.\n")
        enemy.die()

class Alien(object):
    """Obcy w grze strzelance"""
    def die(self):
        print("Obcy z trudem łapie oddech: 'To już koniec. Ale wielki koniec...\n"
              "Powiedz moim dwóm milionom larw, że je kochałem...'")

# main
print("\t\tŚmierć Obcego\n")
hero = Player()
invader = Alien()

hero.blast(invader)

input("\n\nAby zakończyć naciśnij klawisz Enter")
