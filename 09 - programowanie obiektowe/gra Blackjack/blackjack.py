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
