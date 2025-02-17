# Dictionaries to use for testing. Once basics are sorted, import from CSV?

units = {"eirika":  {
                    "name": "Eirika",
                    "level": 1,
                    "promoted": False,
                    "job": "Lord",
                    "available_jobs": ["great lord(f)"],
                    "hp": 0,
                    "str": 0,
                    "skl": 0,
                    "spd": 0,
                    "lck": 5,
                    "def": 0,
                    "res": 0,
                    "con": 0,
                    "hp_grow": 70,
                    "str_grow": 40,
                    "skl_grow": 60,
                    "spd_grow": 60,
                    "lck_grow": 60,
                    "def_grow": 30,
                    "res_grow": 30,
                    },
        
        "seth":     {
                    "name": "Seth",
                    "level": 1,
                    "promoted": True,
                    "job": "Paladin",
                    "available_jobs": None,
                    "hp": 28,
                    "str": 13,
                    "skl": 12,
                    "spd": 11,
                    "lck": 13,
                    "def": 9,
                    "res": 7,
                    "con": 9,
                    "hp_grow": 90,
                    "str_grow": 50,
                    "skl_grow": 45,
                    "spd_grow": 45,
                    "lck_grow": 25,
                    "def_grow": 40,
                    "res_grow": 30,
                    }
        }

weapons = {"rapier": 
                     {
                     "name": "Rapier",
                     "mt": 7,
                     "hit": 95,
                     "crt": 10,
                     "wt": 5,
                     "type": "sword",
                     "effective_against": "cavalry, armour",
                     "magic": False,
                     "invert_triangle": False
                     },
        
        "silver_lance": {
                      "name": "Silver Lance",
                      "mt": 14,
                      "hit": 75,
                      "crt": 0,
                      "wt": 10,
                      "type": "lance",
                      "effective_against": None,
                      "magic": False,
                      "invert_triangle": True
                     }
            }

jobs = {"lord(f)": {
                   "name": "Lord",
                   "hp": 16,
                   "str": 4,
                   "skl": 8,
                   "spd": 9,
                   "def": 3,
                   "res": 1,
                   "con": 5,
                   "hp_cap": 60,
                   "str_cap": 20,
                   "skl_cap": 20,
                   "spd_cap": 20,
                   "lck_cap": 30,
                   "def_cap": 20,
                   "res_cap": 20,
                   "weapon_types": "sword",
                   "class_skill": None,
                   "type_1": None,
                   "type_2": None
                   },
                
        "paladin(m)": {
                      "name": "Paladin",
                      "hp": 2,
                      "str": 1,
                      "skl": 1,
                      "spd": 1,
                      "def": 2,
                      "res": 1,
                      "con": 2,
                      "hp_cap": 60,
                      "str_cap": 25,
                      "skl_cap": 26,
                      "spd_cap": 24,
                      "lck_cap": 30,
                      "def_cap": 25,
                      "res_cap": 25,
                      "weapon_types": "sword, lance",
                      "class_skill": None,
                      "type_1": "cavalry",
                      "type_2": None
                      },
        
        "great lord(f)": {
                        "name": "Great Lord",
                        "hp": 4,
                        "str": 2,
                        "skl": 2,
                        "spd": 1,
                        "def": 3,
                        "res": 5,
                        "con": 2,
                        "hp_cap": 60,
                        "str_cap": 24,
                        "skl_cap": 29,
                        "spd_cap": 30,
                        "lck_cap": 30,
                        "def_cap": 22,
                        "res_cap": 25,
                        "weapon_types": "sword",
                        "class_skill": None,
                        "type_1": "Cavalry",
                        "type_2": None
                        }
        }

terrain = {"plain": {
                    "name": "Plain",
                    "avoid": 0,
                    "def_bonus": 0
                    },

           "forest": {
                     "name": "Forest",
                     "avoid": 20,
                     "def_bonus": 1
                     }
        }