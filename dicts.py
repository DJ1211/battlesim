# Add check that path is valid

import os
import csv
path = "./stat_sheets/weapons.csv"

weapons = {}
units = {}
jobs = {}
terrain = {}

with open ("./stat_sheets/weapons.csv", newline='') as weaponscsv:
    reader = csv.DictReader(weaponscsv)
    for row in reader:
        k = row["name"]
        v = row
        if v["effective_against"] != "None":
            v["effective_against"] = v["effective_against"].split(", ")
        weapons[k] = v

with open ("./stat_sheets/units.csv", newline='') as unitscsv:
    reader = csv.DictReader(unitscsv)
    for row in reader:
        k = row["name"]
        v = row
        units[k] = v

with open ("./stat_sheets/jobs.csv", newline='') as jobscsv:
    reader = csv.DictReader(jobscsv)
    for row in reader:
        k = row["name"]
        v = row
        if v["weapon_types"] != "None":
            v["weapon_types"] = v["weapon_types"].split(", ")
        if v["available_jobs"] != "None":
            v["available_jobs"] = v["available_jobs"].split(", ")
        jobs[k] = v

with open ("./stat_sheets/terrain.csv", newline='') as terraincsv:
    reader = csv.DictReader(terraincsv)
    for row in reader:
        k = row["name"]
        v = row
        terrain[k] = v
