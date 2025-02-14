from dicts import units, weapons, jobs
from jobs import Job
import random
import time

class Unit:
    def __init__(self, unit, weapon, job):
        self.name = unit["name"]
        self.level = unit["level"]
        self.promoted = unit["promoted"]
        self.available_jobs = unit["available_jobs"]
        self.hp = unit["hp"]
        self.str = unit["str"]
        self.skl = unit["skl"]
        self.spd = unit["spd"]
        self.lck = unit["lck"]
        self.defence = unit["def"]
        self.res = unit["res"]
        self.con = unit["con"]
        self.hp_grow = unit["hp_grow"]
        self.str_grow = unit["str_grow"]
        self.skl_grow = unit["str_grow"]
        self.spd_grow = unit["spd_grow"]
        self.lck_grow = unit["lck_grow"]
        self.def_grow = unit["def_grow"]
        self.res_grow = unit["res_grow"]
        self.weapon = weapon
        self.job = job
        self.job.apply_stats(self)
    
    def attack(self, target):
        #  Terrain & weapon triangle to add
        if self.calculate_hit(target):
            damage = (self.str + self.weapon.mt)

            if self.job.use_magic == False:
                damage -= target.defence # - Terrain
            else:
                damage -= target.res # - Terrain

            if self.calculate_critical():
                print("Critical Hit!")
                damage *= 3

            if damage < 0:
                damage = 0
            print(f"Damage: {damage}")

            target.hp = target.hp - damage

            if target.hp < 0:
                target.hp = 0
            return target.hp
        
        print("Miss!")
    
    def calculate_hit(self, target):
        # No support bonus to be considered. Weapon triangle currently 0 until implemented
        base_hit_rate = self.weapon.hit + (self.skl * 2) + (self.lck // 2)
        target_attack_speed = target.calculate_attack_speed()
        
        # Terrain to be added later
        avoid_rate = (target_attack_speed * 2) + target.lck # + Terrain

        hit_rate = base_hit_rate - avoid_rate
        hit_value = self.rng()

        if hit_value >= hit_rate:
            return False
        else:
            return True
    
    def calculate_attack_speed(self):
        speed_penalty = self.weapon.wt - self.con
        if speed_penalty < 0:
            speed_penalty = 0

        attack_speed = self.spd - speed_penalty
        if attack_speed < 0:
            attack_speed = 0
        
        return attack_speed
    
    def calculate_critical(self):
        # No supports. Crit bonus to be added later?
        crit_chance = self.rng()
        crit_rate = self.weapon.crt + (self.skl // 2)
        if crit_chance >= crit_rate:
            return False
        else:
            return True

    def battle(self, target):
        # Calculate weapon advantage
        self.weapon.calculate_weapon_triangle(target.weapon)
        target.weapon.calculate_weapon_triangle(self.weapon)

        # Calculate speed for accuracy & double strike used in attack
        attack_speed = self.calculate_attack_speed()
        target_attack_speed = target.calculate_attack_speed()

        while self.hp > 0 and target.hp > 0:
            print(f"{self.name} attacks {target.name}")
            self.attack(target)
            print(f"{target.name}'s HP: {target.hp}\n")
            if target.hp == 0:
                break
            time.sleep(3)

            print(f"{target.name} attacks {self.name}")
            target.attack(self)
            print(f"{self.name}'s HP: {self.hp}\n")
            if self.hp == 0:
                break
            time.sleep(3)

            # Check for double attack

            if attack_speed - target_attack_speed >= 4:
                print(f"{self.name}'s follow up!")
                print(f"{self.name} attacks {target.name}")
                self.attack(target)
                print(f"{target.name}'s HP: {target.hp}\n")
                time.sleep(3)

            elif target_attack_speed - attack_speed >= 4:
                print(f"{target.name}'s follow up!")
                print(f"{target.name} attacks {self.name}")
                target.attack(self)
                print(f"{self.name}'s HP: {self.hp}\n")
                time.sleep(3)
        
        if self.hp == 0:
            print(f"{self.name} has been defeated!")
        
        elif target.hp == 0:
            print(f"{target.name} has been defeated!")

    def set_level(self, value = None):
        starting_level = self.level
        if value == None:
            return
        if 1 <= value <= 20:
            print(f"Setting {self.name} to level {value}\n")
            self.level = value
        else:
            print("Invalid Level")
        
        self.calculate_level_up(starting_level)
            
    def calculate_level_up(self, starting_level):
        hp_counter = 0
        str_counter = 0
        skl_counter = 0
        spd_counter = 0
        lck_counter = 0
        def_counter = 0
        res_counter = 0
        for i in range(starting_level, self.level):
            hp_chance = self.rng()
            str_chance = self.rng()
            skl_chance = self.rng()
            spd_chance = self.rng()
            lck_chance = self.rng()
            def_chance = self.rng()
            res_chance = self.rng()
            
            if hp_chance < self.hp_grow:
                hp_counter += 1
                self.hp += 1
            
            if str_chance < self.str_grow:
                str_counter += 1
                self.str += 1
            
            if skl_chance < self.skl_grow:
                skl_counter += 1
                self.skl += 1

            if spd_chance < self.spd_grow:
                spd_counter += 1
                self.spd += 1
            
            if lck_chance < self.lck_grow:
                lck_counter += 1
                self.lck += 1
            
            if def_chance < self.def_grow:
                def_counter += 1
                self.defence += 1
            
            if res_chance < self.res_grow:
                res_counter += 1
                self.res += 1
        
        print(f"HP +{hp_counter}")
        print(f"Str +{str_counter}")
        print(f"Skl +{skl_counter}")
        print(f"Spd +{spd_counter}")
        print(f"Lck +{lck_counter}")
        print(f"Def +{def_counter}")
        print(f"Res +{res_counter}")
        print("\n")
        time.sleep(5)    

    def promote(self, index):
        if self.level >= 10:
            new_job = self.available_jobs[index]
            self.job = Job(jobs[new_job])
            self.job.apply_stats(self)
            self.available_jobs = None
            self.level = 1
        else:
            print("Cannot Promote")

         
    def rng(self):
        rand1 = random.randint(0, 99)
        rand2 = random.randint(0, 99)
        return (rand1 + rand2) // 2

