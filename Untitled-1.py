class Area:
    def __init__(self, name, has_bonfire=False, requires_light=False, has_light_sources=False, has_shortcuts=False):
        self.name = name
        self.has_bonfire = has_bonfire
        self.requires_light = requires_light
        self.has_light_sources = has_light_sources
        self.has_shortcuts = has_shortcuts
        self.connections = []

    def connect(self, other_area):
        self.connections.append(other_area)

class Level:
    def __init__(self):
        self.areas = {
            "starting_area": Area("Starting Area", has_bonfire=True),
            "dark_corridor": Area("Dark Corridor", requires_light=True),
            "chamber_of_light": Area("Chamber of Light", has_light_sources=True),
            "looping_path": Area("Looping Path", has_shortcuts=True),
        }
        self.connect_areas()

    def connect_areas(self):
        self.areas["starting_area"].connect(self.areas["dark_corridor"])
        self.areas["dark_corridor"].connect(self.areas["chamber_of_light"])
        self.areas["chamber_of_light"].connect(self.areas["looping_path"])
        self.areas["looping_path"].connect(self.areas["starting_area"])

# Example of creating a Level instance
level = Level()
