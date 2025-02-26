from dicts import units, weapons, jobs
from weapons import Weapon
from jobs import Job
from terrain import Terrain
import random
import time
import tkinter as tk

class Unit:
    def __init__(self, unit):
        self.name = unit["name"]
        self.level = int(unit["level"])
        self.job = unit["default_job"]
        self.hp = int(unit["hp"])
        self.str = int(unit["str"])
        self.skl = int(unit["skl"])
        self.spd = int(unit["spd"])
        self.lck = int(unit["lck"])
        self.defence = int(unit["def"])
        self.res = int(unit["res"])
        self.con = int(unit["con"])
        self.hp_grow = int(unit["hp_grow"])
        self.str_grow = int(unit["str_grow"])
        self.skl_grow = int(unit["str_grow"])
        self.spd_grow = int(unit["spd_grow"])
        self.lck_grow = int(unit["lck_grow"])
        self.def_grow = int(unit["def_grow"])
        self.res_grow = int(unit["res_grow"])
        self.weapon = None
        self.terrain = None
        self.base_level = self.level
        self.base_hp = self.hp
        self.base_str = self.str
        self.base_skl = self.skl
        self.base_spd = self.spd
        self.base_lck = self.lck
        self.base_defence = self.defence
        self.base_res = self.res
        self.base_con = self.con
        self.damage = None
        self.hit_rate = None
        self.crit_rate = None
        self.assign_job(jobs[self.job])
    
    def assign_job(self, job):
        self.level = self.base_level
        self.hp = self.base_hp
        self.str = self.base_str
        self.skl = self.base_skl
        self.spd = self.base_spd
        self.lck = self.base_lck
        self.defence = self.base_defence
        self.res = self.base_res
        self.con = self.base_con
        self.job = Job(job)
        self.job.apply_stats(self)

    def assign_weapon(self, weapon, battle_window):
        unit_weapon = Weapon(weapon)
        if unit_weapon.type in self.job.weapon_types:
            self.weapon = Weapon(weapon)
        else:
            battle_window.insert(tk.END, "Invalid Weapon\n\n")
            battle_window.see(tk.END)  

    def assign_terrain(self, terrain):
        self.terrain = Terrain(terrain)
        if self.job.type_1 == "Flying" or self.job.type_2 == "Flying":
            self.terrain.avoid = 0
            self.terrain.def_bonus = 0
    
    def calculate_hit(self, target):
        
        base_hit_rate = self.weapon.hit + (self.skl * 2) + (self.lck // 2)
        target_attack_speed = target.calculate_attack_speed()
        
        avoid_rate = (target_attack_speed * 2) + target.lck + target.terrain.avoid

        hit_rate = base_hit_rate - avoid_rate
        hit_value = self.rng()

        self.hit_rate = hit_rate
        if self.hit_rate > 100:
            self.hit_rate = 100
        if self.hit_rate < 0:
            self.hit_rate = 0

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
        # No supports. Crit bonus to be added later
        crit_chance = self.rng()
        crit_rate = self.weapon.crt + (self.skl // 2)

        self.crit_rate = crit_rate
        if self.crit_rate > 100:
            self.crit_rate = 100
        if self.crit_rate < 0:
            self.crit_rate = 0

        if crit_chance >= crit_rate:
            return False
        else:
            return True
        
    def calculate_damage(self, target):
        self.damage = (self.str + self.weapon.mt)

        if self.weapon.magic == False:
            self.damage -= target.defence + target.terrain.def_bonus
        else:
            self.damage -= target.res + target.terrain.def_bonus

        if self.damage < 0:
            self.damage = 0

    def attack(self, target, battle_window):
        if self.calculate_hit(target):     

            if self.calculate_critical():
                battle_window.insert(tk.END, "Critical Hit!\n")
                battle_window.see(tk.END)
                self.damage *= 3

            battle_window.insert(tk.END, f"Damage: {self.damage}\n")
            battle_window.see(tk.END)

            target.hp = target.hp - self.damage

            if target.hp < 0:
                target.hp = 0
            return target.hp
        
        battle_window.insert(tk.END, "Miss!\n")
        battle_window.see(tk.END)

    def set_level(self, battle_window, value = None):
        # Records the starting level to be used in applying stats and then raises the level to the intended level

        starting_level = self.level
        if value == None:
            return
        if value <= self.level:
            battle_window.insert(tk.END, "Cannot lower level\n\n")
            battle_window.see(tk.END)  
            return
        if 1 <= value <= self.job.max_level:
            battle_window.insert(tk.END, f"Setting {self.name} to level {value}\n\n")
            battle_window.see(tk.END)  
            self.level = value
        else:
            battle_window.insert(tk.END, "Invalid Level\n\n")
            battle_window.see(tk.END)  
        
        self.calculate_level_up(starting_level, battle_window)
            
    def calculate_level_up(self, starting_level, battle_window):
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
                self.hp += 1
                if self.hp > self.job.hp_cap:
                    self.hp = self.job.hp_cap
                else:
                    hp_counter += 1
            
            if str_chance < self.str_grow:
                self.str += 1
                if self.str > self.job.str_cap:
                    self.str = self.job.str_cap
                else:
                    str_counter += 1
            
            if skl_chance < self.skl_grow:
                self.skl += 1
                if self.skl > self.job.skl_cap:
                    self.skl = self.job.skl_cap
                else:
                    skl_counter += 1

            if spd_chance < self.spd_grow:
                self.spd += 1
                if self.spd > self.job.spd_cap:
                    self.spd = self.job.spd_cap
                else:
                    spd_counter += 1
            
            if lck_chance < self.lck_grow:
                self.lck += 1
                if self.lck > self.job.lck_cap:
                    self.lck = self.job.lck_cap
                else:
                    lck_counter += 1
            
            if def_chance < self.def_grow:
                self.defence += 1
                if self.defence > self.job.def_cap:
                    self.defence = self.job.def_cap
                else:
                    def_counter += 1
            
            if res_chance < self.res_grow:
                self.res += 1
                if self.res > self.job.res_cap:
                    self.res = self.job.res_cap
                else:
                    res_counter += 1
        
        battle_window.insert(tk.END, f"HP +{hp_counter}\n") 
        battle_window.insert(tk.END, f"Str +{str_counter}\n") 
        battle_window.insert(tk.END, f"Skl +{skl_counter}\n") 
        battle_window.insert(tk.END, f"Spd +{spd_counter}\n") 
        battle_window.insert(tk.END, f"Lck +{lck_counter}\n") 
        battle_window.insert(tk.END, f"Def +{def_counter}\n") 
        battle_window.insert(tk.END, f"Res +{res_counter}\n\n") 
        battle_window.see(tk.END)  

    def promote(self, target_job, battle_window):
        if self.level >= 10:
            battle_window.insert(tk.END, f"Promoting {self.name} from {self.job.name} to {target_job}\n\n") 
            battle_window.see(tk.END)  
            self.job = Job(jobs[target_job])
            battle_window.insert(tk.END, f"HP +{self.job.hp_promote}\n") 
            battle_window.insert(tk.END, f"Str +{self.job.str_promote}\n") 
            battle_window.insert(tk.END, f"Skl +{self.job.skl_promote}\n") 
            battle_window.insert(tk.END, f"Spd +{self.job.spd_promote}\n") 
            battle_window.insert(tk.END, f"Def +{self.job.def_promote}\n") 
            battle_window.insert(tk.END, f"Res +{self.job.res_promote}\n") 
            battle_window.insert(tk.END, f"Res +{self.job.con_promote}\n\n") 
            battle_window.see(tk.END)  
            self.job.apply_promotion(self)
            self.level = 1
        else:
            battle_window.insert(tk.END, "Cannot Promote\n\n") 
            battle_window.see(tk.END)  
         
    def rng(self):
        rand1 = random.randint(0, 99)
        rand2 = random.randint(0, 99)
        return (rand1 + rand2) // 2