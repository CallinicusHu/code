import random


class System(object):

    def __init__(self):
        pass

    def roll_check(self, score):  # how can you do this without the score argument?
        numbers = []
        print("your score is: ", score)
        for number in range(max(score, 3)):

            numbers.append(random.randint(1, 5))

        numbers.sort(reverse=True)


        return numbers[0] + numbers[1] + numbers[2]


class Player(object):

    def __init__(self, attack, defense, petting):
        self.attack = attack
        self.defense = defense
        self.petting = petting

    def roll_attack(self):
        return system.roll_check(self.attack)

    def roll_defense(self):
        return system.roll_check(self.attack)

    def roll_petting(self):
        return system.roll_check(self.attack)


system = System()
my_player = Player(4, 8, 2)

print(my_player.roll_attack())
