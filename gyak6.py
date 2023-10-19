macska = 0

def kert(macska):
    macska = macska +11
    print(macska)

kert(macska)

print(macska)

def haz(macska):
    macska = macska +11
    print(macska)
  #  macska = haz(macska)
    return macska

macska = haz(5)

print(macska)