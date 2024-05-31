class Employee(object):

    def __init__(self, name):
        self._name = name
        self._serf = None
        self._boss = None

        self.company = {}

    def who_are_you(self):
        return self._name + " name"

    def set_daddy(self, _boss):
        self._boss = _boss

    def who_is_your_daddy(self):
        return self._boss

    def set_serf(self, _serf):
        self._serf = _serf

    def who_is_your_serf(self):
        return self._serf

    def __str__(self):
        return self._name


class Junior(Employee):
    def __init__(self, name, boss):
        super(Junior, self).__init__(name)
        self._boss = boss

    @property
    def boss(self):
        return self._boss


class Senior(Junior):
    def __init__(self, name, boss, _serf):
        super(Senior, self).__init__(name, boss)
        self._serf = _serf

    @property
    def serf(self):
        return self._serf


class Boss(Employee):
    def __init__(self, name, _serf):
        super(Boss, self).__init__(name)
        self._serf = _serf

    @property
    def serf(self):
        return self._serf


aba = Junior("aba", None)
bob = Senior("bob", None, aba)
cad = Senior("cad", None, bob)
dud = Boss("dud", cad)

aba.set_daddy(bob)
bob.set_daddy(cad)
cad.set_daddy(dud)

# bob.who_are_you()
# bob.who_is_your_serf()
# bob.who_is_your_daddy()
# print()
# print(bob)
# print(company.get("bob"))
# print()
# print(bob.boss)
# print()

# print()
# for person in company:
#     try:
#         if company.get(person)._serf == "":
#             print(f"{company.get(person)} has no serf""")
#         else:
#             print(company.get(person), end=" ")
#             print(company.get(person).who_is_your_serf())
#     except TypeError:
#         print("typeerror")
#     except:
#         print(f"{person} has no serf")
# print()
#
# print(bob.serf, " bobserf")
# print(bob.who_is_your_serf(), " bobserfmethod")
# print()
#
# print(dud.serf, " dudsserf")
# print(dud.who_is_your_serf(), " dudserfemethod")
#
# print(aba.boss, " ababoss")
# print(aba.who_is_your_daddy(), " ababossmethod")
#
# # dud serfje cad serfje bob serfje kicsoda

print("new test")

print(dud)
print(dud.who_is_your_serf().who_is_your_serf().who_is_your_serf())

