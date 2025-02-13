from units import Unit
from dicts import units, weapons
import time

def main():
    unit_1 = Unit(units["eirika"], weapons["swords"]["rapier"])
    unit_2 = Unit(units["seth"], weapons["lances"]["silver_lance"])
    target_level_1 = 20
    target_level_2 = 10

    print(f"Setting {unit_1.name} to level {target_level_1}\n")
    unit_1.set_level(target_level_1)
    print("\n")
    time.sleep(5)
    print(f"Setting {unit_2.name} to level {target_level_2}\n")
    unit_2.set_level(target_level_2)
    print("\n")
    time.sleep(5)
    unit_1.battle(unit_2)


main()