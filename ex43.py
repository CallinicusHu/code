import ex43_atbash_cipher
import random
from textwrap import dedent
#from sys import exit

class Scene(object):

    def enter(self):
        print("you reached here, enter")
        print("actually this never ever happens")


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    def enter(self):
        print(f"You died, {random.sample(("sad", "mysterious", "not my fault", "for now", "it is fine"), 1)[0]}.")
        exit(0)



class CentralCorridor(Scene):

    def enter(self):
        print("You are here.")




        #return 'death'

        return 'laser_weapon_armory'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            The armory is locked behind a password.
            There is a password reminder sticked on the door.
            'It is brown as a corgi and bear as an otter.'
            """))

        password = ex43_atbash_cipher.encode(input("... "))

        if password != ex43_atbash_cipher.encode(ex43_atbash_cipher.decode("ivwkz mwz")):
            print(dedent(f"""
            Your password appears to be incorrect.
            You have another chance but the air is running out of the room.
            Luckily you found another password reminder sticker.
            It says...
            
            ivwkz mwz

            Might be some sort of code."""))

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



class TheBridge(Scene):

    def enter(self):
        print("this time we are here")

class EscapePod(Scene):

    def enter(self):
        pass

class Finished(Scene):
    def enter(self):
        print("You won! Good job.")
        exit(0)


class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

print("end")