
import pandas as pd
from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# --- Carga de Datos ---
# Construir la ruta absoluta al archivo CSV
try:
    CWD = os.getcwd()
    CSV_PATH = os.path.join(CWD, 'data.csv')
    df = pd.read_csv(CSV_PATH)
    # Convertir a mayúsculas las columnas que usaremos para buscar, para facilitar las coincidencias
    df['municipio_usuaria'] = df['municipio_usuaria'].str.upper()
    df['servicio'] = df['servicio'].str.upper()
    df['tematica_1'] = df['tematica_1'].str.upper()
except FileNotFoundError:
    print(f"Error: No se encontró el archivo {CSV_PATH}. Asegúrate de que 'data.csv' existe.")
    df = pd.DataFrame() # Crear un DataFrame vacío si no se encuentra el archivo

# --- Lógica de Q&A ---
def answer_question(question):
    """
    Analiza una pregunta para extraer entidades y traducirla a una consulta de pandas.
    Es flexible con el orden de las palabras y puede manejar múltiples condiciones.
    """
    question_upper = question.upper()
    # Limpiar la pregunta de signos de puntuación comunes
    cleaned_question = question_upper.replace('?', '').replace('¿', '').replace('.', '').replace(',', '')
    words = cleaned_question.split()

    # Extraer listas de entidades únicas del DataFrame
    municipios = df['municipio_usuaria'].unique()
    servicios = df['servicio'].unique()
    tematicas = df['tematica_1'].unique()

    # Diccionario para guardar los filtros encontrados
    filters = {}

    # Identificar entidades en la pregunta
    for word in words:
        if word in municipios:
            filters['municipio_usuaria'] = word
        if word in servicios:
            filters['servicio'] = word
        if word in tematicas:
            filters['tematica_1'] = word

    # Si no se encuentra ninguna entidad, devolver un mensaje por defecto
    if not filters:
        return "No pude identificar un municipio, servicio o temática en tu pregunta. Por favor, intenta de nuevo."

    # Construir la consulta de Pandas dinámicamente
    query_df = df
    response_parts = []
    
    # Aplicar todos los filtros encontrados
    for column, value in filters.items():
        query_df = query_df[query_df[column] == value]
        
        # Formatear el nombre de la columna para la respuesta
        column_name_for_response = column.replace('_usuaria', '').replace('_', ' ')
        response_parts.append(f"para {column_name_for_response} '{value.title()}'")

    count = query_df.shape[0]

    # Construir la respuesta final
    if 'CUANTOS' in words or 'CUANTAS' in words:
        if response_parts:
            return f"Hay {count} registros que cumplen con las condiciones: " + " y ".join(response_parts) + "."
        else:
            # Esto no debería ocurrir si se encontraron filtros, pero es un fallback
            return f"Se encontraron {count} registros."
    else:
        # Si no se pregunta "cuántos", se puede adaptar para devolver una lista o resumen
        if count > 0:
            # Por ahora, solo devolvemos el conteo, pero se podría expandir
            return f"Encontré {count} registros que coinciden con tu búsqueda: " + " y ".join(response_parts) + "."
        else:
            return "No se encontraron registros que coincidan con tu búsqueda."

# --- Rutas de la API ---
@app.route('/')
def index():
    """Sirve la página principal."""
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    """Recibe una pregunta, la procesa y devuelve una respuesta."""
    if df.empty:
        return jsonify({'answer': 'Error: La base de datos (data.csv) no se ha cargado correctamente.'}), 500

    data = request.get_json()
    question = data.get('question', '')

    if not question:
        return jsonify({'answer': 'No se recibió ninguna pregunta.'}), 400

    response = answer_question(question)
    return jsonify({'answer': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
