from tkinter import Tk, BOTH, Canvas, Button, StringVar, OptionMenu, Label, ttk, IntVar, Checkbutton, Entry
from tkinter.scrolledtext import ScrolledText
from dicts import units, jobs, weapons
from units import Unit
from jobs import Job
import sys

class Console(object):
    def __init__(self, textbox):
        self.textbox = textbox

    def write(self, text):
        self.textbox.configure(state="normal")
        self.textbox.insert("end", text)
        self.textbox.see("end")
        self.textbox.configure(state="disabled")

    def flush(self):
        pass

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Battle Simulator")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg = "white", height = height, width = width)
        self.__canvas.pack(fill = BOTH, expand = 1)
        
        self.unit_1_button = None
        self.unit_1_job_button = None
        self.unit_1_weapon_button = None
        self.unit_1_promotions_button = None
        self.unit_1_checkbutton = None
        self.unit_1_level_up_entry = None

        self.unit_list = list(units.keys())
        self.jobs_list = list(jobs.keys())
        
        self.unit_1_name_label = Label(self.__canvas)
        self.unit_1_level_label = Label(self.__canvas)
        self.unit_1_job_label = Label(self.__canvas)
        self.unit_1_hp_label = Label(self.__canvas)
        self.unit_1_str_label = Label(self.__canvas)
        self.unit_1_skl_label = Label(self.__canvas)
        self.unit_1_spd_label = Label(self.__canvas)
        self.unit_1_lck_label = Label(self.__canvas)
        self.unit_1_defence_label = Label(self.__canvas)
        self.unit_1_res_label = Label(self.__canvas)
        self.unit_1_con_label = Label(self.__canvas)
        self.unit_1_weapon_label = Label(self.__canvas)
        self.unit_1_weapon_mt_label = Label(self.__canvas)
        self.unit_1_weapon_wt_label = Label(self.__canvas)
        self.unit_1_weapon_hit_label = Label(self.__canvas)
        self.unit_1_weapon_crt_label = Label(self.__canvas)
        self.unit_1_level_up_label = Label(self.__canvas, text = "Level Up to Level:")

        self.unit_1_unit_labels = {
            "name_label": {'label': self.unit_1_name_label, 'row': 0, 'column':1},
            "level_label": {'label': self.unit_1_level_label, 'row': 1, 'column': 1}, 
            "job_label": {'label': self.unit_1_job_label, 'row': 2, 'column': 1}, 
            "hp_label": {'label': self.unit_1_hp_label, 'row': 3, 'column': 1}, 
            "str_label": {'label': self.unit_1_str_label, 'row': 4, 'column': 1}, 
            "skl_label": {'label': self.unit_1_skl_label, 'row': 5, 'column': 1}, 
            "spd_label": {'label': self.unit_1_spd_label, 'row': 6, 'column': 1}, 
            "lck_label": {'label': self.unit_1_lck_label, 'row': 7, 'column': 1}, 
            "defence_label": {'label': self.unit_1_defence_label, 'row': 8, 'column': 1}, 
            "res_label": {'label': self.unit_1_res_label, 'row': 9, 'column': 1}, 
            "con_label": {'label': self.unit_1_con_label, 'row': 10, 'column': 1}, 
            "weapon_label": {'label': self.unit_1_weapon_label, 'row': 11, 'column': 1}, 
        }
        self.unit_1_weapon_labels = {
            "mt_label": {'label': self.unit_1_weapon_mt_label, 'row': 12, 'column':1},
            "wt_label": {'label': self.unit_1_weapon_wt_label, 'row': 13, 'column':1},
            "hit_label": {'label': self.unit_1_weapon_hit_label, 'row': 14, 'column':1},
            "crt_label": {'label': self.unit_1_weapon_crt_label, 'row': 15, 'column':1},
        }

        for label_info in self.unit_1_unit_labels.values():
            label_info['label'].grid(row=label_info['row'], column=label_info['column'])
        for label_info in self.unit_1_weapon_labels.values():
            label_info['label'].grid(row=label_info['row'], column=label_info['column'])

        


        self.unit_1_clicked = StringVar()
        self.unit_1_clicked.set("Select a Unit")
        self.unit_1_job_clicked = StringVar()
        self.unit_1_job_clicked.set("Select a Class")
        self.unit_1_weapon_clicked = StringVar()
        self.unit_1_weapon_clicked.set("Select a Weapon")
        self.unit_1_promotion_clicked = StringVar()
        self.unit_1_promotion_clicked.set("Choose a Promotion")
        self.unit_1_level_var = StringVar()
        
        if self.unit_1_button is None:
            combo_unit_1 = ttk.Combobox(self.__canvas, textvariable=self.unit_1_clicked, values=self.unit_list)
            combo_unit_1.grid(row=0, column=0)
            self.unit_1_button = Button(self.__canvas, text="Select Unit", command = self.select_unit_1)
            self.unit_1_button.grid(row=1, column=0)

        self.log_widget = ScrolledText(self.__root, height=20, width=80, font=("Arial", "12", "normal"))
        self.log_widget.pack()
        self.redirect_console()



    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__is_running = True  
        while self.__is_running:
            self.redraw()
        self.reset_logging()
        print("Window Closed")

    def close(self):
        self.__is_running = False

    def select_unit_1(self):
        unit = self.unit_1_clicked.get()
        self.unit_1 = Unit(units[unit])
        self.unit_1_promotion_list = self.update_promotions_list(self.unit_1)
        self.unit_1_weapons_list = self.update_weapons_list(self.unit_1)
        self.update_unit_display()

        if self.unit_1_weapon_button is None:
                self.combo_unit_1_weapon = ttk.Combobox(self.__canvas, textvariable=self.unit_1_weapon_clicked, values=self.unit_1_weapons_list)
                self.combo_unit_1_weapon.grid(row=2, column=0)
                self.unit_1_weapon_button = Button(self.__canvas, text="Equip Weapon", 
                                                   command = lambda: self.apply_weapon(self.unit_1,
                                                                                       self.unit_1_weapon_clicked,
                                                                                       self.unit_1_weapon_labels))
                self.unit_1_weapon_button.grid(row=3, column=0)
        
        if self.unit_1_promotions_button is None:
            self.combo_unit_1_promotions = ttk.Combobox(self.__canvas, textvariable=self.unit_1_promotion_clicked, values=self.unit_1_promotion_list)
            self.combo_unit_1_promotions.grid(row=4, column=0)
            self.unit_1_promotions_button = Button(self.__canvas, text="Promote Unit",
                                                   command = lambda: self.apply_promotion(self.unit_1,
                                                                                        self.unit_1_promotion_clicked,
                                                                                        self.combo_unit_1_promotions))
            self.unit_1_promotions_button.grid(row=5, column=0)
        
        if self.unit_1_checkbutton is None:
            self.unit_1_var = IntVar()
            self.checkbutton = Checkbutton(self.__canvas, text = "Change Class?", variable = self.unit_1_var, onvalue = 1, offvalue = 0, command = self.on_unit_1_button_toggle)
            self.checkbutton.grid(row=10, column=0)
        
        if self.unit_1_level_up_entry is None:
            self.unit_1_level_up_entry = Entry(self.__canvas, textvariable= self.unit_1_level_var)
            self.unit_1_level_up_sub_btn = Button(self.__canvas, text = "Submit", command = lambda: self.apply_level_up(self.unit_1,
                                                                                                              self.unit_1_level_var))
            self.unit_1_level_up_label.grid(row=7, column=0)
            self.unit_1_level_up_entry.grid(row=8, column=0)
            self.unit_1_level_up_sub_btn.grid(row=9, column=0)

    def on_unit_1_button_toggle(self):
        if self.unit_1_var.get() == 1:
            self.combo_unit_1_job = ttk.Combobox(self.__canvas, textvariable=self.unit_1_job_clicked, values=self.jobs_list)
            self.combo_unit_1_job.grid(row=12, column=0)
            self.unit_1_job_button = Button(self.__canvas, text="Apply Class", command = lambda: self.apply_job(self.unit_1,
                                                                                                              self.unit_1_job_clicked,
                                                                                                              self.combo_unit_1_weapon,
                                                                                                              self.combo_unit_1_promotions))
            self.unit_1_job_button.grid(row=11, column=0)
        else:
            self.combo_unit_1_job.grid_remove()
            self.unit_1_job_button.grid_remove()

    def apply_job(self, unit, job_clicked, weapon_combobox, promotions_combobox):
        job = job_clicked.get()
        unit_job = jobs[job]
        unit.assign_job(unit_job)
        self.update_weapons_list(unit, weapon_combobox)
        self.update_promotions_list(unit, promotions_combobox)
        self.update_unit_display()
    
    def apply_weapon(self, unit, weapon_clicked, label_dict):
        weapon = weapon_clicked.get()
        unit_weapon = weapons[weapon]
        unit.assign_weapon(unit_weapon)


        self.update_unit_display()

    def apply_promotion(self, unit, promotion_clicked, promotion_combobox):
        target_job = promotion_clicked.get()
        unit.promote(target_job)
        self.update_promotions_list(unit, promotion_combobox)
        self.update_unit_display()


    def update_unit_display(self):
        self.unit_1_name_label.config(text = "Name: " + self.unit_1.name)
        self.unit_1_level_label.config(text = "Level: " + str(self.unit_1.level))
        if self.unit_1.job is not None:
            self.unit_1_job_label.config(text = "Class: " + self.unit_1.job.name)
        else:
            self.unit_1_job_label.config(text = "None")
        self.unit_1_hp_label.config(text = "HP: " + str(self.unit_1.hp))
        self.unit_1_str_label.config(text = "Str: " + str(self.unit_1.str))
        self.unit_1_skl_label.config(text = "Skl: " + str(self.unit_1.skl))
        self.unit_1_spd_label.config(text = "Spd: " + str(self.unit_1.spd))
        self.unit_1_lck_label.config(text = "Lck: " + str(self.unit_1.lck))
        self.unit_1_defence_label.config(text = "Def: " + str(self.unit_1.defence))
        self.unit_1_res_label.config(text = "Res: " + str(self.unit_1.res))
        self.unit_1_con_label.config(text = "Con: " + str(self.unit_1.con))
        if self.unit_1.weapon is not None:
            self.unit_1_weapon_label.config(text = "Weapon: " + self.unit_1.weapon.name)
            self.unit_1_weapon_wt_label.config(text = "Wt: " + str(self.unit_1.weapon.wt))
            self.unit_1_weapon_mt_label.config(text = "Mt: " + str(self.unit_1.weapon.mt))
            self.unit_1_weapon_hit_label.config(text = "Hit: " + str(self.unit_1.weapon.hit))
            self.unit_1_weapon_crt_label.config(text = "Crt: " + str(self.unit_1.weapon.crt))
        
    def apply_level_up(self, unit, level_var):
        target_level = level_var.get()
        unit.set_level(int(target_level))
        level_var.set("")
        self.update_unit_display()

    def update_weapons_list(self, unit, weapon_combobox = None):
        valid_weapons = [weapon_key for weapon_key in weapons.keys()
                        if weapons[weapon_key]['type'] in unit.job.weapon_types]

        if weapon_combobox is not None:
            weapon_combobox['values'] = valid_weapons
        else:
            return valid_weapons

    def update_promotions_list(self, unit, promotions_combobox = None):
        valid_jobs = unit.job.available_jobs

        if promotions_combobox is not None:
            promotions_combobox['values'] = valid_jobs
        else:
            return valid_jobs
        

    def reset_logging(self):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    def test_print(self):
        print("Test Print")
    
    def redirect_console(self):
        console = Console(self.log_widget)
        sys.stdout = console
        sys.stderr = console