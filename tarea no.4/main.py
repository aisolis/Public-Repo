from flask import Flask, request, jsonify
import csv
from avlTree import AVLTree

app = Flask(__name__)

# Instancia del árbol AVL
avl_tree = AVLTree()

@app.route('/upload', methods=['POST'])
def upload_file():
    # Verificar si se ha enviado un archivo
    if 'file' not in request.files:
        return jsonify({'error': 'No se ha enviado ningún archivo'}), 400
    
    file = request.files['file']

    # Verificar si el archivo tiene un nombre y si es un archivo CSV
    if file.filename == '':
        return jsonify({'error': 'No se ha proporcionado un nombre de archivo'}), 400
    if not file.filename.endswith('.csv'):
        return jsonify({'error': 'El archivo proporcionado no es un archivo CSV'}), 400

    # Leer el archivo CSV y agregar los datos al árbol AVL
    try:
        csv_data = csv.reader(file)
        for row in csv_data:
            key = int(row[0])  # Supongamos que la primera columna es la clave
            data = row[1]  # Supongamos que la segunda columna es el dato
            avl_tree.insert(key, data)
        return jsonify({'message': 'Los datos se han cargado correctamente en el árbol AVL'}), 200
    except Exception as e:
        return jsonify({'error': 'Error al leer el archivo CSV'}), 500

@app.route('/search/<int:key>', methods=['GET'])
def search_data(key):
    result = avl_tree.search(key)
    if result:
        return jsonify({'data': result}), 200
    else:
        return jsonify({'error': 'No se encontraron datos para la clave especificada'}), 404

if __name__ == '__main__':
    app.run(debug=True)