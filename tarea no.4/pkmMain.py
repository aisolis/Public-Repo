import csv
import os
from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify
from io import StringIO
from pokemon import Pokemon
from avlTree import AVLTree

app = Flask(__name__)

def read_pokemon_csv(file_stream):
    pokemons = []
    csv_reader = csv.DictReader(file_stream, delimiter=';')
    for row in csv_reader:
        # Crea un diccionario para cada Pokémon con toda su información
        pokemon_info = {
            'Nombre': row['Nombre'],
            'Nivel': int(row['Nivel']),
            'Tipo': row['Tipo']
        }
        pokemons.append(pokemon_info)
    return pokemons

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No se encontró parte del archivo'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No se seleccionó archivo'}), 400
    if file:
        file_stream = StringIO(file.read().decode('utf-8'))
        pokemons = read_pokemon_csv(file_stream)

        # Guarda los datos de Pokémon en la variable de clase
        AVLTree.insert_pokemon_data(pokemons)
        
        return jsonify(pokemons)


@app.route('/search', methods=['GET'])
def search_pokemon():
    name_query = request.args.get('name', None)

    if not name_query:
        return jsonify({'error': 'Debes proporcionar un nombre de Pokémon'}), 400

    # Busca el Pokémon por nombre en los datos almacenados
    result = AVLTree.search_pokemon_by_name(name_query)
    
    if result:
        return jsonify(result)
    else:
        return jsonify({'mensaje': 'Pokémon no encontrado'}), 404

@app.route('/add_pokemon', methods=['POST'])
def add_pokemon():
    # Asegurarse de que la solicitud contenga un JSON
    if not request.is_json:
        return jsonify({"error": "La solicitud debe ser JSON"}), 400
    
    data = request.get_json()

    # Extraer datos del Pokémon del JSON
    try:
        nivel = data['Nivel']
        nombre = data['Nombre']
        tipo = data['Tipo']
    except KeyError as e:
        # Si falta algún campo requerido, devuelve un error
        return jsonify({'error': f'No se han proporcionado todos los valores: {e}'}), 400
    
    # Crear un diccionario con los datos del Pokémon
    new_pokemon = {
        'Nombre': nombre,
        'Nivel': nivel,
        'Tipo': tipo
    }

    # Insertar el nuevo Pokémon en la estructura de datos
    AVLTree.pokemons_data.append(new_pokemon)
    
    # Devolver una respuesta indicando éxito
    return jsonify({"mensaje": "Pokémon agregado con éxito", "pokemon": new_pokemon}), 201


@app.route('/pokemons', methods=['GET'])
def get_pokemons():
    # Devolver todos los Pokémon almacenados en AVLTree.pokemons_data
    return jsonify(AVLTree.pokemons_data)


if __name__ == '__main__':
    app.run(debug=True)