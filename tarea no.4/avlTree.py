from pokemon import Pokemon
from avlNode import AVLNode

class AVLTree:
    pokemons_data = []  # Lista para almacenar los datos de los Pokémon

    @classmethod
    def insert_pokemon_data(cls, pokemons):
        cls.pokemons_data = pokemons

    @classmethod
    def search_pokemon_by_name(cls, name):
        result = [pokemon for pokemon in cls.pokemons_data if pokemon['Nombre'].lower() == name.lower()]
        return result

    def insert(self, root, pokemon):
        if not root:
            return AVLNode(pokemon)
        elif pokemon.name < root.pokemon.name:
            root.left = self.insert(root.left, pokemon)
        else:
            root.right = self.insert(root.right, pokemon)

        root.height = 1 + max(self._get_height(root.left),
                              self._get_height(root.right))

        balance = self._get_balance(root)

        # Left Left
        if balance > 1 and pokemon.name < root.left.pokemon.name:
            return self._rotate_right(root)
        # Right Right
        if balance < -1 and pokemon.name > root.right.pokemon.name:
            return self._rotate_left(root)
        # Left Right
        if balance > 1 and pokemon.name > root.left.pokemon.name:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)
        # Right Left
        if balance < -1 and pokemon.name < root.right.pokemon.name:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def search(self, root, name):
        if not root or root.pokemon.name == name:
            return root
        elif name < root.pokemon.name:
            return self.search(root.left, name)
        else:
            return self.search(root.right, name)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))
        return y

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left),
                           self._get_height(x.right))
        return x

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)