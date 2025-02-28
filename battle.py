import tkinter as tk

class Battle:
    def __init__(self, unit_1, unit_2, battle_window, window):
        self.unit_1 = unit_1
        self.unit_2 = unit_2
        self.battle_window = battle_window
        self.window = window

    def start_battle(self):
        # Calculate speed for accuracy & double strike used in attack
        self.unit_1_attack_speed = self.unit_1.calculate_attack_speed()
        self.unit_2_attack_speed = self.unit_2.calculate_attack_speed()

        self.window.update_unit_display()

        self.do_first_battle_step()

    def do_first_battle_step(self):
        self.update_battle_log(f"{self.unit_1.name} attacks {self.unit_2.name}\n")
        self.unit_1.attack(self.unit_2, self.battle_window)
        self.update_battle_log(f"{self.unit_2.name}'s HP: {self.unit_2.hp}\n\n")
        self.window.update_unit_display()

        if self.check_defeat(self.unit_2) == False:
            if self.unit_1.weapon.other_effect == "Brave":
                self.battle_window.after(3000, self.do_first_brave_step)
            else:
                self.battle_window.after(3000, self.do_second_battle_step)


    def do_second_battle_step(self):
        self.update_battle_log(f"{self.unit_2.name} attacks {self.unit_1.name}\n")
        self.unit_2.attack(self.unit_1, self.battle_window)
        self.update_battle_log(f"{self.unit_1.name}'s HP: {self.unit_1.hp}\n\n")
        self.window.update_unit_display()

        if self.check_defeat(self.unit_1) == False:
            if self.unit_2.weapon.other_effect == "Brave":
                self.battle_window.after(3000, self.do_second_brave_step)
            else:
                self.battle_window.after(3000, self.do_follow_up)


    def do_follow_up(self):
        if self.unit_1_attack_speed - self.unit_2_attack_speed >= 4:
            self.update_battle_log(f"{self.unit_1.name}'s follow up!\n") 
            self.update_battle_log(f"{self.unit_1.name} attacks {self.unit_2.name}\n")
            self.unit_1.attack(self.unit_2, self.battle_window)
            self.update_battle_log(f"{self.unit_2.name}'s HP: {self.unit_2.hp}\n\n")
            self.window.update_unit_display()
            
            if self.check_defeat(self.unit_2) == False:
                if self.unit_1.weapon.other_effect == "Brave":
                    self.battle_window.after(3000, self.do_first_brave_follow_up)
                else:
                    self.battle_window.after(3000, self.do_first_battle_step)
                   
        elif self.unit_2_attack_speed - self.unit_1_attack_speed >= 4:
            self.update_battle_log(f"{self.unit_2.name}'s follow up!\n") 
            self.update_battle_log(f"{self.unit_2.name} attacks {self.unit_1.name}\n")
            self.unit_2.attack(self.unit_1, self.battle_window)
            self.update_battle_log(f"{self.unit_1.name}'s HP: {self.unit_1.hp}\n\n")
            self.window.update_unit_display()
            if self.check_defeat(self.unit_1) == False:
                if self.unit_2.weapon.other_effect == "Brave":
                    self.battle_window.after(3000, self.do_second_brave_follow_up)
                else:
                    self.battle_window.after(3000, self.do_first_battle_step)
        
        else:
            self.battle_window.after(0, self.do_first_battle_step)


    def do_first_brave_step(self):
        self.update_battle_log(f"{self.unit_1.name}'s Brave attack!\n")
        self.update_battle_log(f"{self.unit_1.name} attacks {self.unit_2.name}\n")
        self.unit_1.attack(self.unit_2, self.battle_window)
        self.update_battle_log(f"{self.unit_2.name}'s HP: {self.unit_2.hp}\n\n")
        self.window.update_unit_display()
        
        if self.check_defeat(self.unit_2) == False:
            self.battle_window.after(3000, self.do_second_battle_step)


    def do_second_brave_step(self):
        self.update_battle_log(f"{self.unit_2.name}'s Brave attack!\n")
        self.update_battle_log(f"{self.unit_2.name} attacks {self.unit_1.name}\n")
        self.unit_2.attack(self.unit_1, self.battle_window)
        self.update_battle_log(f"{self.unit_1.name}'s HP: {self.unit_1.hp}\n\n")
        self.window.update_unit_display()

        if self.check_defeat(self.unit_2) == False:
            self.battle_window.after(3000, self.do_follow_up)


    def do_first_brave_follow_up(self):
        self.update_battle_log(f"{self.unit_1.name}'s Brave follow up!\n")
        self.unit_1.attack(self.unit_2, self.battle_window)
        self.update_battle_log(f"{self.unit_2.name}'s HP: {self.unit_2.hp}\n\n")
        self.window.update_unit_display()

        if self.check_defeat(self.unit_2) == False:
            self.battle_window.after(3000, self.do_first_battle_step)

    def do_second_brave_follow_up(self):
        self.update_battle_log(f"{self.unit_2.name}'s Brave follow up!\n")
        self.update_battle_log(f"{self.unit_2.name} attacks {self.unit_1.name}\n")
        self.unit_2.attack(self.unit_1, self.battle_window)
        self.update_battle_log(f"{self.unit_1.name}'s HP: {self.unit_1.hp}\n\n")
        self.window.update_unit_display()
        
        if self.check_defeat(self.unit_1) == False:
            self.battle_window.after(3000, self.do_first_battle_step)

    def check_defeat(self, defeated_unit):
        if defeated_unit.hp == 0:
            self.update_battle_log(f"{defeated_unit.name} has been defeated!\n\n")
            self.window.enable_buttons()
            self.window.battle_in_progress = False
            return True
        return False

    def update_battle_log(self, message):
        self.battle_window.insert(tk.END, message)
        self.battle_window.see(tk.END)