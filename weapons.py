from dicts import weapons

class Weapon:
    def __init__(self, weapon):
        self.name = weapon["name"]
        self.mt = weapon["mt"]
        self.hit = weapon["hit"]
        self.crt = weapon["crt"]
        self.wt = weapon["wt"]
        self.type = weapon["type"]
        self.magic = weapon["magic"]
        self.effective_against = weapon["effective_against"]
        self.invert_triangle = weapon["invert_triangle"]

    def calculate_weapon_triangle(self, target):
        if self.invert_triangle == True or target.invert_triangle == True:
            print("TRIANGLE INVERTED")      
            self.type, target.type = target.type, self.type

        # +15 accuracy for advantage, -15 for disadvantage
        if self.type == "sword":
            if target.type == "axe":
                self.hit += 15
                target.hit -= 15
            elif target.type == "lance":
                self.hit -= 15
                target.hit += 15

        if self.type == "axe":
            if target.type == "lance":
                self.hit += 15
                target.hit -= 15
            elif target.type == "sword":
                self.hit -= 15
                target.hit += 15
        
        if self.type == "lance":
            if target.type == "sword":
                self.hit += 15
                target.hit -= 15
            elif target.type == "axe":
                self.hit -= 15
                target.hit += 15
        
        if self.type == "light":
            if target.type == "dark":
                self.hit += 15
                target.hit -= 15
            elif target.type == "anima":
                self.hit -= 15
                target.hit += 15

        if self.type == "dark":
            if target.type == "anima":
                self.hit += 15
                target.hit -= 15
            elif target.type == "light":
                self.hit -= 15
                target.hit += 15
        
        if self.type == "anima":
            if target.type == "light":
                self.hit += 15
                target.hit -= 15
            elif target.type == "dark":
                self.hit -=15
                target.hit += 15

    def calculate_effective_damage(self, target):
        if self.effective_against != None:
            if target.type_1 in self.effective_against or target.type_2 in self.effective_against:
                print(f"{self.name} is effective against {target.name}")
                self.mt *= 3
