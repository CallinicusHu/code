# neighbours[city][neighbor]:km
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


def map_distance(start, goal):

    if goal in neighbours[start]:
        return neighbours[start][goal]
    else:
        return wayfinder(start, goal, list(set(cities) - {start, goal}))

def wayfinder(start, goal, stops):



    for stop in stops:
        if stop in neighbours[start] and stop not in neighbours[goal]:






print(map_distance("Steamdrift", "Cogburg"))
print("\n")
print(map_distance("Steamdrift", "Leverstorm"))
# print(map_distance("Steamdrift", "Irondale"))
