import ex43_atbash_cipher
import random
from textwrap import dedent


# from sys import exit

class Scene(object):

    def __init__(self):
        print(self)

    def enter(self):
        print("you reached here, enter")
        print("actually this never ever happens")


class Engine(object):

    def __init__(self, scene_map):

        self.scene_map = scene_map
        self.room_code = {
            "1": 'central_corridor',
            "2": 'laser_weapon_armory',
            "3": 'the_bridge',
            "4": 'escape_pod',
            "6": 'death',
            "5": 'finished',

            #'central_corridor': "1",
            #'laser_weapon_armory': "2",
            #'the_bridge': "3",
            #'escape_pod': "4",
            #'death': "6",
            #'finished': "5"

        }  # can I somehow SIMPLY get the key from the value? : - ( I did not need it in the end but I would like to know
        #tried google
        #help
        #please
        # : ' (

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

    def where(self, here):
        print(dedent("""Type the room's number into which you wish to go.
            1: Central Corridor
            2: Laser WeaponArmory
            3: The Bridge
            4: Escape Pod
            5: I just want to win.
            6: I just want to die.
            """))
        where = input("< ")

        while True:
            if self.room_code.get(here) == self.room_code.get(where):
                print("Good news: You are already here. Dummy.")
                where = input("< ")
            elif where.isnumeric() and 0 < int(where) < 7:
                return self.room_code.get(where)
            else:
                print("Sorry you might had made a mistake, a typo or simply are retarded.")
                where = input("< ")


class Death(Scene):

    def enter(self):
        print(f"You died, {random.sample(("sad", "mysterious", "not my fault", "for now", "it is fine"), 1)[0]}.")
        exit(0)


class CentralCorridor(Scene):

    def enter(self):
        print("You are at the Central Corridor.")



        return a_game.where("1")

        # return 'laser_weapon_armory'


class LaserWeaponArmory(Scene):

    def enter(self):
        print("This is the Laser Wearpon Armory.")
        """
        print(dedent("""
        # The armory is locked behind a password.
        # There is a password reminder sticked on the door.
        # 'It is brown as a corgi and bear as an otter.'
        # """))
        """
        password = ex43_atbash_cipher.encode(input("... "))

        if password != ex43_atbash_cipher.encode(ex43_atbash_cipher.decode("ivwkz mwz")):
            print(dedent(f"""
        # Your password appears to be incorrect.
        # You have another chance but the air is running out of the room.
        # Luckily you found another password reminder sticker.
        # It says...

        # ivwkz mwz

        # Might be some sort of code."""))
        """
        else:
            print("You were right!")
            return 'the_bridge'

        password = ex43_atbash_cipher.encode(input("... "))

        if password != ex43_atbash_cipher.encode(ex43_atbash_cipher.decode("ivwkz mwz")):
            print("It might be something else. How much air...")
            return 'death'
        else:
            print("You were right this time!")
            return 'the_bridge'
        """
        return a_game.where("2")


class TheBridge(Scene):

    def enter(self):
        print("This is the Bridge.")
        return a_game.where("3")

        #return 'escape_pod'


class EscapePod(Scene):

    def enter(self):
        print("Here is the Escape Pod.")
        return a_game.where("4")

        #return 'finished'


class Finished(Scene):
    def enter(self):
        print("You won! Good job.")

        return 'finished'


class Map(object):

    def __init__(self):
        self.scenes = {
            'central_corridor': CentralCorridor(),
            'laser_weapon_armory': LaserWeaponArmory(),
            'the_bridge': TheBridge(),
            'escape_pod': EscapePod(),
            'death': Death(),
            'finished': Finished(),
        }

    def set_start_scene(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return self.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

    def __str__(self):
        return self.start_scene


a_map = Map()
a_map.set_start_scene("central_corridor")
a_game = Engine(a_map)
a_game.play()

print("The End")
