from dicts import terrain

class Terrain:
    def __init__(self, terrain):
        self.name = terrain["name"]
        self.avoid = int(terrain["avoid"])
        self.def_bonus = int(terrain["def_bonus"])