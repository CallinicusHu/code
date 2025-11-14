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
        return f"from {start} to {goal} the shortest distance is {neighbours[start][goal]} km"
    else:
        return (f"from {start} to {goal} the shortest distance is "
                f"{wayfinder(start, goal, list(set(cities) - {start, goal}))} km")


def wayfinder(start, goal, stops):
    ways = [key for key in neighbours[start].keys()]
    way_lengths = [0 for _ in range(len(ways))]

    for way in range(len(ways)):
        index = 0
        while True:
            if way_lengths[way] == 0:
                way_lengths[way] = way_lengths[way] + neighbours[start][ways[way]]
                print(f"from {start} to {stops[index]}, +{neighbours[start][ways[way]]} km {way_lengths}")
                way_stop = ways[way]

            if stops[index] in neighbours[way_stop] and stops[index] not in neighbours[goal]:
                way_lengths[way] = way_lengths[way] + neighbours[way_stop][stops[index]]
                print(f"from {way_stop} to {stops[index]}, +{neighbours[way_stop][stops[index]]} km {way_lengths}")
                way_stop = stops[index]
                index += 1

            elif stops[index] in neighbours[way_stop] and stops[index] in neighbours[goal]:
                way_lengths[way] += neighbours[way_stop][stops[index]]
                print(f"from {way_stop} to {stops[index]}, +{neighbours[way_stop][stops[index]]} km {way_lengths}")
                break

            else:
                index += 1

    return min(way_lengths)


print("\n")
print(map_distance("Steamdrift", "Cogburg"))
print("\n")
print(map_distance("Irondale", "Steamdrift"))
print("\n")
# print(map_distance("Steamdrift", "Irondale"))
