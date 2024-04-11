class Pokemon:
    def __init__(self, name, level, ptype):
        self.name = name
        self.level = level
        self.ptype = ptype

    def __str__(self):
        return f"{self.name} (Nivel: {self.level}, Tipo: {self.ptype})"