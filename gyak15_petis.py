import json


class Log(object):
    def __init__(self, packages):
        with open("truck_log_petis", "w", encoding="UTF-8") as truck_log_petis:
            truck_log_petis.write(f"# Deliver {packages}\n")

        self.transport_id = 0
        self.cargo_id = 0

    def create_log(self, event, time, transport_id, kind, location, v_destination=None, cargo_id=None,
                   c_destination=None,
                   origin=None):
        with open("truck_log_petis", "a", encoding="UTF-8") as truck_log_petis:
            if cargo_id and v_destination:
                truck_log_petis.write(
                    f'\u007b"event": "{event}", "time": {time}, "transport_id": {transport_id}, "kind": "{kind}", "location": "{location}", "destination": "{v_destination}", "cargo": [\u007b"cargo_id": {cargo_id}, "destination": "{c_destination}", "origin": "{origin}"\u007d]\u007d')
            elif not cargo_id and v_destination:
                truck_log_petis.write(
                    f'\u007b"event": "{event}", "time": {time}, "transport_id": {transport_id}, "kind": "{kind}", "location": "{location}", "destination": "{v_destination}"\u007d')
            elif cargo_id and not v_destination:
                truck_log_petis.write(
                    f'\u007b"event": "{event}", "time": {time}, "transport_id": {transport_id}, "kind": "{kind}", "location": "{location}", "cargo": [\u007b"cargo_id": {cargo_id}, "destination": "{c_destination}", "origin": "{origin}"\u007d]\u007d')
            elif not cargo_id and not v_destination:
                truck_log_petis.write(
                    f'\u007b"event": "{event}", "time": {time}, "transport_id": {transport_id}, "kind": "{kind}", "location": "{location}" \u007d')
            truck_log_petis.write("\n")


class Truck(object):
    def __init__(self, name, truck_log_petis):
        self.name = name  # callsign of the truck
        self.position = 0  # distance from home
        self.route = None  # A or B route
        self.cargo = False  # it is empty
        self.truck_log_petis = truck_log_petis
        self.my_transport_id = 0
        self.my_cargo_id = 0
        self.sleep = True

    def peti_move(self, packages, worktime):

        packages = self.begin_the_turn(packages, worktime)
        self.take_action()
        self.end_turn(worktime)

        return packages

    def begin_the_turn(self, packages, worktime):
        if self.position == 0 and packages:
            if packages[0] == "A":
                self.route = "A"
            elif packages[0] == "B":
                self.route = "B"
            self.cargo = True
            self.truck_log_petis.transport_id += 1
            self.truck_log_petis.cargo_id += 1
            self.my_transport_id = self.truck_log_petis.transport_id
            self.my_cargo_id = self.truck_log_petis.cargo_id
            self.sleep = False
            packages = packages[1:]

            self.truck_log_petis.create_log(
                "DEPART", worktime, self.my_transport_id, self.name, "FACTORY", "B" if self.route == "B" else "PORT",
                self.my_cargo_id, self.route, "FACTORY")

        return packages

    def take_action(self):
        if self.cargo and self.position == 0:
            self.position += 1

        elif self.position > 0 and not self.cargo:
            self.position -= 1

        elif self.cargo and self.route == "B" and self.position < 5:
            self.position += 1

        else:
            self.sleep = True

    def end_turn(self, worktime):
        if self.sleep and self.route:
            if self.position == 0:
                self.route = None
                self.truck_log_petis.create_log(
                    "ARRIVE", worktime, self.my_transport_id, self.name, "FACTORY")
            if self.position == 1 and self.route == "A":
                self.cargo = False
                self.truck_log_petis.create_log(
                    "ARRIVE", worktime, self.my_transport_id, self.name, "PORT", None, self.my_cargo_id, "A", "PORT")


class Ship(Truck):
    def __init__(self, ship_log):
        super().__init__("ship_1", ship_log)
        self.port = ""

    def shipping(self, a_truck, b_truck, worktime):
        if a_truck.route == "A" and a_truck.position == 1:
            self.port += "A"
            self.my_cargo_id = a_truck.my_cargo_id
        if b_truck.route == "A" and b_truck.position == 1:
            self.port += "A"
            self.my_cargo_id = b_truck.my_cargo_id

        if not self.cargo and self.port and self.position == 0:
            self.cargo = True
            self.port = self.port[1:]
            self.truck_log_petis.transport_id += 1
            self.my_transport_id = self.truck_log_petis.transport_id
            self.truck_log_petis.create_log(
                "DEPART", worktime, self.my_transport_id, self.name, "PORT", "A", self.my_cargo_id, "A", "PORT")

        elif not self.cargo and self.position > 0:
            if self.position == 4:
                self.truck_log_petis.create_log(
                    "DEPART", worktime, self.my_transport_id, self.name, "A", "PORT")
            self.position -= 1
            if self.position == 0:
                self.truck_log_petis.create_log(
                    "ARRIVE", worktime, self.my_transport_id, self.name, "PORT")

        if self.position != 4 and self.cargo:
            self.position += 1

        if self.position == 4 and self.cargo:
            self.truck_log_petis.create_log(
                "ARRIVE", worktime, self.my_transport_id, self.name, "A", None, self.my_cargo_id, "A", "PORT")
            self.cargo = False


def delivery_timer(list_of_packages):
    truck_log_petis = Log(list_of_packages)
    worktime = 0
    truck_1 = Truck("truck_1", truck_log_petis)
    truck_2 = Truck("truck_2", truck_log_petis)
    ship_1 = Ship(truck_log_petis)

    while True:

        worktime += + 1

        ship_1.shipping(truck_1, truck_2, worktime)

        if len(list_of_packages) > 0 and not (list_of_packages[0] == "A" or list_of_packages[0] == "B"):
            return f"error at worktime {worktime} invalid package in {list_of_packages}"

        list_of_packages = truck_1.peti_move(list_of_packages, worktime)

        if len(list_of_packages) > 0 and not (list_of_packages[0] == "A" or list_of_packages[0] == "B"):
            return f"error at worktime {worktime} invalid package in {list_of_packages}"

        list_of_packages = truck_2.peti_move(list_of_packages, worktime)

        print()
        print(truck_1.name, "pos", truck_1.position, "cargo", truck_1.cargo, "route", truck_1.route, "worktime",
              worktime)
        print(truck_2.name, "pos", truck_2.position, "cargo", truck_2.cargo, "route", truck_2.route, "worktime",
              worktime)
        print(ship_1.name, "pos", ship_1.position, "cargo", ship_1.cargo)

        if not truck_1.cargo and not truck_2.cargo and not list_of_packages and not ship_1.port and not ship_1.cargo:
            return worktime

# delivery_timer("BABAABBBAAAAAAAA")
