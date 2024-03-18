class MoveActions(object):

    def through_door(self, where):
        print("egy")

    def dimension_door(self):
        print("kettő")

    def move_to(self, new_room):
        self.you_are_here = self.rooms[new_room]