""" A	5
    AB	5
    BB	5
    ABB	7
    AABABBAB	?
    ABBBABAAABBB	?
"""


class Truck(object):
    def __init__(self, name):
        self.name = name  # callsign of the truck
        self.position = 0  # distance from home
        self.route = None  # A or B route
        self.cargo = False  # it is empty


def delivery_timer(list_of_packages) -> int:
    worktime = 0
    a_truck = Truck("a_truck")
    b_truck = Truck("b_truck")
    number_of_packages = len(list_of_packages)

    while True:


        worktime = worktime + 1

        if a_truck.position == 0 and list_of_packages:
            a_truck.route = "B"
            a_truck.cargo = True
            a_truck.position = a_truck.position + 1
            list_of_packages = list_of_packages[1:]

        elif a_truck.route == "B" and a_truck.position != 0:
            if a_truck.position < 5:
                a_truck.position += 1
                if a_truck.position == 5:
                    a_truck.cargo = False
            else:
                a_truck.position -= 1

        if b_truck.position == 0 and list_of_packages:
            b_truck.route = "B"
            b_truck.cargo = True
            b_truck.position = b_truck.position + 1
            list_of_packages = list_of_packages[1:]

        elif b_truck.route == "B" and b_truck.position != 0:
            if b_truck.position < 5:
                b_truck.position += 1
                if b_truck.position == 5:
                    b_truck.cargo = False
            else:
                b_truck.position -= 1


        if a_truck.position == 0:
            a_truck.route = None

        if b_truck.position == 0:
            b_truck.route = None

        print()
        print(a_truck.name, a_truck.position, a_truck.cargo, a_truck.route, "worktime", worktime)
        print(b_truck.name, b_truck.position, b_truck.cargo, b_truck.route, "worktime", worktime)

        if not a_truck.cargo and not b_truck.cargo and not list_of_packages:
            return worktime

        if worktime == 20:
            return worktime


    # return delivery_time
