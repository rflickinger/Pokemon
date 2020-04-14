class Pokemon:
    def __init__(self, name, level, type, max_health, current_health, ko):
        self.name = name                     #str name
        self.level = level                   #int level
        self.pType = type                    #str type ie: water, fire, etc
        self.max_health = max_health         #int maximum health
        self.current_health = current_health #int current health
        self.ko = ko                         #bool is knocked out


