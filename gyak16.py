# neighbours[city][neighbor]:km
import csv
import json

cities = ["Cogburg", "Copperhold", "Irondale", "Gizbourne", "Leverstorm", "Rustport", "Steamdrift"]
neighbours = {
    "Cogburg": {
        "Copperhold": 1047,
        "Irondale": 1034,
        "Steamdrift": 1269,
        "Rustport": 1421
    },
    "Copperhold": {
        "Irondale": 345,
        "Leverstorm": 569,
        "Cogburg": 1047
    },
    "Irondale": {
        "Gizbourne": 526,
        "Cogburg": 1034,
        "Copperhold": 345,
        "Leverstorm": 673,
        "Rustport": 1302
    },
    "Gizbourne": {
        "Irondale": 526,
        "Leverstorm": 866,
        "Rustport": 1220
    },
    "Leverstorm": {
        "Gizbourne": 866,
        "Irondale": 673,
        "Copperhold": 569
    },
    "Rustport": {
        "Cogburg": 1421,
        "Gizbourne": 1220,
        "Irondale": 1302,
        "Steamdrift": 1947
    },
    "Steamdrift": {
        "Cogburg": 1269,
        "Rustport": 1947
    }
}

train_data = []

with open ("train_data_gyak.csv", "r", encoding="UTF-8") as source:
    for row in source:
        train_data.append(row.strip("\n"))

for index, line in enumerate(train_data):
    train_data[index] = line.split(',')

train_data_temp = train_data.copy()
travel_averages = neighbours.copy()

travel_json = json.dumps(travel_averages, indent=4)

print(travel_json)

for neighbourhood in neighbours:
    for neighbour in neighbours[neighbourhood]:
        measure = [] #measure the average travel time between cites
        for index, line in enumerate(train_data_temp):
            if neighbourhood == line[2] and neighbour == line[3]:
                measure.append(float(line[4]))
        travel_averages[neighbourhood].update({neighbour: (sum(measure)/len(measure))})

test_dataset = []

with open ("train_data_test.csv", "r", encoding="UTF-8") as source:
    for row in source:
        test_dataset.append(row.strip("\n"))

for index, line in enumerate(test_dataset):
    test_dataset[index] = line.split(',')

test_dataset.pop(0)

def predict(stop1, stop2):
    return travel_averages[stop1][stop2]

error_sum = 0
for line in test_dataset:
    predicted_speed = predict(line[2], line[3])
    difference = float(line[4]) - predicted_speed
    square = difference * difference
    error_sum += square
mse = error_sum / len(test_dataset)
print(f"Mean squared error is {mse}")

def create_log(logthis):
    with open("stopstops_log", "a", encoding="UTF-8") as stop_log:
        stop_log.write(logthis)
        stop_log.write("\n")


def map_distance(start, goal):
    with open("stopstops_log", "w", encoding="UTF-8") as stop_log:
        stop_log.write("\n")

    if goal in neighbours[start]:
        return f"from {start} to {goal} the shortest distance is {neighbours[start][goal]} km"
    else:
        return (f"from {start} to {goal} the shortest distance is "
                f"{wayfinder(start, goal)} km")


def find_routes(neighb, start, goal):
    all_routes = []

    def dfs(current, path):
        path.append(current)

        if current == goal:
            all_routes.append((path.copy()))

        for nxt in neighb[current]:
            if nxt not in path:
                dfs(nxt, path)

        path.pop()

    dfs(start, [])
    return all_routes


def wayfinder(start, goal):
    distances = []

    for route in find_routes(neighbours, start, goal):
        this_route = 0
        for count, station in enumerate(route):
            create_log(
                f"We go from {station} to {route[count+1]} they are {neighbours[station][route[count+1]]} km-s from each-other")
            this_route += neighbours[station][route[count+1]]
            if count+2 == len(route):
                break
        distances.append(this_route)
        create_log(
            f"\nThe distance of the {route} route is {this_route} km-s.\n")

    return min(distances)
