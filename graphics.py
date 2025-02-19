from tkinter import Tk, BOTH, Canvas, Button, StringVar, OptionMenu, Label, ttk
from dicts import units, jobs, weapons
from units import Unit
from jobs import Job

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

        self.unit_list = list(units.keys())
        self.jobs_list = list(jobs.keys())
        self.weapons_list = list(weapons.keys())


        self.unit_1_name_label = Label(self.__root, text = "None")
        self.unit_1_level_label = Label(self.__root, text = "None")
        self.unit_1_job_label = Label(self.__root, text = "None")
        self.unit_1_hp_label = Label(self.__root, text = "None")
        self.unit_1_str_label = Label(self.__root, text = "None")
        self.unit_1_skl_label = Label(self.__root, text = "None")
        self.unit_1_spd_label = Label(self.__root, text = "None")
        self.unit_1_lck_label = Label(self.__root, text = "None")
        self.unit_1_defence_label = Label(self.__root, text = "None")
        self.unit_1_res_label = Label(self.__root, text = "None")
        self.unit_1_con_label = Label(self.__root, text = "None")
        self.unit_1_weapon_label = Label(self.__root, text = "None")
        self.unit_1_weapon_wt_label = Label(self.__root, text = "None")
        self.unit_1_weapon_mt_label = Label(self.__root, text = "None")
        self.unit_1_weapon_hit_label = Label(self.__root, text = "None")
        self.unit_1_weapon_crt_label = Label(self.__root, text = "None")

        self.unit_1_clicked = StringVar()
        self.unit_1_clicked.set("Select a Unit")
        self.unit_1_job_clicked = StringVar()
        self.unit_1_job_clicked.set("Select a Class")
        self.unit_1_weapon_clicked = StringVar()
        self.unit_1_weapon_clicked.set("Select a Weapon")
        self.unit_1_promotion_clicked = StringVar()
        self.unit_1_promotion_clicked.set("Choose a Promotion")
        
        if self.unit_1_button is None:
            combo_unit_1 = ttk.Combobox(self.__root, textvariable=self.unit_1_clicked, values=self.unit_list)
            combo_unit_1.pack()
            self.unit_1_button = Button(self.__root, text="Select Unit", command = self.select_unit_1)
            self.unit_1_button.pack()


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__is_running = True  
        while self.__is_running:
            self.redraw()
        print("Window Closed")

    def close(self):
        self.__is_running = False

    def select_unit_1(self):
        unit = self.unit_1_clicked.get()
        self.unit_1 = Unit(units[unit])
        self.update_unit_display()

        self.unit_1_name_label.pack()
        self.unit_1_level_label.pack()
        self.unit_1_job_label.pack()
        self.unit_1_hp_label.pack()
        self.unit_1_str_label.pack()
        self.unit_1_skl_label.pack()
        self.unit_1_spd_label.pack()
        self.unit_1_lck_label.pack()
        self.unit_1_defence_label.pack()
        self.unit_1_res_label.pack()
        self.unit_1_con_label.pack()
        self.unit_1_weapon_label.pack()

        if self.unit_1_job_button is None:
            combo_unit_1_job = ttk.Combobox(self.__root, textvariable=self.unit_1_job_clicked, values=self.jobs_list)
            combo_unit_1_job.pack()
            self.unit_1_job_button = Button(self.__root, text="Apply Class", command = self.apply_unit_1_job)
            self.unit_1_job_button.pack()

    def apply_unit_1_job(self):
        job = self.unit_1_job_clicked.get()
        unit_1_job = jobs[job]
        self.unit_1.assign_job(unit_1_job)
        self.unit_1_promotion_list = list(self.unit_1.job.available_jobs)
        self.update_unit_display()

        if self.unit_1_weapon_button is None:
            combo_unit_1_weapon = ttk.Combobox(self.__root, textvariable=self.unit_1_weapon_clicked, values=self.weapons_list)
            combo_unit_1_weapon.pack()
            self.unit_1_weapon_button = Button(self.__root, text="Equip Weapon", command = self.apply_unit_1_weapon)
            self.unit_1_weapon_button.pack()
        
        if self.unit_1_promotions_button is None:
            combo_unit_1_promotions = ttk.Combobox(self.__root, textvariable=self.unit_1_promotion_clicked, values=self.unit_1_promotion_list)
            combo_unit_1_promotions.pack()
            self.unit_1_promotion_button = Button(self.__root, text="Promote Unit", command = self.unit_1_promote)
            self.unit_1_promotion_button.pack()
    
    def apply_unit_1_weapon(self):
        weapon = self.unit_1_weapon_clicked.get()
        unit_1_weapon = weapons[weapon]
        self.unit_1.assign_weapon(unit_1_weapon)
        self.unit_1_weapon_wt_label.pack()
        self.unit_1_weapon_mt_label.pack()
        self.unit_1_weapon_hit_label.pack()
        self.unit_1_weapon_crt_label.pack()

        self.update_unit_display()

    def unit_1_promote(self):
        print("Promoting Unit")


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
