from dicts import jobs

class Job:
    def __init__(self, job):
        self.name = job["name"]
        self.hp = int(job["hp"])
        self.str = int(job["str"])
        self.skl = int(job["skl"])
        self.spd = int(job["spd"])
        self.defence = int(job["def"])
        self.res = int(job["res"])
        self.con = int(job["con"])
        self.hp_cap = int(job["hp_cap"])
        self.str_cap = int(job["str_cap"])
        self.skl_cap = int(job["skl_cap"])
        self.spd_cap = int(job["spd_cap"])
        self.lck_cap = int(job["lck_cap"])
        self.def_cap = int(job["def_cap"])
        self.res_cap = int(job["res_cap"])
        self.hp_promote = int(job["hp_promote"])
        self.str_promote = int(job["str_promote"])
        self.skl_promote = int(job["skl_promote"])
        self.spd_promote = int(job["spd_promote"])
        self.def_promote = int(job["def_promote"])
        self.res_promote = int(job["res_promote"])
        self.con_promote = int(job["con_promote"])
        self.max_level = int(job["max_level"])
        self.weapon_types = job["weapon_types"]
        self.class_skill = job["class_skill"]
        self.type_1 = job["type_1"]
        self.type_2 = job["type_2"]
        self.available_jobs = job["available_jobs"]
    
    def apply_stats(self, unit):
        # Applies class base stats to unit
        unit.hp += self.hp
        unit.str += self.str
        unit.skl += self.skl
        unit.spd += self.spd
        unit.defence += self.defence
        unit.res += self.res
        unit.con += self.con

    def apply_promotion(self, unit):
        # Applies class promotion stats to unit
        unit.hp += self.hp_promote
        unit.str += self.str_promote
        unit.skl += self.skl_promote
        unit.spd += self.spd_promote
        unit.defence += self.def_promote
        unit.res += self.res_promote
        unit.con += self.con_promote

