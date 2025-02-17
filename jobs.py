from dicts import jobs

class Job:
    def __init__(self, job):
        self.name = job["name"]
        self.hp = job["hp"]
        self.str = job["str"]
        self.skl = job["skl"]
        self.spd = job["spd"]
        self.defence = job["def"]
        self.res = job["res"]
        self.con = job["con"]
        self.hp_cap = job["hp_cap"]
        self.str_cap = job["str_cap"]
        self.skl_cap = job["skl_cap"]
        self.spd_cap = job["spd_cap"]
        self.lck_cap = job["lck_cap"]
        self.def_cap = job["def_cap"]
        self.res_cap = job["res_cap"]
        self.weapon_types = job["weapon_types"]
        self.type_1 = job["type_1"]
        self.type_2 = job["type_2"]
    
    def apply_stats(self, unit):
        # Applies class base stats to unit
        unit.hp += self.hp
        unit.str += self.str
        unit.skl += self.skl
        unit.spd += self.spd
        unit.defence += self.defence
        unit.res += self.res
        unit.con += self.con
