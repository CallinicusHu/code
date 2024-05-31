import room_actions_ex45
import move_actions_ex45

class RunTheGame(object):

    def __init__(self, rooms):
        self.MOVEACTIONS = move_actions_ex45.MoveActions(rooms)

        self.EVERYTHING = {
            "normal door": lambda a: self.MOVEACTIONS.door(a),
            "dimension door": lambda a: self.MOVEACTIONS.door(a),

            "light torch": "room_action",
            "poke wall": "room_action",
            "take loot": "room_action",

            "byby": lambda a: exit(0)
        }


    def play(self):

        print("You are in the 1st room, you can go to room 2 or 4.")

        while True:
            action = input("< ")

            if action in self.EVERYTHING:
                self.EVERYTHING[action](action)




