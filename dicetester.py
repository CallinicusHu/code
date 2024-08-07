from random import randint

x_of_d8 = max(2, int(input("how many d8s? ")))
a_lot = int(input("how many rolls? "))
sample = int(input("how many tries? "))

def d8x():
    #makes a list of xd8 roll outcomes
    return sorted([randint(1, 8) for _ in range(x_of_d8)])

def high_roller():
    #adds together the highest 2 of xd8 rolls
    roll = d8x()
    return roll[-1] + roll[-2]

def low_roller():
    #adds together the lowest 2 of xd8 rolls
    roll = d8x()
    return roll[0] + roll[1]

def roll_high_a_lot():
    #adds together the highest 2 of xd8 rolls a lot of times
    return [high_roller() for _ in range (a_lot)]

def roll_low_a_lot():
    # adds together the lowest 2 of xd8 rolls a lot of times
    return [low_roller() for _ in range(a_lot)]


def the_big_number_i_need():
    #gives me the average of a lot of big rolls
    ave = (sum(roll_high_a_lot()) / a_lot)
    rounding = ave - int(ave)
    roughave = round(ave)
    if rounding >= 0.7 or rounding <= 0.3:
        return roughave
    else:
        return f"{roughave}-{roughave + 1}"

def the_small_number_i_need():
    #gives me the average of a lot of small rolls
    ave = (sum(roll_low_a_lot()) / a_lot)
    rounding = ave - int(ave)
    roughave = round(ave)
    if rounding >= 0.7 or rounding <= 0.3:
        return roughave
    else:
        return f"{roughave}-{roughave + 1}"

gimme_high = "\n".join([f"{the_big_number_i_need()}" for _ in range(sample)])
gimme_low = "\n".join([f"{the_small_number_i_need()}" for _ in range(sample)])

print(f"you rolled with: {x_of_d8}d8 a {a_lot} of times\nbig\n{gimme_high}\nsmall\n{gimme_low}")

