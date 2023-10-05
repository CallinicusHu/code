x = ["Egy", "Kettő", "Három", "Négy", "Öt"]

c = 0

while c < 5:
    print(x[c])
    c += 1

print("\n")

for c in range(0, 5):
    print(c)
    c += 1 #nem csinál semmit vagy nem tudjuk
    print(c)


print("\n")

for word in x:
    print(word)

print("\n")

for word in x:
    print(x)

print("\n")

list_words = []

for word in x:
    list_words.append(word)
    print(list_words)
