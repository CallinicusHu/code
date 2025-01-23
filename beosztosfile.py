import csv

játékbeosztás = []

with open('beosztosfile.csv', newline='') as csvfile:
    játékbeosztásnyit = csv.reader(csvfile, delimiter=',')
    for row in játékbeosztásnyit:
        játékbeosztás.append(row)

fejléc = játékbeosztás[0]
del játékbeosztás[0]

játékbeosztás_formázva = []

for sor, játék in enumerate(játékbeosztás):
    játékbeosztás_formázva.append([])
    for oszlop, elem in enumerate(játék):
        if elem:
            játékbeosztás_formázva[sor].append(elem)


csütörtök = játékbeosztás_formázva[:8]
péntek = játékbeosztás_formázva[8:15]
szombat = játékbeosztás_formázva[15:22]

class Játék(object):

    def __init__(self, minimum, maximum, mesélő, cím, jelentkezők, nap):
        self.minimum_létszám = minimum
        self.maximum_létszám = maximum
        self.mesélő = mesélő
        self.cím = cím
        self.jelentkezők = jelentkezők
        self.nap = nap

játékok = []

for játék in játékbeosztás:

    játékok.append(Játék(
        játék[0],
        játék[1],
        játék[2],
        játék[3],
        játék[4:]

    ))