from dicts import weapons

class Weapon:
    def __init__(self, weapon):
        self.name = weapon["name"]
        self.mt = weapon["mt"]
        self.hit = weapon["hit"]
        self.crt = weapon["crt"]
        self.wt = weapon["wt"]
        self.type = weapon["type"]

    def calculate_weapon_triangle(self, target):
        # +15 accuracy for advantage, -15 for disadvantage
        if self.type == "sword":
            if target.type == "axe":
                self.hit += 15
            elif target.type == "lance":
                self.hit -= 15

        if self.type == "axe":
            if target.type == "lance":
                self.hit += 15
            elif target.type == "sword":
                self.hit -= 15
        
        if self.type == "lance":
            if target.type == "sword":
                self.hit += 15
            elif target.type == "axe":
                self.hit -= 15
        
        if self.type == "light":
            if target.type == "dark":
                self.hit += 15
            elif target.type == "anima":
                self.hit -= 15

        if self.type == "dark":
            if target.type == "anima":
                self.hit += 15
            elif target.type == "light":
                self.hit -= 15
        
        if self.type == "anima":
            if target.type == "light":
                self.hit += 15
            elif target.type == "dark":
                self.hit -=15