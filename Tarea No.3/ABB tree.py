import os
import graphviz

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class SearchResult:
    def __init__(self, value, node_type):
        self.value = value
        self.node_type = node_type

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        try:
            value = int(value)
            if not self.root:
                self.root = TreeNode(value)
            else:
                self._insert_recursively(self.root, value)
                self.visualize_tree()
        except ValueError:
            print("Error: Ingrese un número entero válido")

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def visualize_tree(self):
        dot = graphviz.Digraph()
        self._visualize_tree_recursive(self.root, dot)
        dot.render('binary_tree', format='png', cleanup=True)

    def _visualize_tree_recursive(self, node, dot):
        if node:
            dot.node(str(node.value))
            if node.left:
                dot.edge(str(node.value), str(node.left.value))
                self._visualize_tree_recursive(node.left, dot)
            if node.right:
                dot.edge(str(node.value), str(node.right.value))
                self._visualize_tree_recursive(node.right, dot)

    def in_order_traversal(self):
        self._in_order_traversal_recursive(self.root)
        print()

    def _in_order_traversal_recursive(self, node):
        if node:
            self._in_order_traversal_recursive(node.left)
            print(node.value, end=" ")
            self._in_order_traversal_recursive(node.right)

    # Nuevo Método: Recorrido post-orden
    def post_order_traversal(self):
        self._post_order_traversal_recursive(self.root)
        print()

    def _post_order_traversal_recursive(self, node):
        if node:
            self._post_order_traversal_recursive(node.left)
            self._post_order_traversal_recursive(node.right)
            print(node.value, end=" ")

    # Nuevo Método: Recorrido pre-orden
    def pre_order_traversal(self):
        self._pre_order_traversal_recursive(self.root)
        print()

    def _pre_order_traversal_recursive(self, node):
        if node:
            print(node.value, end=" ")
            self._pre_order_traversal_recursive(node.left)
            self._pre_order_traversal_recursive(node.right)

    def search(self, value):
        result = self._search_recursive(self.root, value)
        if result:
            return result
        else:
            return None

    def _search_recursive(self, node, value):
        if node is None:
            return None
        elif value == node.value:
            if node == self.root:
                return SearchResult(value, "RAIZ")
            elif node.left or node.right:
                if node.left and node.right:
                    return SearchResult(value, "CON_HIJOS")
                else:
                    return SearchResult(value, "HIJO")
            else:
                return SearchResult(value, "HOJA")
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
        
    def delete(self, value):
        if self.search(value):
            self.root = self._delete_recursive(self.root, value)
            self.visualize_tree()
            print(f"Nodo con valor {value} eliminado correctamente.")
        else:
            print(f"No se Encontro el nodo con valor {value} en el árbol.")

    def _delete_recursive(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_min(node.right)
                node.value = successor.value
                node.right = self._delete_recursive(node.right, successor.value)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def load_from_file(tree):
        filename = input ("Ingrese la Ruta del Archivo: ")
        try:
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line.isdigit():
                        value = int(line)
                        tree.insert(value)
                    else:
                        print(f"Datos cargados correctamente desde el archivo.")
        except FileNotFoundError:
            print("El archivo especificado no se encuentra.")
        except ValueError:
            print("Error al convertir los datos del archivo a números enteros.")

def main():
    tree = BinarySearchTree()
    while True:
        os.system('clear')
        print("\n----- MENU -----")
        print("1. Insertar un valor")
        print("2. Mostrar Recorrido in-orden")
        print("3. Mostrar Recorrido post-orden")
        print("4. Mostrar Recorrido pre-orden")
        print("5. Buscar un valor")
        print("6. Eliminar un valor")
        print("7. Cargar archivo con datos binario")
        print("8. Salir del programa")

        choice = input("Ingrese su opción: ")

        if choice == '1':
            value_input = input("Ingrese el valor que desea insertar: ")
            try:
                value = int(value_input)
                tree.insert(value)
            except ValueError:
                print("Error: Ingrese un número entero válido")
            input("Presione Enter para continuar")
            tree.visualize_tree()
        elif choice == '2':
            print("Recorrido in-orden:")
            tree.in_order_traversal()
            input("Presione Enter para continuar")
        elif choice == '3':
            print("Recorrido post-orden:")
            tree.post_order_traversal()
            input("Presione Enter para continuar")
        elif choice == '4':
            print("Recorrido pre-orden:")
            tree.pre_order_traversal()
            input("Presione Enter para continuar")
        elif choice == '5':
            value = int(input("Ingrese el valor que desea buscar: "))
            result = tree.search(value)
            if result:
                print(f"El valor {result.value} se encuentra en un nodo de tipo {result.node_type}.")
            else:
                print(f"El valor {value} no se encuentra en el árbol.")
            tree.pre_order_traversal()
            input("Presione Enter para continuar")
        elif choice == '6':
            value = int(input("Ingrese el valor que desea eliminar: "))
            tree.delete(value)
            input("Presione Enter para continuar")
        elif choice == '7':
            filename = input("Ingrese el nombre del archivo: ")
            tree.load_from_file()
            input("Presione Enter para continuar")
        elif choice == '8':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
