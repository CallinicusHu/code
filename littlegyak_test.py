from littlegyak import my_player
from littlegyak import System
from littlegyak import Player

def test_score():
    assert (my_player.attack == 4)

def test_score_fail():
    assert (my_player.attack != 484)
    assert (my_player.attack != "panda")


def test_attack(): #if the expected outcome is uncertain how can I know if it is right?

    result = my_player.roll_attack()

    assert (result == int(result))

def test_attack_fail():

    result = my_player.roll_attack()

    assert (result != str(result))

