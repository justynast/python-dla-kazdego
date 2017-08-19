# gra w karty 3.0
# demonstruje dziedziczenie - przesłanianie metod


class Card(object):
    """ Karta do gry """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Unprintable_Card(Card):
    """ karta, której ranga i kolor nie są ujawniane przy jej wyświetleniu """
    def __str__(self):
        return "<utajniona>"


class Positionable_Card(Card):
    """ karta, która może być odkryta lub zakryta """
    def __init__(self, rank, suit, face_up = True):
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up
