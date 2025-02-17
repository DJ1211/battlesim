from dicts import terrain

class Terrain:
    def __init__(self, terrain):
        self.name = terrain["name"]
        self.avoid = terrain["avoid"]
        self.def_bonus = terrain["def_bonus"]