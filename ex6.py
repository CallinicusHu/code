types_of_people = 10
x = f"There are {types_of_people} types of people."
types_of_people = 5
print(x)


binary = "binary"
do_not = "don't"
y = f"Those who {binary} and tho who {do_not}."

print(x)
print(y)

print(f"I said: '{y}'")

#hilarious = "13 False"
#joke_evaluation = "Isn't that joke so funny?! {}"

#print(joke_evaluation.format(hilarious))
print("Isn't that joke so funny?! {}".format((False, True)))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
