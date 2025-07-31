import json
import csv

with open('hhjatekok2025.json', 'r', encoding='utf-8') as file:
    raw_data = json.load(file)

COLUMNS = ["Mesélő", "Nap", "Játék",
           "Játékos 1", "Játékos 2", "Játékos 3", "Játékos 4", "Játékos 5",
           "Játékos 6", "Játékos 7", "Játékos 8", "Játékos 9", "Játékos 10",
           "Játékos 11", "Játékos 12", "Játékos 13", "Játékos 14", "Játékos 15",
           "Játékos 16", "Játékos 17", "Játékos 18", "Játékos 19", "Játékos 20"
           ]

DAYS = ["Szombat", "Vasárnap", "Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek"]


def daytranslate(day):
    translated = ""
    if day["name"].startswith("Sat"):
        translated = "Szombat"
    if day["name"].startswith("Sun"):
        translated = "Vasárnap"
    if day["name"].startswith("Mon"):
        translated = "Hétfő"
    if day["name"].startswith("Tue"):
        translated = "Kedd"
    if day["name"].startswith("Wed"):
        translated = "Szerda"
    if day["name"].startswith("Thu"):
        translated = "Csütörtök"
    if day["name"].startswith("Fri"):
        translated = "Péntek"
    if len(day["name"]) > 30:
        translated += " este"
    return translated


# név és e-mail cím
with open('hhtabor2025email.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(COLUMNS)
    for day in raw_data['slots']:
        for session in day['sessions']:
            temp = []
            gms = ""
            for gm in session["gms"]:  # mesélő
                gms += gm["name"] + " <" + gm["email"] + ">" + ", "
            if gms:
                temp.append(gms.strip(", "))
            else:  # feltételezem hogy üres gm list esetén 0x futott le a loop, tehát a hiányzó mesélő estén üres lenne és akkor if gms: false
                temp.append("HIÁNYZIK")
            temp.append(daytranslate(day))  # nap
            temp.append(session["name"])  # játék neve
            for player in session["players"]:  # játékosok
                temp.append(f"{player["name"]} <{player["email"]}>")
            writer.writerow(temp)

# név és egyéb
with (open('hhtabor2025info.csv', 'w', newline='') as file):
    writer = csv.writer(file)
    extended_columns = [COLUMNS[1], COLUMNS[0], COLUMNS[2]] + ["Max", "Foglalt", "Szabad"] + COLUMNS[3:]
    writer.writerow(extended_columns)
    counter = []
    for day in raw_data['slots']:
        for session in day['sessions']:
            temp = []
            temp.append(daytranslate(day))  # nap
            gms = ""
            for gm in session["gms"]:  # mesélő
                gms += gm["name"] + ", "
            if gms:
                temp.append(gms.strip(", "))
            else:  # feltételezem hogy üres gm list esetén 0x futott le a loop, tehát a hiányzó mesélő estén üres lenne és akkor if gms: false
                temp.append("HIÁNYZIK")
            temp.append(session["name"])  # játék neve
            temp.append(session["table_count"] * session["table_size"])  # max hely
            temp.append(len(session["players"]))  # foglalt hely
            temp.append(session["table_count"] * session["table_size"] - len(session["players"]))  # szabad hely
            for player in session["players"]:  # játékosok
                temp.append(f"{player["name"]}")
            writer.writerow(temp)
            counter += [temp]

    # Összegző sorok számítása
    day_sums = {day: {"Összes hely": 0, "Foglalt hely": 0, "Szabad hely": 0} for day in DAYS}
    for row in counter:
        day = row[0]  # A nap neve az első oszlopban
        max_hely = row[3]
        foglalt_hely = row[4]
        szabad_hely = row[5]
        if day in day_sums:
            day_sums[day]["Összes hely"] += max_hely
            day_sums[day]["Foglalt hely"] += foglalt_hely
            day_sums[day]["Szabad hely"] += szabad_hely

    # Összegző sorok írása
    writer.writerow(["Alább az éjszakai játékokkal nem számolok."])
    writer.writerow(["Játéknap"] + DAYS)
    writer.writerow(["Szabad hely"] + [day_sums[day]["Szabad hely"] for day in DAYS] + ["ennyi játékost tudnak még játékok fogadni aznap."])
    writer.writerow(["Foglalt hely"] + [day_sums[day]["Foglalt hely"] for day in DAYS] + ["ennyi játékhely foglalt aznap."])
    writer.writerow(["Összes hely"] + [day_sums[day]["Összes hely"] for day in DAYS] + ["maximális mennyiségű leülthetető játékos."])

    # További statisztikák
    all_the_possible_people = ["Leültethető emberek"]
    for day in raw_data["slots"]:
        if len(day["name"]) < 30:
            todays_people = 0
            for session in day["sessions"]:
                todays_people += session["table_count"] * session["table_size"] + session["table_count"]
            all_the_possible_people.append(f"{todays_people}")
    all_the_possible_people.append("mesélők + játékosok maximális száma aznap.")
    writer.writerow(all_the_possible_people)

    people_who_sit = ["Leültetett emberek"]
    for day in raw_data["slots"]:
        if len(day["name"]) < 30:
            todays_people = 0
            for session in day["sessions"]:
                todays_people += len(session["players"]) + session["table_count"]
            people_who_sit.append(f"{todays_people}")
    people_who_sit.append("mesélők + játékosok aktuális száma aznap.")
    writer.writerow(people_who_sit)
"""
#megtelt játékok levéllel
with (open('hhtabor2025megtelt.csv', 'w', newline='') as file):
    writer = csv.writer(file)
    extended_columns = ["Címek", "Fejléc", "Levél"]
    writer.writerow(extended_columns)
    for row in counter:
        for session in raw_data["slots"]["sessions"]:
            if session["name"] == row[2]:
                temp = session["gms"]["name"]
"""