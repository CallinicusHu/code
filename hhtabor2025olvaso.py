import json
import csv

with open('hhjatekok2025.json', 'r', encoding='utf-8') as file:
    raw_data = json.load(file)

columns = ["Mesélő", "Nap", "Játék",
           "Játékos 1", "Játékos 2", "Játékos 3", "Játékos 4", "Játékos 5",
           "Játékos 6", "Játékos 7", "Játékos 8", "Játékos 9", "Játékos 10",
           "Játékos 11", "Játékos 12", "Játékos 13", "Játékos 14", "Játékos 15",
           "Játékos 16", "Játékos 17", "Játékos 18", "Játékos 19", "Játékos 20"
           ]


def daytranslate():
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
    writer.writerow(columns)
    for day in raw_data['slots']:
        for session in day['sessions']:
            temp = []
            gms = ""
            for gm in session["gms"]: # mesélő
                gms += gm["name"] + " <" + gm["email"] + ">" + ", "
            if gms:
                temp.append(gms.strip(", "))
            else: #feltételezem hogy üres gm list esetén 0x futott le a loop, tehát a hiányzó mesélő estén üres lenne és akkor if gms: false
                temp.append("HIÁNYZIK")
            temp.append(daytranslate())  # nap
            temp.append(session["name"])  # játék neve
            for player in session["players"]:  # játékosok
                temp.append(f"{player["name"]} <{player["email"]}>")
            writer.writerow(temp)

# név és egyéb
with (open('hhtabor2025info.csv', 'w', newline='') as file):
    writer = csv.writer(file)
    extended_columns = [columns[1], columns[0], columns[2]] + ["Max", "Foglalt", "Szabad"] + columns[3:]
    writer.writerow(extended_columns)
    for day in raw_data['slots']:
        for session in day['sessions']:
            temp = []
            temp.append(daytranslate())  # nap
            gms = ""
            for gm in session["gms"]: # mesélő
                gms += gm["name"] + ", "
            if gms:
                temp.append(gms.strip(", "))
            else: #feltételezem hogy üres gm list esetén 0x futott le a loop, tehát a hiányzó mesélő estén üres lenne és akkor if gms: false
                temp.append("HIÁNYZIK")
            temp.append(session["name"])  # játék neve
            temp.append(session["table_count"] * session["table_size"])  # max hely
            temp.append(len(session["players"]))  # foglalt hely
            temp.append(session["table_count"] * session["table_size"] - len(session["players"]))  # szabad hely
            for player in session["players"]:  # játékosok
                temp.append(f"{player["name"]}")
            writer.writerow(temp)

