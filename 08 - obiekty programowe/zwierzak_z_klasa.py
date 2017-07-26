# zwierzak z klasą
# demonstruje atrybuty klasy i metody statyczne

class Critter(object):
    """ wirtualny pupil """
    total = 0

    @staticmethod
    def status():
        print("Ogólna liczba zwierzaków wynosi:", Critter.total)
