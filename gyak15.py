class Truck(object):
    def __init__(self, name):
        self.name = name  # callsign of the truck
        self.position = 0  # distance from home
        self.route = None  # A or B route
        self.cargo = False  # it is empty

    def move(self, packages):  # packages is list_of_packages

        if self.position == 0 and packages:
            if packages[0] == "A":
                self.route = "A"
            elif packages[0] == "B":
                self.route = "B"
            self.cargo = True
            self.position = self.position + 1
            packages = packages[1:]

        elif self.route == "B" and self.position != 0:
            if self.position < 5 and self.cargo:
                self.position += 1
                if self.position == 5:
                    self.cargo = False
            else:
                self.position -= 1

        elif self.route == "A" and self.position == 1:
            self.cargo = False
            self.position -= 1

        if self.position == 0:
            self.route = None

        return packages


class Ship(Truck):
    def __init__(self):
        super().__init__("a_ship")
        self.port = ""

    def shipping(self, a_truck, b_truck):
        if a_truck.route == "A" and a_truck.position == 1:
            self.port += "A"
        if b_truck.route == "A" and b_truck.position == 1:
            self.port += "A"

        if not self.cargo and self.port and self.position == 0:
            self.cargo = True
            self.port = self.port[1:]
        elif not self.cargo and self.position > 0:
            self.position -= 1

        if self.position != 4 and self.cargo:
            self.position += 1

        if self.position == 4 and self.cargo:
            self.cargo = False


def delivery_timer(list_of_packages):
    worktime = 0
    a_truck = Truck("a_truck")
    b_truck = Truck("b_truck")
    a_ship = Ship()

    while True:

        worktime += + 1

        a_ship.shipping(a_truck, b_truck)

        if len(list_of_packages) > 0 and not (list_of_packages[0] == "A" or list_of_packages[0] == "B"):
            return f"error at worktime {worktime} invalid package in {list_of_packages}"

        list_of_packages = a_truck.move(list_of_packages)

        if len(list_of_packages) > 0 and not (list_of_packages[0] == "A" or list_of_packages[0] == "B"):
            return f"error at worktime {worktime} invalid package in {list_of_packages}"

        list_of_packages = b_truck.move(list_of_packages)

        print()
        print(a_truck.name, "pos", a_truck.position, "cargo", a_truck.cargo, "route", a_truck.route, "worktime",
              worktime)
        print(b_truck.name, "pos", b_truck.position, "cargo", b_truck.cargo, "route", b_truck.route, "worktime",
              worktime)
        print(a_ship.name, "pos", a_ship.position, "cargo", a_ship.cargo)

        if not a_truck.cargo and not b_truck.cargo and not list_of_packages and not a_ship.port and not a_ship.cargo:
            return worktime
