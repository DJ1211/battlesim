import time

def battle(unit_1, unit_2):
        # Calculate weapon advantage
        unit_1.weapon.calculate_weapon_triangle(unit_2.weapon)

        # Calculate effective damage (e.g. bows vs flying)
        unit_1.weapon.calculate_effective_damage(unit_2.job)
        unit_2.weapon.calculate_effective_damage(unit_1.job)

        # Calculate speed for accuracy & double strike used in attack
        unit_1_attack_speed = unit_1.calculate_attack_speed()
        unit_2_attack_speed = unit_2.calculate_attack_speed()

        while unit_1.hp > 0 and unit_2.hp > 0:
            print(f"{unit_1.name} attacks {unit_2.name}")
            unit_1.attack(unit_2)
            print(f"{unit_2.name}'s HP: {unit_2.hp}\n")
            if unit_2.hp == 0:
                break
            time.sleep(3)

            print(f"{unit_2.name} attacks {unit_1.name}")
            unit_2.attack(unit_1)
            print(f"{unit_1.name}'s HP: {unit_1.hp}\n")
            if unit_1.hp == 0:
                break
            time.sleep(3)

            # Check for double attack

            if unit_1_attack_speed - unit_2_attack_speed >= 4:
                print(f"{unit_1.name}'s follow up!")
                print(f"{unit_1.name} attacks {unit_2.name}")
                unit_1.attack(unit_2)
                print(f"{unit_2.name}'s HP: {unit_2.hp}\n")
                time.sleep(3)

            elif unit_2_attack_speed - unit_1_attack_speed >= 4:
                print(f"{unit_2.name}'s follow up!")
                print(f"{unit_2.name} attacks {unit_1.name}")
                unit_2.attack(unit_1)
                print(f"{unit_1.name}'s HP: {unit_1.hp}\n")
                time.sleep(3)
        
        if unit_1.hp == 0:
            print(f"{unit_1.name} has been defeated!")
        
        elif unit_2.hp == 0:
            print(f"{unit_2.name} has been defeated!")