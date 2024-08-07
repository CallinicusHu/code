from random import randint

x_of_d8 = 16
a_lot = 1 #1_000_000
sample = 5

def d8x():
    #makes a list of xd8 roll outcomes
    return [randint(1, 8) for _ in range(x_of_d8)]

def high_roller():
    #adds together the highest 2 of 3d8 rolls
    roll = d8x()
    return roll.pop(roll.index(max(roll))) + roll.pop(roll.index(max(roll)))

def low_roller():
    #adds together the lowest 2 of 3d8 rolls
    roll = d8x()
    return roll.pop(roll.index(min(roll))) + roll.pop(roll.index(min(roll)))

def roll_high_a_lot():
    #adds together the highest 2 of 3d8 rolls a million times
    return [high_roller() for _ in range (a_lot)]

def roll_low_a_lot():
    # adds together the lowest 2 of 3d8 rolls a million times
    return [low_roller() for _ in range(a_lot)]


def the_big_number_i_need():
    #gives me the average of a million rolls
    lots_of_rolls = roll_high_a_lot()
    return (sum(lots_of_rolls) / len(lots_of_rolls))

def the_small_number_i_need():
    #gives me the average of a million rolls
    lots_of_rolls = roll_low_a_lot()
    return (sum(lots_of_rolls) / len(lots_of_rolls))


gimme_high = "\n".join([f"{the_big_number_i_need()}" for _ in range(sample)])
gimme_low = "\n".join([f"{the_small_number_i_need()}" for _ in range(sample)])

print(f"you rolled with: {x_of_d8}d8 a {a_lot} of times\nbig\n{gimme_high}\nsmall\n{gimme_low}")

