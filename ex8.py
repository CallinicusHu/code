formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, ",", formatter, ",", formatter, ",", formatter))
print(formatter, formatter)
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
print(formatter.format(1, 2, 3, 4))

def valami (a, b):
    return a + b

print(valami(1, 2))

#print(valami(1, 2, 3))
