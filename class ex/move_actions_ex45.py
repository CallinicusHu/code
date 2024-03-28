class MoveActions(object):

    def __init__(self, rooms):

        self.rooms = rooms
        self.you_are_here = self.rooms[1]

    def door(self, door_type):
        try:
            where = int(input("Where do you wanna end up? "))
            if ((door_type == "normal door" and where in self.you_are_here.DOORS)
                    or door_type == "dimension door"):
                self.you_are_here = self.rooms[where]
                print(self.you_are_here.LOOK)
                print(f"You may leave through the following doors: {str(self.you_are_here.DOORS)[1:-1:]}")
            else:
                print("Cannot go there!")

        except (KeyError, ValueError):
            print(": - ((")
