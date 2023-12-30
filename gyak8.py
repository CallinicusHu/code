import random

art_tup = ("creo", "intellego", "muto", "perdo", "rego",
           "animal", "aquam", "auram", "corpus", "herbam",
           "ignem", "imaginem", "mentem", "terram", "vim")

art_list = []

for art in art_tup:
    art_list.append(f"{art}:".ljust(10).title())


def create_art_xp_table(max_level):
    art_xp_table = {}
    next_level_cost = 0
    for level in range(1, max_level):
        next_level_cost += level
        art_xp_table.update({level: next_level_cost})
    return art_xp_table


art_xp_table = create_art_xp_table(33)


#for item in art_xp_table:
#    print(item, art_xp_table.get(item))

# for item in art_list:
#    print(item)

def spend_art_xp(art_xp_pool):


    specialize = []
    ignore = []

    for spec in range(random.randint(1, 10)):
        specialize.append(random.randint(0, 14))
    for ign in range(random.randint(0, 4)):
        ignore.append(random.randint(0, 14))
    #print(len(specialize))

    #print("likes: ", end=" ")
    #for spec in specialize:
    #    print(art_tup[spec], end=" ")
    #print("\n")
    #print("dislikes: ", end=" ")
    #for ign in ignore:
    #    print(art_tup[ign], end=" ")

    years = min(max(int(art_xp_pool/30), 1), 5)
    #print("\n", years)

    for xp in range(art_xp_pool):
        which_art = random.randint(0, 14)
        for experience in range(years):
            if which_art not in specialize:
                #print("reroll", which_art)
                which_art = random.randint(0, 14)
        if which_art in ignore:
            which_art = random.randint(0, 14)
        while our_arts_xp.get(art_list[which_art]) == 465:
            which_art = random.randint(0, 14)
        our_arts_xp.update({art_list[which_art]: our_arts_xp.get(art_list[which_art]) + 1})

    our_arts_level = our_arts_xp.copy()

    for art in our_arts_level:
        for level in art_xp_table:
            if our_arts_level.get(art) < art_xp_table.get(level):
                our_arts_level.update({art: level - 1})
                break

    #for art in our_arts_level:
    #    if our_arts_xp.get(art) == 465:
    #        our_arts_level.update({art: 30})

    return our_arts_level


#wizard_name = input("Name your wizard wisely! ")
art_xp_pool = int(input("How much XP our wizard has for arts? "))
our_arts_xp = dict.fromkeys(art_list, 0)

our_arts_level = spend_art_xp(art_xp_pool)

#for item in our_arts_level:
#    print(item, f"XP: {our_arts_xp.get(item)}".ljust(8), "level:", our_arts_level.get(item))


art_xp_and_lvl = []

for art in art_list:
    art_xp_and_lvl.append(f"| {art} Level: {str(our_arts_level.get(art)).ljust(3)} XP: {str(our_arts_xp.get(art)).ljust(3)}| ")

count = 0

art_xp_and_lvl_str = ""

for art in range(15):
    art_xp_and_lvl_str += art_xp_and_lvl[count]

    if (art + 1) % 3 == 0:
        art_xp_and_lvl_str += "\n"

    count += 5
    if count > 14:
        count -= 14

for art in our_arts_level.items():
    print(art)
print(art_xp_and_lvl_str)
