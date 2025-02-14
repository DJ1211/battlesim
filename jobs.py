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
        self.use_magic = job["use_magic"]
        self.use_swords_light = job["use_swords_light"]
        self.use_axes_dark = job["use_axes_dark"]
        self.use_laces_anima = job["use_lances_anima"]
        self.use_bows_staves = job["use_bows_staves"]
    
    def apply_stats(self, unit):
        # Applies class base stats to unit
        unit.hp += self.hp
        unit.str += self.str
        unit.skl += self.skl
        unit.spd += self.spd
        unit.defence += self.defence
        unit.res += self.res
        unit.con += self.con
