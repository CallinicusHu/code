four_paths = ["Fighter", "Mage", "Priest", "Rogue"]

# c = 0 # a c számlálni van
new_path = "Yes"


def path_choice():
    print("\nYou may select your path now. \n\nThe Paths are:\n1:", four_paths[0] + "\n2:", four_paths[1] + "\n3:",
          four_paths[2] + "\n4:", four_paths[3])

    print("\nType the assigned number of the preferred path:", end=" ")
    y = (int(input())) - 1

    if 0 > y:
        raise ValueError("You tried to cheat the [] with a 0 or negative number.")
        # Más invalid értékkel amúgy is hibára futott a powershellben.

    return y # az y a kaszt sorszáma


# asszem az ebben lévő y független a későbbi y-tól

while new_path == "Yes":
    y = path_choice()
    print("\nYour path:", four_paths[y])
    print(
        "\nAre you happy with your path? Would you like to pick another?\nType:\nYes, if you would like to pick a new path.\nOr\nNo, if you are happy with your path.")
    new_path = input()
    if new_path == "No":
        print("\nGreat! Have fun with your path!")
    elif new_path == "Yes":
        print("\nOkey, pick another one!")
    else:
        raise ValueError("Sorry I can only accept a Yes or No answer!")

your_path = four_paths[y]

fighter = [
    12, 11, 9, 11,  # 0-3
    13, 9, 10, 11,  # 4-7
    12, 10, 10, 11,  # 8-11
    11, 12, 10, 10,  # 12-15
    13, 10, 10, 10,  # 16-19
    12, 12, 9, 10]  # 20-23

mage = [
    10, 10, 12, 11,
    10, 10, 11, 12,
    9, 10, 13, 11,
    9, 10, 11, 13,
    10, 9, 13, 11,
    9, 10, 12, 12]

priest = [
    9, 10, 13, 11,
    13, 10, 9, 11,
    11, 10, 10, 12,
    11, 10, 12, 10,
    12, 9, 12, 10,
    12, 9, 10, 12]

rogue = [
    9, 12, 12, 10,
    10, 11, 12, 10,
    10, 12, 11, 10,
    12, 11, 10, 10,
    10, 13, 11, 9,
    12, 12, 10, 9]


def print_possible_statblocks(y):
    if four_paths[y] == "Fighter":
        print("""
           ST  AG  IN  WI
        1: 12, 11,  9, 11,
        2: 13,  9, 10, 11,
        3: 12, 10, 10, 11,
        4: 11, 12, 10, 10,
        5: 13, 10, 10, 10,
        6: 12, 12,  9, 10
        """)

    if four_paths[y] == "Mage":
        print("""
           ST  AG  IN  WI
        1: 10, 10, 12, 11,
        2: 10, 10, 11, 12,
        3:  9, 10, 13, 11,
        4:  9, 10, 11, 13,
        5: 10,  9, 13, 11,
        6:  9, 10, 12, 12
        """)

    if four_paths[y] == "Priest":
        print("""
           ST  AG  IN  WI
        1:  9, 10, 13, 11,
        2: 13, 10,  9, 11,
        3: 11, 10, 10, 12,
        4: 11, 10, 12, 10,
        5: 12,  9, 10, 12,
        6: 11,  9, 10, 13
        """)

    if four_paths[y] == "Rogue":
        print("""
           ST  AG  IN  WI
        1:  9, 12, 12, 10,
        2: 10, 11, 12, 10,
        3: 10, 12, 11, 10,
        4: 12, 11, 10, 10,
        5: 10, 13, 11,  9,
        6: 12, 12, 10,  9
        """)


def select_attribute_line(line): # todo: többi kasztok, hiba ha nem 1-6 van megadva
    line = int(line)
    if y == 0:
        st = fighter[line * 4 - 4]
        ag = fighter[line * 4 - 3]
        agy = fighter[line * 4 - 2] #az intellectet nehéz rövidíteni mert az int és in is másra kell az agy meg nem jó mert olyan mint az ag vagy agi az ész meg ékezetes olyant nem akarok
        wil = fighter[line * 4 - 1]
        print(f"\nStrength: {st}\nAgility: {ag}\nIntellect: {agy}\nWill: {wil}")
    """
    print(st)
    print(ag)
    print(agy)
    print(wil)
"""

print("\nHere is the list of your possible Attribute scores:")
print_possible_statblocks(y)
print("Chose one of the lines from the list, by typing the count number of the line: ", end="")
select_attribute_line(input()) # todo: egy statjaid lista amibe a statjaid kerülnek amiket megadsz a select_attribute_lineal


# print(Fighter[4: 8]) #vajon hogy tudom úgy printelni hogy nem lesznek [ között ] a számok

"""
fighter_sum = 0
mage_sum = 0
priest_sum = 0
rogue_sum = 0

for total in fighter:
    fighter_sum = fighter_sum + total
print(fighter_sum)
for total in mage:
    mage_sum = mage_sum + total
print(mage_sum)
for total in priest:
    priest_sum = priest_sum + total
print(priest_sum)
for total in rogue:
    rogue_sum = rogue_sum + total
print(rogue_sum)
"""
# teszteltem hogy jól írtam-e be a tulajdonságokat

# Itt tartok, szeretném hogy ismerje a fighter lehetséges attribute sorozatait amiket ki is tud osztani neki.
# Amit nem tudok hogy teszem bele 4 elemű listám egy 6 elemű listába amit utána kioszthatok, az is fix hogy az elem[1] az erő, 2 az ügyesség, stb.
