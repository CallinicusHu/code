DIRECTIONS = ("north", "south", "east", "west", "down", "up", "left", "right", "back")
VERBS = ("go", "stop", "kill", "eat")
STOPS = ("the", "in", "of", "from", "at", "it")
NOUNS = ("door", "bear", "princess", "cabinet")


def scan(stuff):
    words = stuff.split()

    commands = []

    for word in words:
        test_word = word.lower()
        if test_word in DIRECTIONS:
            commands.append(('direction', word))
        elif test_word in VERBS:
            commands.append(('verb', word))
        elif test_word in STOPS:
            commands.append(('stop', word))
        elif test_word in NOUNS:
            commands.append(("noun", word))
        elif test_word.isnumeric():
            commands.append(("number", int(word)))
        else:
            commands.append(("error", word))

    return commands

print(scan("Kill the bear."))
