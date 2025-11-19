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


def wayfinder(start, goal):
    way_length = 0
    way_stop = start
    stops = cities.copy()
    stops.remove(start)

    while goal not in neighbours[way_stop]:
        for city in cities:
            if city in neighbours[way_stop] and city in stops:

                create_log(
                    f"Go from {way_stop} to {city} it ads {neighbours[way_stop][city]} km")

                next_stop = city
                way_length += neighbours[way_stop][next_stop]
                way_stop = next_stop

                create_log(
                    f"The distance for this way is {way_length} km")

                stops.remove(city)
                create_log(f"{stops}")

                break
            if way_length > 10000:
                return way_length

    way_length += neighbours[way_stop][goal]

    create_log(
        f"Last we went from {way_stop} to {goal} +{neighbours[way_stop][goal]} km The total distance for this way is {way_length} km")

    return way_length
