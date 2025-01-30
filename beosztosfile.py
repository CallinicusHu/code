import csv

def csinálj_listát_belőle(file):

    listánk = []

    with open(file, newline='') as csvfile:
        nyit = csv.reader(csvfile, delimiter=',')
        for row in nyit:
            listánk.append(row)

    del listánk[0]

    formázott_listánk = []

    for sor, játék in enumerate(listánk):
        formázott_listánk.append([])
        for oszlop, elem in enumerate(játék):
            if elem:
                formázott_listánk[sor].append(elem)

    return formázott_listánk


def beosztó(eztet):

    beosztva = []

    for hanyadik, játék in enumerate(eztet):

        beosztva.append(Játék(
            játék[1],
            játék[2],
            játék[3],
            játék[4],
            játék[5:],
            játék[0]))

    return beosztva

class Játék(object):

    def __init__(self, minimum, maximum, mesélő, cím, jelentkezők, nap):
        self.minimum_létszám = minimum
        self.maximum_létszám = maximum
        self.mesélő = mesélő
        self.cím = cím
        self.jelentkezők = jelentkezők
        self.nap = nap

    def __str__(self):
        return (f"{self.minimum_létszám}, "
                f"{self.maximum_létszám}, "
                f"{self.mesélő}, "
                f"{self.cím}, "
                f"{self.jelentkezők}, "
                f"{self.nap}")

játékbeosztás = csinálj_listát_belőle("beosztosfile.csv")
beosztott = csinálj_listát_belőle("beosztott.csv")

print(

)
print(beosztott[0]
      )
print()
