import tkinter as tk

class Battle:
    def __init__(self, unit_1, unit_2, battle_window, button, window):
        self.unit_1 = unit_1
        self.unit_2 = unit_2
        self.battle_window = battle_window
        self.button = button
        self.window = window

    def start_battle(self):
        # Calculate weapon advantage
        self.unit_1.weapon.calculate_weapon_triangle(self.unit_2.weapon, self.battle_window)

        # Calculate effective damage (e.g. bows vs flying)
        self.unit_1.weapon.calculate_effective_damage(self.unit_2.job, self.battle_window)
        self.unit_2.weapon.calculate_effective_damage(self.unit_1.job, self.battle_window)

        # Calculate speed for accuracy & double strike used in attack
        self.unit_1_attack_speed = self.unit_1.calculate_attack_speed()
        self.unit_2_attack_speed = self.unit_2.calculate_attack_speed()


        self.window.update_unit_display()

        self.do_first_battle_step()

    def do_first_battle_step(self):
        self.battle_window.insert(tk.END, f"{self.unit_1.name} attacks {self.unit_2.name}\n")
        self.battle_window.see(tk.END)
        self.unit_1.attack(self.unit_2, self.battle_window)
        self.battle_window.insert(tk.END, f"{self.unit_2.name}'s HP: {self.unit_2.hp}\n\n")
        self.window.update_unit_display()
        self.battle_window.see(tk.END)
        if self.unit_2.hp != 0:
            self.battle_window.after(3000, self.do_second_battle_step)
        else:
            self.battle_window.insert(tk.END, f"{self.unit_2.name} has been defeated!\n\n")
            self.battle_window.see(tk.END)
            self.button.config(text="Battle!", state="normal")
            self.window.battle_in_progress = False


    def do_second_battle_step(self):
        self.battle_window.insert(tk.END, f"{self.unit_2.name} attacks {self.unit_1.name}\n")
        self.battle_window.see(tk.END)
        self.unit_2.attack(self.unit_1, self.battle_window)
        self.battle_window.insert(tk.END, f"{self.unit_1.name}'s HP: {self.unit_1.hp}\n\n")
        self.window.update_unit_display()
        self.battle_window.see(tk.END)
        if self.unit_1.hp != 0:
            self.battle_window.after(3000, self.do_follow_up)
        else:
            self.battle_window.insert(tk.END, f"{self.unit_1.name} has been defeated!\n\n")
            self.battle_window.see(tk.END)
            self.button.config(text="Battle!", state="normal")
            self.window.battle_in_progress = False
    
    def do_follow_up(self):
        if self.unit_1_attack_speed - self.unit_2_attack_speed >= 4:
            self.battle_window.insert(tk.END, f"{self.unit_1.name}'s follow up!\n") 
            self.battle_window.see(tk.END)
            self.battle_window.insert(tk.END, f"{self.unit_1.name} attacks {self.unit_2.name}\n")
            self.battle_window.see(tk.END)
            self.unit_1.attack(self.unit_2, self.battle_window)
            self.battle_window.insert(tk.END, f"{self.unit_2.name}'s HP: {self.unit_2.hp}\n\n")
            self.window.update_unit_display()
            self.battle_window.see(tk.END)
            if self.unit_2.hp != 0:
                self.battle_window.after(3000, self.do_first_battle_step)
            else:
                self.battle_window.insert(tk.END, f"{self.unit_2.name} has been defeated!\n\n")
                self.battle_window.see(tk.END)
                self.button.config(text="Battle!", state="normal")
                self.window.battle_in_progress = False
        
        elif self.unit_2_attack_speed - self.unit_1_attack_speed >= 4:
            self.battle_window.insert(tk.END, f"{self.unit_2.name}'s follow up!\n") 
            self.battle_window.see(tk.END)
            self.battle_window.insert(tk.END, f"{self.unit_2.name} attacks {self.unit_1.name}\n")
            self.battle_window.see(tk.END)
            self.unit_2.attack(self.unit_1, self.battle_window)
            self.battle_window.insert(tk.END, f"{self.unit_1.name}'s HP: {self.unit_1.hp}\n\n")
            self.window.update_unit_display()
            self.battle_window.see(tk.END)
            if self.unit_1.hp != 0:
                self.battle_window.after(3000, self.do_first_battle_step)
            else:
                self.battle_window.insert(tk.END, f"{self.unit_1.name} has been defeated!\n\n")
                self.battle_window.see(tk.END)
                self.button.config(text="Battle!", state="normal")
                self.window.battle_in_progress = False
        
        else:
            self.battle_window.after(0, self.do_first_battle_step)
