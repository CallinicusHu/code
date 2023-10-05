four_classes = ["Fighter", "Mage", "Priest", "Rogue"]

#c = 0 # a c számlálni van
new_class = "Yes"

def class_choice():
    print("\nYou may select your class now. \n\nThe Classes are:\n1:", four_classes[0] + "\n2:", four_classes[1] + "\n3:", four_classes[2] + "\n4:", four_classes[3])

    print("\nType the assigned number of the preffered class:", end=" ")
    y = (int(input()))-1

    if 0 > y:
        raise ValueError("You tried to cheat the [] with a 0 or negative number.")
        #Más invalid értékkel amúgy is hibára futott a powershellben.

    return y
# asszem az ebben lévő y független a későbbi y-tól

while new_class == "Yes":
    y = class_choice()
    print("\nYour class:", four_classes[y])
    print("\nAre you happy with your class? Would you like to pick another?\nType:\nYes, if you would like to pick a new class.\nOr\nNo, if you are happy with your class.")
    new_class = input()
    if new_class == "No":
        print("\nGreat! Have fun with your class!")
    elif new_class == "Yes":
        print("\nOkey, pick another one.")
    else:
        raise ValueError("Sorry I can only accept a Yes or No answer!")


Fighter = [
12, 11, 9, 11, # 0-4
13, 9, 10, 11, # 4-8
12, 10, 10, 11, # 8-12
11, 12, 10, 10, # 12-16
13, 10, 10, 10, # 16-20
12, 12, 9, 10] # 20-24

Mage = [
10, 10, 12, 11,
10, 10, 11, 12,
9, 10, 13, 11,
9, 10, 11, 13,
10, 9, 13, 11,
9, 10, 12, 12]

Priest = [
9, 10, 13, 11,
13, 10, 9, 11,
11, 10, 10, 12,
11, 10, 12, 10,
12, 9, 12, 10,
12, 9, 10, 12]

Rogue = [
9, 12, 12, 10,
10, 11, 12, 10,
10, 12, 11, 10,
12, 11, 10, 10,
10, 13, 11, 9,
12, 12, 10, 9]

if four_classes[y] == "Fighter":
    print("""
    12, 11, 9, 11,
    13, 9, 10, 11,
    12, 10, 10, 11,
    11, 12, 10, 10,
    13, 10, 10, 10,
    12, 12, 9, 10
    """)

#print(Fighter[4: 8]) #vajon hogy tudom úgy printelni hogy nem lesznek [ között ] a számok

"""
fighter_sum = 0
mage_sum = 0
priest_sum = 0
rogue_sum = 0

for total in Fighter:
    fighter_sum = fighter_sum + total
print(fighter_sum)
for total in Mage:
    mage_sum = mage_sum + total
print(mage_sum)
for total in Priest:
    priest_sum = priest_sum + total
print(priest_sum)
for total in Rogue:
    rogue_sum = rogue_sum + total
print(rogue_sum)
"""
#teszteltem hogy jól írtam-e be a tulajdonságokat

# Itt tartok, szeretném hogy ismerje a fighter lehetséges attribute sorozatait amiket ki is tud osztani neki.
# Amit nem tudok hogy teszem bele 4 elemű listám egy 6 elemű listába amit utána kioszthatok, az is fix hogy az elem[1] az erő, 2 az ügyesség, stb.
