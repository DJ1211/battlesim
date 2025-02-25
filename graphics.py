from tkinter import Tk, BOTH, Frame, Canvas, Button, StringVar, OptionMenu, Label, ttk, IntVar, Checkbutton, Entry
from tkinter.scrolledtext import ScrolledText
from dicts import units, jobs, weapons, terrain
from units import Unit
from battle import Battle

class Window:
    def __init__(self):
        self.__root = Tk()
        self.__root.title("Battle Simulator")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.unit_1 = None
        self.unit_2 = None
      
        self.unit_list = list(units.keys())
        self.jobs_list = list(jobs.keys())
        self.terrain_list = list(terrain.keys())

        self.unit_1_clicked = StringVar()
        self.unit_1_clicked.set("Select a Unit")
        self.unit_1_job_clicked = StringVar()
        self.unit_1_job_clicked.set("Select a Class")
        self.unit_1_weapon_clicked = StringVar()
        self.unit_1_weapon_clicked.set("Select a Weapon")
        self.unit_1_promotion_clicked = StringVar()
        self.unit_1_promotion_clicked.set("Choose a Promotion")
        self.unit_1_terrain_clicked = StringVar()
        self.unit_1_terrain_clicked.set("Choose Terrain")
        self.unit_1_level_var = StringVar()
        self.unit_1_var = IntVar()

        self.unit_2_clicked = StringVar()
        self.unit_2_clicked.set("Select a Unit")
        self.unit_2_job_clicked = StringVar()
        self.unit_2_job_clicked.set("Select a Class")
        self.unit_2_weapon_clicked = StringVar()
        self.unit_2_weapon_clicked.set("Select a Weapon")
        self.unit_2_promotion_clicked = StringVar()
        self.unit_2_promotion_clicked.set("Choose a Promotion")
        self.unit_2_terrain_clicked = StringVar()
        self.unit_2_terrain_clicked.set("Choose Terrain")
        self.unit_2_level_var = StringVar()
        self.unit_2_var = IntVar()

        # Create Frames

        self.unit_1_label_frame = Frame(self.__root)
        self.unit_1_button_frame = Frame(self.__root)
        self.unit_2_label_frame = Frame(self.__root)
        self.unit_2_button_frame = Frame(self.__root)
        self.battle_window_frame = Frame(self.__root)

        # Position Frames

        self.unit_1_button_frame.grid(row=0, column=4, sticky='nw')
        self.unit_1_label_frame.grid(row=0, column=3, sticky='nw')
        self.battle_window_frame.grid(row=0, column=2, sticky='nw')
        self.unit_2_label_frame.grid(row=0, column=1, sticky='nw')
        self.unit_2_button_frame.grid(row=0, column=0, sticky='nw')

        # Create all buttons 

        self.combo_unit_1 = ttk.Combobox(self.unit_1_button_frame, textvariable=self.unit_1_clicked, values=self.unit_list)
        self.unit_1_button = Button(self.unit_1_button_frame, text="Select Unit", command = self.select_unit_1)
        self.combo_unit_1_weapon = ttk.Combobox(self.unit_1_button_frame, textvariable=self.unit_1_weapon_clicked, values=None, state='disabled')
        self.unit_1_weapon_button = Button(self.unit_1_button_frame, text="Equip Weapon", 
                                                   command = lambda: self.apply_weapon(self.unit_1,
                                                                                       self.unit_1_weapon_clicked),
                                                    state='disabled')
        self.combo_unit_1_promotions = ttk.Combobox(self.unit_1_button_frame, textvariable=self.unit_1_promotion_clicked, values=None, state='disabled')
        self.unit_1_promotions_button = Button(self.unit_1_button_frame, text="Promote Unit",
                                                   command = lambda: self.apply_promotion(self.unit_1,
                                                                                        self.unit_1_promotion_clicked,
                                                                                        self.combo_unit_1_promotions),
                                                    state='disabled')
        self.combo_unit_1_terrain = ttk.Combobox(self.unit_1_button_frame, textvariable=self.unit_1_terrain_clicked, values=self.terrain_list, state='disabled')
        self.unit_1_terrain_button = Button(self.unit_1_button_frame, text="Apply Terrain",
                                                   command = lambda: self.apply_terrain(self.unit_1,
                                                                                        self.unit_1_terrain_clicked),
                                                    state='disabled')
        self.unit_1_checkbutton = Checkbutton(self.unit_1_button_frame, text = "Change Class?", variable = self.unit_1_var, onvalue = 1, offvalue = 0, command = self.on_unit_1_button_toggle, state='disabled')
        self.unit_1_level_up_entry = Entry(self.unit_1_button_frame, textvariable= self.unit_1_level_var, state='disabled')
        self.unit_1_level_up_sub_btn = Button(self.unit_1_button_frame, text = "Level Up", command = lambda: self.apply_level_up(self.unit_1,
                                                                                                              self.unit_1_level_var),
                                                                                                              state='disabled')
        self.combo_unit_1_job = ttk.Combobox(self.unit_1_button_frame, textvariable=self.unit_1_job_clicked, values=self.jobs_list)
        self.unit_1_job_button = Button(self.unit_1_button_frame, text="Apply Class", command = lambda: self.apply_job(self.unit_1,
                                                                                                              self.unit_1_job_clicked,
                                                                                                              self.combo_unit_1_weapon,
                                                                                                              self.combo_unit_1_promotions))
        


        self.combo_unit_2 = ttk.Combobox(self.unit_2_button_frame, textvariable=self.unit_2_clicked, values=self.unit_list)
        self.unit_2_button = Button(self.unit_2_button_frame, text="Select Unit", command = self.select_unit_2)
        self.combo_unit_2_weapon = ttk.Combobox(self.unit_2_button_frame, textvariable=self.unit_2_weapon_clicked, values=None, state='disabled')
        self.unit_2_weapon_button = Button(self.unit_2_button_frame, text="Equip Weapon", 
                                                   command = lambda: self.apply_weapon(self.unit_2,
                                                                                       self.unit_2_weapon_clicked),
                                                                                       state='disabled')
        self.combo_unit_2_promotions = ttk.Combobox(self.unit_2_button_frame, textvariable=self.unit_2_promotion_clicked, values=None, state='disabled')
        self.unit_2_promotions_button = Button(self.unit_2_button_frame, text="Promote Unit",
                                                   command = lambda: self.apply_promotion(self.unit_2,
                                                                                        self.unit_2_promotion_clicked,
                                                                                        self.combo_unit_2_promotions),
                                                                                        state='disabled')
        self.combo_unit_2_terrain = ttk.Combobox(self.unit_2_button_frame, textvariable=self.unit_2_terrain_clicked, values=self.terrain_list, state='disabled')
        self.unit_2_terrain_button = Button(self.unit_2_button_frame, text="Apply Terrain",
                                                   command = lambda: self.apply_terrain(self.unit_2,
                                                                                        self.unit_2_terrain_clicked),
                                                    state='disabled')
        self.unit_2_checkbutton = Checkbutton(self.unit_2_button_frame, text = "Change Class?", variable = self.unit_2_var, onvalue = 1, offvalue = 0, command = self.on_unit_2_button_toggle, state='disabled')
        self.unit_2_level_up_entry = Entry(self.unit_2_button_frame, textvariable= self.unit_2_level_var, state='disabled')
        self.unit_2_level_up_sub_btn = Button(self.unit_2_button_frame, text = "Level Up", command = lambda: self.apply_level_up(self.unit_2,
                                                                                                              self.unit_2_level_var),
                                                                                                              state='disabled')
        self.combo_unit_2_job = ttk.Combobox(self.unit_2_button_frame, textvariable=self.unit_2_job_clicked, values=self.jobs_list)
        self.unit_2_job_button = Button(self.unit_2_button_frame, text="Apply Class", command = lambda: self.apply_job(self.unit_2,
                                                                                                              self.unit_2_job_clicked,
                                                                                                              self.combo_unit_2_weapon,
                                                                                                              self.combo_unit_2_promotions))
        
        self.battle_button = Button(self.battle_window_frame, text="Battle!", command=None, state='disabled')
        
        # Create all labels

        self.unit_1_label = Label(self.unit_1_label_frame, text = "Attacking Unit", font=('', 12, 'bold'), width=20)
        self.unit_1_name_label = Label(self.unit_1_label_frame, text = "Name: None", width=20)
        self.unit_1_level_label = Label(self.unit_1_label_frame, text = "Level: None", width=20)
        self.unit_1_job_label = Label(self.unit_1_label_frame, text = "Class: None", width=20)
        self.unit_1_hp_label = Label(self.unit_1_label_frame, text = "Hp: None", width=20)
        self.unit_1_str_label = Label(self.unit_1_label_frame, text = "Str: None", width=20)
        self.unit_1_skl_label = Label(self.unit_1_label_frame, text = "Skl: None", width=20)
        self.unit_1_spd_label = Label(self.unit_1_label_frame, text = "Spd: None", width=20)
        self.unit_1_lck_label = Label(self.unit_1_label_frame, text = "Lck: None", width=20)
        self.unit_1_defence_label = Label(self.unit_1_label_frame, text = "Def: None", width=20)
        self.unit_1_res_label = Label(self.unit_1_label_frame, text = "Res: None", width=20)
        self.unit_1_con_label = Label(self.unit_1_label_frame, text = "Con: None", width=20)
        self.unit_1_weapon_label = Label(self.unit_1_label_frame, text = "Weapon: None", width=20)
        self.unit_1_weapon_mt_label = Label(self.unit_1_label_frame, text = "Mt: None", width=20)
        self.unit_1_weapon_wt_label = Label(self.unit_1_label_frame, text = "Wt: None", width=20)
        self.unit_1_weapon_hit_label = Label(self.unit_1_label_frame, text = "Hit: None", width=20)
        self.unit_1_weapon_crt_label = Label(self.unit_1_label_frame, text = "Crt: None", width=20)
        self.unit_1_terrain_type_label = Label(self.unit_1_label_frame, text = "Terrain: None", width=20)
        self.unit_1_terrain_def_label = Label(self.unit_1_label_frame, text = "Def Bonus: None", width=20)
        self.unit_1_terrain_avoid_label = Label(self.unit_1_label_frame, text = "Avoid Bonus: None", width=20)
        self.unit_1_level_up_label = Label(self.unit_1_button_frame, text = "Level Up to Level:", width=20)

        self.unit_2_label = Label(self.unit_2_label_frame, text = "Defending Unit", font=('', 12, 'bold'), width=20)
        self.unit_2_name_label = Label(self.unit_2_label_frame, text = "Name: None", width=20)
        self.unit_2_level_label = Label(self.unit_2_label_frame, text = "Level: None", width=20)
        self.unit_2_job_label = Label(self.unit_2_label_frame, text = "Class: None", width=20)
        self.unit_2_hp_label = Label(self.unit_2_label_frame, text = "Hp: None", width=20)
        self.unit_2_str_label = Label(self.unit_2_label_frame, text = "Str: None", width=20)
        self.unit_2_skl_label = Label(self.unit_2_label_frame, text = "Skl: None", width=20)
        self.unit_2_spd_label = Label(self.unit_2_label_frame, text = "Spd: None", width=20)
        self.unit_2_lck_label = Label(self.unit_2_label_frame, text = "Lck: None", width=20)
        self.unit_2_defence_label = Label(self.unit_2_label_frame, text = "Def: None", width=20)
        self.unit_2_res_label = Label(self.unit_2_label_frame, text = "Res: None", width=20)
        self.unit_2_con_label = Label(self.unit_2_label_frame, text = "Con: None", width=20)
        self.unit_2_weapon_label = Label(self.unit_2_label_frame, text = "Weapon: None", width=20)
        self.unit_2_weapon_mt_label = Label(self.unit_2_label_frame, text = "Mt: None", width=20)
        self.unit_2_weapon_wt_label = Label(self.unit_2_label_frame, text = "Wt: None", width=20)
        self.unit_2_weapon_hit_label = Label(self.unit_2_label_frame, text = "Hit: None", width=20)
        self.unit_2_weapon_crt_label = Label(self.unit_2_label_frame, text = "Crt: None", width=20)
        self.unit_2_terrain_type_label = Label(self.unit_2_label_frame, text = "Terrain: None", width=20)
        self.unit_2_terrain_def_label = Label(self.unit_2_label_frame, text = "Def Bonus: None", width=20)
        self.unit_2_terrain_avoid_label = Label(self.unit_2_label_frame, text = "Avoid Bonus: None", width=20)
        self.unit_2_level_up_label = Label(self.unit_2_button_frame, text = "Level Up to Level:", width=20)

        # Pack all buttons & labels into grid

        self.unit_1_buttons_combobox = {
            "unit_1_combo": {'button': self.combo_unit_1, 'row': 0, 'column': 4, 'padx': 5, 'pady': 5},
            "unit_1_button": {'button': self.unit_1_button, 'row': 1, 'column': 4, 'padx': 5, 'pady': 5},
            "unit_1_weapon_combo": {'button': self.combo_unit_1_weapon, 'row': 2, 'column': 4, 'padx': 5, 'pady': 5},
            "unit_1_weapon_button": {'button': self.unit_1_weapon_button, 'row': 3, 'column': 4, 'padx': 5, 'pady': 5},
            "unit_1_level_label": {'button': self.unit_1_level_up_label, 'row': 4, 'column': 4, 'padx': 5, 'pady': 5},
            "unit_1_level_entry": {'button': self.unit_1_level_up_entry, 'row': 5, 'column': 4, 'padx': 5, 'pady': 5},
            "unit_1_level_button": {'button': self.unit_1_level_up_sub_btn, 'row': 6, 'column': 4, 'padx': 5, 'pady': 5},
            "unit_1_promotion_combo": {'button': self.combo_unit_1_promotions, 'row': 7, 'column': 4, 'padx': 5, 'pady': 5},
            "unit_1_promotion_button": {'button': self.unit_1_promotions_button, 'row': 8, 'column': 4, 'padx': 5, 'pady': 5},
            "unit_1_terrain_combo": {'button': self.combo_unit_1_terrain, 'row': 9, 'column': 4, 'padx': 5, 'pady': 5},
            "unit_1_terrain_button": {'button': self.unit_1_terrain_button, 'row': 10, 'column': 4, 'padx': 5, 'pady': 5},
            "unit_1_checkbutton": {'button': self.unit_1_checkbutton, 'row': 11, 'column': 4, 'padx': 5, 'pady': 5},
            "unit_1_job_combo": {'button': self.combo_unit_1_job, 'row': 12, 'column': 4, 'padx': 5, 'pady': 5},
            "unit_1_job_button": {'button': self.unit_1_job_button, 'row': 13, 'column': 4, 'padx': 5, 'pady': 5},
        }

        self.unit_1_unit_labels = {
            "unit_label": {'label': self.unit_1_label,'row': 0, 'column': 3, 'padx': 5, 'pady': 5},
            "name_label": {'label': self.unit_1_name_label, 'row': 1, 'column': 3, 'padx': 5, 'pady': 5},
            "level_label": {'label': self.unit_1_level_label, 'row': 2, 'column': 3, 'padx': 5, 'pady': 5}, 
            "job_label": {'label': self.unit_1_job_label, 'row': 3, 'column': 3, 'padx': 5, 'pady': 5}, 
            "hp_label": {'label': self.unit_1_hp_label, 'row': 4, 'column': 3, 'padx': 5, 'pady': 5}, 
            "str_label": {'label': self.unit_1_str_label, 'row': 5, 'column': 3, 'padx': 5, 'pady': 5}, 
            "skl_label": {'label': self.unit_1_skl_label, 'row': 6, 'column': 3, 'padx': 5, 'pady': 5}, 
            "spd_label": {'label': self.unit_1_spd_label, 'row': 7, 'column': 3, 'padx': 5, 'pady': 5}, 
            "lck_label": {'label': self.unit_1_lck_label, 'row': 8, 'column': 3, 'padx': 5, 'pady': 5}, 
            "defence_label": {'label': self.unit_1_defence_label, 'row': 9, 'column': 3, 'padx': 5, 'pady': 5}, 
            "res_label": {'label': self.unit_1_res_label, 'row': 10, 'column': 3, 'padx': 5, 'pady': 5}, 
            "con_label": {'label': self.unit_1_con_label, 'row': 11, 'column': 3, 'padx': 5, 'pady': 5}, 
            "weapon_label": {'label': self.unit_1_weapon_label, 'row': 12, 'column': 3, 'padx': 5, 'pady': 5}, 
        }

        self.unit_1_weapon_labels = {
            "mt_label": {'label': self.unit_1_weapon_mt_label, 'row': 13, 'column':3, 'padx': 5, 'pady': 5},
            "wt_label": {'label': self.unit_1_weapon_wt_label, 'row': 14, 'column':3, 'padx': 5, 'pady': 5},
            "hit_label": {'label': self.unit_1_weapon_hit_label, 'row': 15, 'column':3, 'padx': 5, 'pady': 5},
            "crt_label": {'label': self.unit_1_weapon_crt_label, 'row': 16, 'column':3, 'padx': 5, 'pady': 5},
        }

        self.unit_1_terrain_labels = {
            "terrain_type_label": {'label': self.unit_1_terrain_type_label, 'row': 17, 'column': 3, 'padx': 5, 'pady': 5},
            "terrain_def_label": {'label': self.unit_1_terrain_def_label, 'row': 18, 'column': 3, 'padx': 5, 'pady': 5},
            "terrain_avoid_label": {'label': self.unit_1_terrain_avoid_label, 'row': 19, 'column': 3, 'padx': 5, 'pady': 5},
        }

        for button_info in self.unit_1_buttons_combobox.values():
            button_info['button'].grid(row=button_info['row'], column=button_info['column'], padx=button_info['padx'], pady=button_info['pady'])
        for label_info in self.unit_1_unit_labels.values():
            label_info['label'].grid(row=label_info['row'], column=label_info['column'], padx=button_info['padx'], pady=button_info['pady'])
        for label_info in self.unit_1_weapon_labels.values():
            label_info['label'].grid(row=label_info['row'], column=label_info['column'], padx=button_info['padx'], pady=button_info['pady'])
        for label_info in self.unit_1_terrain_labels.values():
            label_info['label'].grid(row=label_info['row'], column=label_info['column'], padx=button_info['padx'], pady=button_info['pady'])

        self.unit_2_buttons_combobox = {
            "unit_2_combo": {'button': self.combo_unit_2, 'row': 0, 'column': 0, 'padx': 5, 'pady': 5},
            "unit_2_button": {'button': self.unit_2_button, 'row': 1, 'column': 0, 'padx': 5, 'pady': 5},
            "unit_2_weapon_combo": {'button': self.combo_unit_2_weapon, 'row': 2, 'column': 0, 'padx': 5, 'pady': 5},
            "unit_2_weapon_button": {'button': self.unit_2_weapon_button, 'row': 3, 'column': 0, 'padx': 5, 'pady': 5},
            "unit_2_level_label": {'button': self.unit_2_level_up_label, 'row': 4, 'column': 0, 'padx': 5, 'pady': 5},
            "unit_2_level_entry": {'button': self.unit_2_level_up_entry, 'row': 5, 'column': 0, 'padx': 5, 'pady': 5},
            "unit_2_level_button": {'button': self.unit_2_level_up_sub_btn, 'row': 6, 'column': 0, 'padx': 5, 'pady': 5},
            "unit_2_promotion_combo": {'button': self.combo_unit_2_promotions, 'row': 7, 'column': 0, 'padx': 5, 'pady': 5},
            "unit_2_promotion_button": {'button': self.unit_2_promotions_button, 'row': 8, 'column': 0, 'padx': 5, 'pady': 5},
            "unit_2_terrain_combo": {'button': self.combo_unit_2_terrain, 'row': 9, 'column': 0, 'padx': 5, 'pady': 5},
            "unit_2_terrain_button": {'button': self.unit_2_terrain_button, 'row': 10, 'column': 0, 'padx': 5, 'pady': 5},
            "unit_2_checkbutton": {'button': self.unit_2_checkbutton, 'row': 11, 'column': 0, 'padx': 5, 'pady': 5},
            "unit_2_job_combo": {'button': self.combo_unit_2_job, 'row': 12, 'column': 0, 'padx': 5, 'pady': 5},
            "unit_2_job_button": {'button': self.unit_2_job_button, 'row': 13, 'column': 0, 'padx': 5, 'pady': 5},
        }

        self.unit_2_unit_labels = {
            "unit_label": {'label': self.unit_2_label,'row': 0, 'column': 1, 'padx': 5, 'pady': 5},
            "name_label": {'label': self.unit_2_name_label, 'row': 1, 'column':1, 'padx': 5, 'pady': 5},
            "level_label": {'label': self.unit_2_level_label, 'row': 2, 'column': 1, 'padx': 5, 'pady': 5}, 
            "job_label": {'label': self.unit_2_job_label, 'row': 3, 'column': 1, 'padx': 5, 'pady': 5}, 
            "hp_label": {'label': self.unit_2_hp_label, 'row': 4, 'column': 1, 'padx': 5, 'pady': 5}, 
            "str_label": {'label': self.unit_2_str_label, 'row': 5, 'column': 1, 'padx': 5, 'pady': 5}, 
            "skl_label": {'label': self.unit_2_skl_label, 'row': 6, 'column': 1, 'padx': 5, 'pady': 5}, 
            "spd_label": {'label': self.unit_2_spd_label, 'row': 7, 'column': 1, 'padx': 5, 'pady': 5}, 
            "lck_label": {'label': self.unit_2_lck_label, 'row': 8, 'column': 1, 'padx': 5, 'pady': 5}, 
            "defence_label": {'label': self.unit_2_defence_label, 'row': 9, 'column': 1, 'padx': 5, 'pady': 5}, 
            "res_label": {'label': self.unit_2_res_label, 'row': 10, 'column': 1, 'padx': 5, 'pady': 5}, 
            "con_label": {'label': self.unit_2_con_label, 'row': 11, 'column': 1, 'padx': 5, 'pady': 5}, 
            "weapon_label": {'label': self.unit_2_weapon_label, 'row': 12, 'column': 1, 'padx': 5, 'pady': 5}, 
        }

        self.unit_2_weapon_labels = {
            "mt_label": {'label': self.unit_2_weapon_mt_label, 'row': 13, 'column':1, 'padx': 5, 'pady': 5},
            "wt_label": {'label': self.unit_2_weapon_wt_label, 'row': 14, 'column':1, 'padx': 5, 'pady': 5},
            "hit_label": {'label': self.unit_2_weapon_hit_label, 'row': 15, 'column':1, 'padx': 5, 'pady': 5},
            "crt_label": {'label': self.unit_2_weapon_crt_label, 'row': 16, 'column':1, 'padx': 5, 'pady': 5},
        }
        
        self.unit_2_terrain_labels = {
            "terrain_type_label": {'label': self.unit_2_terrain_type_label, 'row': 17, 'column': 1, 'padx': 5, 'pady': 5},
            "terrain_def_label": {'label': self.unit_2_terrain_def_label, 'row': 18, 'column': 1, 'padx': 5, 'pady': 5},
            "terrain_avoid_label": {'label': self.unit_2_terrain_avoid_label, 'row': 19, 'column': 1, 'padx': 5, 'pady': 5},
        }

        for button_info in self.unit_2_buttons_combobox.values():
            button_info['button'].grid(row=button_info['row'], column=button_info['column'], padx=button_info['padx'], pady=button_info['pady'])
        for label_info in self.unit_2_unit_labels.values():
            label_info['label'].grid(row=label_info['row'], column=label_info['column'], padx=button_info['padx'], pady=button_info['pady'])
        for label_info in self.unit_2_weapon_labels.values():
            label_info['label'].grid(row=label_info['row'], column=label_info['column'], padx=button_info['padx'], pady=button_info['pady'])
        for label_info in self.unit_2_terrain_labels.values():
            label_info['label'].grid(row=label_info['row'], column=label_info['column'], padx=button_info['padx'], pady=button_info['pady'])

        # Create battle window  & button

        self.battle_window = ScrolledText(self.battle_window_frame, height=20, width=60, font=("Arial", "12", "normal"))
        self.battle_window.grid(row=0, column=2, rowspan=16, sticky='ns', padx=20)
        self.battle_button.grid(row=18, column=2, pady=20)

        # Set window size

        self.__root.update()
        window_width = self.__root.winfo_width()
        window_height = self.__root.winfo_height()
        self.__root.minsize(window_width, window_height)
        self.__root.maxsize(window_width, window_height)

        # Hide Job Change buttons

        self.unit_1_job_button.grid_remove()
        self.combo_unit_1_job.grid_remove()
        self.unit_2_job_button.grid_remove()
        self.combo_unit_2_job.grid_remove()
        
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
        self.unit_1_promotion_list = self.update_promotions_list(self.unit_1)
        self.unit_1_weapons_list = self.update_weapons_list(self.unit_1)
        self.update_unit_display()

        self.combo_unit_1_weapon['values'] = self.unit_1_weapons_list
        self.combo_unit_1_promotions['values'] = self.unit_1_promotion_list
        self.unit_1_weapon_button.config(state='normal')
        self.combo_unit_1_weapon.config(state='normal')
        self.combo_unit_1_promotions.config(state='normal')
        self.unit_1_promotions_button.config(state='normal')
        self.unit_1_level_up_sub_btn.config(state='normal')
        self.unit_1_checkbutton.config(state='normal')
        self.unit_1_level_up_entry.config(state='normal')
        self.unit_1_terrain_button.config(state='normal')
        self.combo_unit_1_terrain.config(state='normal')

    def on_unit_1_button_toggle(self):
        if self.unit_1_var.get() == 1:
            self.combo_unit_1_job.grid()
            self.unit_1_job_button.grid()        
        else:
            self.combo_unit_1_job.grid_remove()
            self.unit_1_job_button.grid_remove()

    def select_unit_2(self):
        unit = self.unit_2_clicked.get()
        self.unit_2 = Unit(units[unit])
        self.unit_2_promotion_list = self.update_promotions_list(self.unit_2)
        self.unit_2_weapons_list = self.update_weapons_list(self.unit_2)
        self.update_unit_display()

        self.combo_unit_2_weapon['values'] = self.unit_2_weapons_list
        self.combo_unit_2_promotions['values'] = self.unit_2_promotion_list
        self.unit_2_weapon_button.config(state='normal')
        self.combo_unit_2_weapon.config(state='normal')
        self.combo_unit_2_promotions.config(state='normal')
        self.unit_2_promotions_button.config(state='normal')
        self.unit_2_level_up_sub_btn.config(state='normal')
        self.unit_2_checkbutton.config(state='normal')
        self.unit_2_level_up_entry.config(state='normal')
        self.unit_2_terrain_button.config(state='normal')
        self.combo_unit_2_terrain.config(state='normal')

    def on_unit_2_button_toggle(self):
        if self.unit_2_var.get() == 1:
            self.combo_unit_2_job.grid()
            self.unit_2_job_button.grid()
        else:
            self.combo_unit_2_job.grid_remove()
            self.unit_2_job_button.grid_remove()


    def apply_job(self, unit, job_clicked, weapon_combobox, promotions_combobox):
        job = job_clicked.get()
        unit_job = jobs[job]
        unit.assign_job(unit_job)
        self.update_weapons_list(unit, weapon_combobox)
        self.update_promotions_list(unit, promotions_combobox)
        self.update_unit_display()
    
    def apply_weapon(self, unit, weapon_clicked):
        weapon = weapon_clicked.get()
        unit_weapon = weapons[weapon]
        unit.assign_weapon(unit_weapon, self.battle_window)
        self.update_unit_display()

    def apply_promotion(self, unit, promotion_clicked, promotion_combobox):
        target_job = promotion_clicked.get()
        unit.promote(target_job, self.battle_window)
        self.update_promotions_list(unit, promotion_combobox)
        self.update_unit_display()

    def apply_level_up(self, unit, level_var):
        target_level = level_var.get()
        unit.set_level(self.battle_window, int(target_level))
        level_var.set("")
        self.update_unit_display()

    def apply_terrain(self, unit, terrain_clicked):
        terrain_selection = terrain_clicked.get()
        unit_terrain = terrain[terrain_selection]
        unit.assign_terrain(unit_terrain)
        self.update_unit_display()

    def update_unit_display(self):
        if self.unit_1 is not None:
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
            if self.unit_1.terrain is not None:
                self.unit_1_terrain_type_label.config(text = "Terrain: " + self.unit_1.terrain.name)
                self.unit_1_terrain_def_label.config(text = "Def Bonus: " + str(self.unit_1.terrain.def_bonus))
                self.unit_1_terrain_avoid_label.config(text = "Avoid Bonus: " + str(self.unit_1.terrain.avoid))
        
        if self.unit_2 is not None:
            self.unit_2_name_label.config(text = "Name: " + self.unit_2.name)
            self.unit_2_level_label.config(text = "Level: " + str(self.unit_2.level))
            if self.unit_2.job is not None:
                self.unit_2_job_label.config(text = "Class: " + self.unit_2.job.name)
            else:
                self.unit_2_job_label.config(text = "None")
            self.unit_2_hp_label.config(text = "HP: " + str(self.unit_2.hp))
            self.unit_2_str_label.config(text = "Str: " + str(self.unit_2.str))
            self.unit_2_skl_label.config(text = "Skl: " + str(self.unit_2.skl))
            self.unit_2_spd_label.config(text = "Spd: " + str(self.unit_2.spd))
            self.unit_2_lck_label.config(text = "Lck: " + str(self.unit_2.lck))
            self.unit_2_defence_label.config(text = "Def: " + str(self.unit_2.defence))
            self.unit_2_res_label.config(text = "Res: " + str(self.unit_2.res))
            self.unit_2_con_label.config(text = "Con: " + str(self.unit_2.con))
            if self.unit_2.weapon is not None:
                self.unit_2_weapon_label.config(text = "Weapon: " + self.unit_2.weapon.name)
                self.unit_2_weapon_wt_label.config(text = "Wt: " + str(self.unit_2.weapon.wt))
                self.unit_2_weapon_mt_label.config(text = "Mt: " + str(self.unit_2.weapon.mt))
                self.unit_2_weapon_hit_label.config(text = "Hit: " + str(self.unit_2.weapon.hit))
                self.unit_2_weapon_crt_label.config(text = "Crt: " + str(self.unit_2.weapon.crt))
            if self.unit_2.terrain is not None:
                self.unit_2_terrain_type_label.config(text = "Terrain: " + self.unit_2.terrain.name)
                self.unit_2_terrain_def_label.config(text = "Def Bonus: " + str(self.unit_2.terrain.def_bonus))
                self.unit_2_terrain_avoid_label.config(text = "Avoid Bonus: " + str(self.unit_2.terrain.avoid))

        if self.unit_1 is not None and self.unit_2 is not None:
            if self.unit_1.weapon is not None and self.unit_1.terrain is not None and self.unit_2.weapon is not None and self.unit_2.terrain is not None:
                self.battle_button.config(command=self.start_unit_battle, state='normal')

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
        
    def start_unit_battle(self):
        battle = Battle(self.unit_1, self.unit_2, self.battle_window)
        battle.start_battle()
        
