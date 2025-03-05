# Add check that path is valid

import os
import csv

current_dir = os.path.dirname(os.path.abspath(__file__))
weapon_path = os.path.join(current_dir, "stat_sheets", "weapons.csv")
unit_path = os.path.join(current_dir, "stat_sheets", "units.csv")
jobs_path = os.path.join(current_dir, "stat_sheets", "jobs.csv")
terrain_path = os.path.join(current_dir, "stat_sheets", "terrain.csv")

weapons = {}
units = {}
jobs = {}
terrain = {}

if os.path.exists(weapon_path):
    with open (weapon_path, newline='') as weaponscsv:
        reader = csv.DictReader(weaponscsv)
        for row in reader:
            k = row["name"]
            v = row
            if v["effective_against"] != "None":
                v["effective_against"] = v["effective_against"].split(", ")
            weapons[k] = v
else:
    raise Exception(f"File not found: {weapon_path}")

if os.path.exists(unit_path):
    with open (unit_path, newline='') as unitscsv:
        reader = csv.DictReader(unitscsv)
        for row in reader:
            k = row["name"]
            v = row
            units[k] = v
else:
    raise Exception("Missing units.csv")


if os.path.exists(jobs_path):
    with open (jobs_path, newline='') as jobscsv:
        reader = csv.DictReader(jobscsv)
        for row in reader:
            k = row["name"]
            v = row
            if v["weapon_types"] != "None":
                v["weapon_types"] = v["weapon_types"].split(", ")
            if v["available_jobs"] != "None":
                v["available_jobs"] = v["available_jobs"].split(", ")
            jobs[k] = v
else:
    raise Exception("Missing jobs.csv")

if os.path.exists(terrain_path):
    with open (terrain_path, newline='') as terraincsv:
        reader = csv.DictReader(terraincsv)
        for row in reader:
            k = row["name"]
            v = row
            terrain[k] = v
else:
    raise Exception("Missing terrain.csv")
