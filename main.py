from units import Unit
from weapons import Weapon
from jobs import Job
from dicts import units, weapons, jobs, terrain
from battle import battle
import time

def main():

    unit_1_id = units["Eirika"]
    unit_1_weapon = weapons["Rapier"]
    unit_1_job = jobs["Lord (F)"]
    unit_1_terrain = terrain["plain"]
    unit_2_id = units["Lute"]
    unit_2_weapon = weapons["Thunder"]
    unit_2_job = jobs["Mage (F)"]
    unit_2_terrain = terrain["forest"]

    unit_1 = Unit(unit_1_id)
    unit_2 = Unit(unit_2_id)
    unit_1.assign_job(unit_1_job)
    unit_1.assign_weapon(unit_1_weapon)
    unit_1.assign_terrain(unit_1_terrain)
    unit_2.assign_job(unit_2_job)
    unit_2.assign_weapon(unit_2_weapon)
    unit_2.assign_terrain(unit_2_terrain)
    target_level_1 = 20
    target_level_2 = 20

    print(type(unit_1.weapon.mt))
 
#    unit_1.set_level(target_level_1)
#    unit_1.promote(0)
#    unit_1.set_level(target_level_1)
#    unit_2.set_level(target_level_2)
#    unit_2.promote(0)
#    unit_2.set_level(target_level_2)
#    battle(unit_1, unit_2)

main()