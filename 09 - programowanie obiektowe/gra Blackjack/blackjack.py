# Blackjack
# od 1 do 7 graczy współzawodniczy z rozdającym

import karty, gry


class BJ_Card(karty.Card):
    """ karta do blackjacka """
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v


class BJ_Deck(karty.Deck):
    """ talia kart do blackjacka """
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(karty.Hand):
    """ ręka w blackjacku """
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # jeśli karta w ręce ma wartość None, to wartość sumy wynosi None
        for card in self.cards:
            if not card.value:
                return None

        # zsumuj wartość kart, traktuj każdego asa jako 1
        t = 0
        for card in self.cards:
            t += card.value

        # ustal czy ręka zawiera asa
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        # jeśli ręka zawiera asa, a suma jest wystarczająco niska, potraktuj asa jako 11
        if contains_ace and t <= 11:
            # dodaj tylko 10 ponieważ już dodaliśmy 1 za asa
            t += 10

        return t

    def is_busted(self):
        return self.total > 21

