from pokemon import Pokemon

class AVLNode:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.height = 1
        self.left = None
        self.right = None