import random


class Veteran:
    def __new__(cls, *args, **kwargs): #*args, **kwargs are some kind of placeholders here?
        print(f'A generic {cls} materializes before you.') #shouldn't the print only say "Veteran"?

        return super().__new__(cls)

    def __init__(self, name):
        print(f"It's name is {name}.")
        self.name = name
        self.attack_bonus = 5
        self.damage_bonus = 3
        self.is_shortsword_drawn = False

    def multiattack(self, target):
        self.longsword(target)
        self.longsword(target)
        if self.is_shortsword_drawn:
            self.shortsword(target)

    def longsword(self, target):
        print(f'\n{self.name} {str(Veteran)} attacks {target} with a longsword:')
        held_in_one_hand = self.is_shortsword_drawn
        if held_in_one_hand:
            self.attack(target, 8)
        else:
            self.attack(target, 10)

    def shortsword(self, target):
        print(f'\n{self.name} {str(Veteran)} attacks {target} with a shortsword:')
        self.attack(target, 6)

    def attack(self, target, damage_dice_size):
        print(f'{target} loses {random.randint(1, damage_dice_size) + self.damage_bonus} hit points '
              f'if their AC is {random.randint(1, 20) + self.attack_bonus} or lower.')

    def draw_shortsword(self):
        if not self.is_shortsword_drawn:
            print(f'\n{self.name} draws a vicious shortsword with its off-hand.')
            self.is_shortsword_drawn = True


print("You are adventuring in the expensively rendered shithole called Baldur's Gate.")

clueless_adventurer = input('How shalt I call thee? ')

handler_zodge = Veteran('Captain Zodge')

handler_zodge.multiattack(clueless_adventurer)

handler_zodge.draw_shortsword()
handler_zodge.multiattack(clueless_adventurer)
