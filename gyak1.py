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

print(Fighter[4: 8]) #vajon hogy tudom úgy printelni hogy nem lesznek [ között ] a számok

# Itt tartok, szeretném hogy ismerje a fighter lehetséges attribute sorozatait amiket ki is tud osztani neki.
# Amit nem tudok hogy teszem bele 4 elemű listám egy 6 elemű listába amit utána kioszthatok, az is fix hogy az elem[1] az erő, 2 az ügyesség, stb.
