import room_actions_ex45
import move_actions_ex45

class RunTheGame(object):

    MOVEACTIONS = move_actions_ex45.MoveActions()

    def __init__(self, rooms):
        self.rooms = rooms

    def everything(self, action):
        EVERYTHING = {
            "1": self.MOVEACTIONS.through_door(1),
            "2": self.MOVEACTIONS.through_door(2),
            "3": self.MOVEACTIONS.through_door(3),
            "4": self.MOVEACTIONS.through_door(4),
            "5": self.MOVEACTIONS.through_door(5),
            "6": self.MOVEACTIONS.through_door(6),
            "7": self.MOVEACTIONS.through_door(7),
            "dimension door": self.MOVEACTIONS.dimension_door(),

            "light torch": "room_action",
            "poke wall": "room_action",
            "take loot": "room_action",

            "byby": exit(0)
        }

    def play(self):
        while True:
            action = input("< ")

            if action in self.EVERYTHING:
                self.everything(action)
            #
            # if action == "byby":
            #     exit(0)

