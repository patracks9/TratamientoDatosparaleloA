# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Bienvenido a la API de Microservicio Base - Tratamiento de Datos Paralelo A'})

@app.route('/api/sumar', methods=['POST'])
def sumar():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    if a is None or b is None:
        return jsonify({'error': 'Faltan datos para sumar'}), 400
    return jsonify({'resultado': a + b })

@app.route('/api/inf')
def info():
    return jsonify({
        'nombre': 'Microservicio Base Tratamiento de Datos Paralelo A',
        'version': '1.0.0',
        'descripcion': 'Este microservicio suma y da info',
        'autor': 'Bryan Patricio Silva'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)