pip install Flask
from flask import Flask, request, jsonify

app = Flask(_name_)

# Lista de tareas
tasks = []

# Ruta para obtener todas las tareas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Ruta para agregar una nueva tarea
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')
    tasks.append(task)
    return jsonify({'message': 'Tarea agregada correctamente'})

# Ruta para actualizar una tarea por su índice
@app.route('/tasks/<int:index>', methods=['PUT'])
def update_task(index):
    data = request.get_json()
    if 0 <= index < len(tasks):
        tasks[index] = data.get('task')
        return jsonify({'message': 'Tarea actualizada correctamente'})
    else:
        return jsonify({'error': 'Índice de tarea fuera de rango'})

# Ruta para eliminar una tarea por su índice
@app.route('/tasks/<int:index>', methods=['DELETE'])
def delete_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
        return jsonify({'message': 'Tarea eliminada correctamente'})
    else:
        return jsonify({'error': 'Índice de tarea fuera de rango'})

if _name_ == '_main_':
    app.run(debug=True)
python app.py