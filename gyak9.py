import random


class Yielder(object):

    D20 = lambda: random.randint(1, 20)
    SWORD = lambda: random.randint(1, 8)

    def __init__(self):
        self.hp = random.randint(10, 100)
        self.atk = random.randint(-5, 10)
        self.ac = random.randint(10, 20)
        self.dmg = random.randint(-3, 5)
        print("Here ends the init.")

    print("Are we ever here?") #yes actually before the init starts

    def yield_some_stuff(self): #but this never starts

        print("Lets fight the bundáskenyér.") #even this print fails to run

        count = 0
        turns = 0

        while self.hp > 0: #actually I don't know if this works or not because it doesn't even start

            if Yielder.D20() + self.atk >= self.ac:
                self.hp -= max(0, Yielder.SWORD() + self.dmg)
                #yield print(self.hp) #I am not exactly what this is useful but surely is
                count += 1
                print(f"The bundáskenyér only has {self.hp} left. This was the {count}. time you hit it.")

            else:
                print("Missed it!")

            #yield print(turns)
            turns += 1
        print(f"The bundáskenyér took {turns} turns.")


yilding = Yielder()
yilding.yield_some_stuff() #does not run I don't know why


class Jutalmak(object):

    def jutalmazzunk_1(self):
        jutalom = min(5, int(input("You are the GM you have to offer some bundáskenyérs to your players: ")))
        print(f"Your players took your generous offer of {jutalom} bundáskenyérs.")

    def jutalmazzunk_2(self):
        jutalom = int(input("You are the GM you have to offer some bundáskenyérs to your players: "))

        if jutalom < 5:
            print("The players nodded at your offer.")
        else:
            print(f"One of the players say: \"So it is Tuesday\" again.")


juti = Jutalmak()
juti.jutalmazzunk_1()
juti.jutalmazzunk_2()

player_skill = None
stuff_on_character_sheet = None
stuff_we_agreed_with_dm = None
def dobat_a_dm():
    print("Dobj meggyőzést.")
    stuff_we_agreed_with_dm = None
    dob_a_jatekos = random.randint(1,20)
    + player_skill + stuff_on_character_sheet + stuff_we_agreed_with_dm
    if dob_a_jatekos >= dob_a_jatekos - 1:
        return "Bementek a dungeonbe."
