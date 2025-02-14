from units import Unit
from weapons import Weapon
from jobs import Job
from dicts import units, weapons, jobs
import time

def main():
    unit_1 = Unit(units["eirika"], Weapon(weapons["rapier"]), Job(jobs["lord(f)"]))
    unit_2 = Unit(units["seth"], Weapon(weapons["silver_lance"]), Job(jobs["paladin(m)"]))
    target_level_1 = 20
    target_level_2 = 20
 
    unit_1.set_level(target_level_1)
    unit_1.promote(0)
    unit_1.set_level(target_level_1)
    unit_2.set_level(target_level_2)
    unit_1.battle(unit_2)

main()