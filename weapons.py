from dicts import weapons
import tkinter as tk

class Weapon:
    def __init__(self, weapon):
        self.name = weapon["name"]
        self.wt = int(weapon["wt"])
        self.mt = int(weapon["mt"])
        self.hit = int(weapon["hit"])
        self.crt = int(weapon["crt"])
        self.type = weapon["type"]
        self.effective_against = weapon["effective_against"]
        self.magic = weapon["magic"] == "True"
        self.invert_triangle = weapon["invert_triangle"] == "True"
        self.triangle_inverted = False
        self.other_effect = weapon["other_effect"]

    def calculate_weapon_triangle(self, target):
        if self.invert_triangle == True or target.invert_triangle == True:
            if self.triangle_inverted == False and target.triangle_inverted == False:
                self.type, target.type = target.type, self.type
                self.triangle_inverted = True 
                target.triangle_inverted = True

        # +15 accuracy for advantage, -15 for disadvantage
        if self.type == "sword":
            if target.type == "axe":
                if self.triangle_inverted == True: 
                    return self.hit + 30
                else:
                    return self.hit + 15
            elif target.type == "lance":
                if self.triangle_inverted == True: 
                    return self.hit - 30
                else:
                    return self.hit - 15
            else:
                return self.hit

        if self.type == "axe":
            if target.type == "lance":
                if self.triangle_inverted == True: 
                    return self.hit + 30
                else:
                    return self.hit + 15
            elif target.type == "sword":
                if self.triangle_inverted == True: 
                    return self.hit - 30
                else:
                    return self.hit - 15
            else:
                return self.hit
        
        if self.type == "lance":
            if target.type == "sword":
                if self.triangle_inverted == True: 
                    return self.hit + 30
                else:
                    return self.hit + 15
            elif target.type == "axe":
                if self.triangle_inverted == True: 
                    return self.hit - 30
                else:
                    return self.hit - 15
            else:
                return self.hit
        
        if self.type == "light":
            if target.type == "dark":
                return self.hit + 15
            elif target.type == "anima":
                return self.hit - 15
            else:
                return self.hit

        if self.type == "dark":
            if target.type == "anima":
                return self.hit + 15
            elif target.type == "light":
                return self.hit - 15
            else:
                return self.hit
        
        if self.type == "anima":
            if target.type == "light":
                return self.hit + 15
            elif target.type == "dark":
                return self.hit - 15
            else:
                return self.hit
        
        else:
            return self.hit

    def calculate_effective_damage(self, target, battle_window):
        if self.effective_against != "None":
            if target.type_1 in self.effective_against or target.type_2 in self.effective_against:
                battle_window.insert(tk.END, f"{self.name} is effective against {target.name}\n\n")
                battle_window.see(tk.END)
                self.mt *= 3
