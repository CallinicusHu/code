
class Room(object):

    LOOK = "Empty"
    DOORS = tuple()

    def __init__(self):

        self.trapped = False
        self.dark = True

    def doorlister(self):
        return ", ".join(str(door) for door in self.DOORS)




