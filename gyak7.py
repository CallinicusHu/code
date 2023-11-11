import random


fallacy = int(input("How many times would you like to roll the dice? "))

def fair_dice(sides):
    dx_collect = 0
    for statistics in range(0, fallacy):
        dx = random.randint(1, sides)
        dx_collect += dx

    print(f"True average: {dx_collect / fallacy}")
    dx_collect = round(dx_collect / fallacy)
    print(f"D{sides}: {dx_collect}\nDifference from average: {dx_collect - (sides / 2)}\n")

fair_dice(4)
fair_dice(6)
fair_dice(8)
fair_dice(10)
fair_dice(12)
fair_dice(20)
fair_dice(100)
fair_dice(1000)
fair_dice(10000)
fair_dice(1000000)
