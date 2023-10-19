import math

xp = 15
age = 0
total_xp = 0

while xp > 0.0:
    total_xp = total_xp+xp
    age += 1
    xp = 15 - (math.floor(age/20))

print("15 xp / year, yearly decreased by 1/20 of age:")
print("Total xp: ", total_xp)
print("Final age: ", age)
print("\n")

spring_xp = 2
summer_xp = 2
autumn_xp = 7
winter_xp = 4

age = 0
total_xp = 0

while autumn_xp > 0:
    age += 1
    total_xp = (total_xp + spring_xp + summer_xp + autumn_xp + winter_xp)
    if autumn_xp > 0:
        autumn_xp = 7 - (math.floor(age/20))
    if summer_xp > 0:
        summer_xp = 2 - (math.floor(age/20))
    if spring_xp > 0:
        spring_xp = 2 - (math.floor(age/20))
    if winter_xp > 0:
        winter_xp = 4 - (math.floor(age/20))

print("Total xp with seasonly XP of 2+2+4+7:", total_xp)
print("Final age:", age)