# Instalacion para uso

## windows
Accede a la página oficial de Graphviz (https://graphviz.org/download/) y selecciona la versión compatible con tu sistema operativo (Windows). Descarga el archivo de instalación.

**Ejecución:** 
Inicia el archivo descargado y sigue las instrucciones del asistente de instalación. Acepta los términos y condiciones y selecciona la ruta de instalación.

**Configuración de variables:**

Busca "Variable de entorno" en el menú Inicio y abre el panel de configuración.
Selecciona "Editar las variables de entorno del sistema".
En la ventana emergente, haz clic en "Nueva" dentro del apartado "Variables de entorno".

Introduce "GRAPHVIZ_HOME" como nombre de la variable y la ruta de la carpeta donde se instaló Graphviz como valor.

Acepta los cambios y reinicia tu equipo.

**Verificación:** 
Abre una terminal (cmd) y escribe el comando "dot -V". Deberías obtener información sobre la versión de Graphviz instalada.

## Linux
**Actualización de paquetes:
** 
Abre una terminal y ejecuta el comando "sudo apt-get update" para actualizar la lista de paquetes disponibles.

**Instalación:**
Ejecuta el comando "sudo apt-get install graphviz" para instalar Graphviz y sus dependencias.

**Verificación:**
Escribe el comando "dot -V" en la terminal para verificar la instalación. Deberías obtener información sobre la versión de Graphviz instalada.

# Correr programa
Usa el comando 
```cmd
py linkedList.py
```

## participantes
|  Nombre | Carnet | Participacion  |
| :------------: | :------------: | :------------: |
| Cristian Sebastian Rodas | 9490-22-523| 100%   |
| Joshua Ivan Andree Mendez Vasquez | 9490-22-4032 | 100%   |
| Alder Isaac Solis De Leon | 9490-22-227 |  100%  |
| Abner Salvador Cancinos | 9490-22-2101 |  100%  |


### Clase Nodo
Encapsula los datos y la estructura de un nodo para una lista enlazada.

**Descripción:
**
Esta clase define un nodo para una lista enlazada. Un nodo es un elemento individual de la lista que contiene datos y punteros a los nodos anterior y siguiente.

**Atributos**:

- datos: El contenido del nodo. Puede ser cualquier tipo de dato, como un número, una cadena o un objeto.
- Nombre: Nombre del individuo asociado al nodo.
- apellido: Apellido del individuo asociado al nodo.
- siguiente: Un puntero al siguiente nodo en la lista.
- anterior: Un puntero al nodo anterior en la lista.

**Métodos:**

__init__(self, datos=None, Nombre=None, apellido=None, siguiente=None, anterior=None): Inicializa un nuevo nodo.

Ejemplo de uso:

```Python
nodo1 = Nodo("Juan Pérez", "Pérez", "Gómez", None, None)
nodo2 = Nodo("María Martínez", "Martínez", "López", nodo1, None)
```
**Ahora nodo1.siguiente apunta a nodo2**

```
print(nodo1.datos)  # Imprime "Juan Pérez"
print(nodo2.anterior.datos)  # Imprime "Juan Pérez"
```

### Clase Lista

**Descripción:**

Esta clase define una lista doblemente enlazada. Una lista doblemente enlazada es una estructura de datos que almacena datos en una secuencia de nodos. Cada nodo contiene el dato en sí mismo, un puntero al siguiente nodo en la lista y un puntero al nodo anterior en la lista.

**Atributos:**

- cabeza: Un puntero al primer nodo de la lista.
- cola: Un puntero al último nodo de la lista.

**Métodos:**

- __init__(self): Inicializa una nueva lista vacía.
- insertarInicio(self, datos, nombre, apellido): Agrega un nuevo nodo al inicio de la lista.
- insertarFinal(self, datos, nombre, apellido): Agrega un nuevo nodo al final de la lista.
- mostrarDatos(self): Imprime el contenido de la lista.
- eliminar(self, dato): Elimina un nodo de la lista por su contenido.
- graficar(self): Genera un diagrama de la lista en formato PNG.

Ejemplo de uso:

```Python
lista = Lista()

lista.insertarInicio("Ana García", "García", "López")
lista.insertarInicio("Pedro Martínez", "Martínez", "Gómez")
lista.insertarFinal("Juan Pérez", "Pérez", "Fernández")

lista.mostrarDatos()

lista.eliminar("Pedro Martínez")

lista.mostrarDatos()

lista.graficar()
```
