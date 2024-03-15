# Correr programa
Usa el comando 
```cmd
py ABB tree.py
```

## participantes
|  Nombre | Carnet | Participacion  |
| :------------: | :------------: | :------------: |
| Cristian Sebastian Rodas | 9490-22-523| 100%   |
| Joshua Ivan Andree Mendez Vasquez | 9490-22-4032 | 100%   |
| Alder Isaac Solis De Leon | 9490-22-227 |  100%  |
| Abner Salvador Cancinos | 9490-22-2101 |  100%  |

# Documentación de Funciones Recursivas

### Funciones del Programa

#### Clase `TreeNode`

- `__init__(self, value)`: Constructor de la clase TreeNode que inicializa un nodo con un valor dado, y sin hijos izquierdo y derecho.

#### Clase `SearchResult`

- `__init__(self, value, node_type)`: Constructor de la clase SearchResult que guarda el valor encontrado y el tipo de nodo en el que se encuentra.

#### Clase `BinarySearchTree`

- `__init__(self)`: Constructor de la clase BinarySearchTree que inicializa un árbol binario de búsqueda vacío.

- `insert(self, value)`: Inserta un valor en el árbol.

- `_insert_recursively(self, node, value)`: Método privado para insertar recursivamente un valor en el árbol.

- `visualize_tree(self)`: Visualiza el árbol utilizando la biblioteca Graphviz.

- `_visualize_tree_recursive(self, node, dot)`: Método privado para visualizar recursivamente el árbol.

- `in_order_traversal(self)`: Realiza un recorrido en orden del árbol e imprime los valores.

- `_in_order_traversal_recursive(self, node)`: Método privado para realizar el recorrido en orden recursivamente.

- `post_order_traversal(self)`: Realiza un recorrido post-orden del árbol e imprime los valores.

- `_post_order_traversal_recursive(self, node)`: Método privado para realizar el recorrido post-orden recursivamente.

- `pre_order_traversal(self)`: Realiza un recorrido pre-orden del árbol e imprime los valores.

- `_pre_order_traversal_recursive(self, node)`: Método privado para realizar el recorrido pre-orden recursivamente.

- `search(self, value)`: Busca un valor en el árbol y devuelve el resultado.

- `_search_recursive(self, node, value)`: Método privado para buscar recursivamente un valor en el árbol.

- `delete(self, value)`: Elimina un valor del árbol.

- `_delete_recursive(self, node, value)`: Método privado para eliminar recursivamente un valor del árbol.

- `_find_min(self, node)`: Método privado para encontrar el valor mínimo en un subárbol.

- `load_from_file(tree)`: Método de clase para cargar datos desde un archivo.

#### Función `main()`

- Función principal que ejecuta el menú interactivo y gestiona las operaciones del árbol binario de búsqueda.
