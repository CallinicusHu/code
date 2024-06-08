from littlegyak import first_player, second_player
from littlegyak import System
from littlegyak import Player

def test_score():
    assert (first_player.attack == 4)

def test_score_fail():
    assert (first_player.attack != 0)


def test_roll_fail():
    assert (first_player.roll_attack != 484)
    assert (first_player.roll_attack != "panda")
    assert (second_player.roll_defense != (1, 2))
    assert (second_player.roll_petting != {"party": "fidessz"})


def test_attack(): #if the expected outcome is uncertain how can I know if it is right?

    result = first_player.roll_attack()

    assert (result == int(result))

def test_attack_fail():

    result = first_player.roll_attack()

    assert (result != str(result))

def test_defense():

    result = second_player.roll_defense()

    assert (result == int(result))


def test_petting_fail():

    result = second_player.roll_petting()

    assert (result != str(result))