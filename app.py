from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

# Cliente de DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Cambia a tu región
table = dynamodb.Table('TuNombreDeTabla')  # Cambia por tu tabla

# POST -> insertar item
@app.route('/item', methods=['POST'])
def create_item():
    data = request.get_json()
    table.put_item(Item=data)
    return jsonify({"message": "Item insertado con éxito", "item": data}), 201

# GET -> obtener item por ID
@app.route('/item/<string:id>', methods=['GET'])
def get_item(id):
    response = table.get_item(Key={'id': id})  # Ajusta si tu PK tiene otro nombre
    item = response.get('Item')
    if item:
        return jsonify(item), 200
    else:
        return jsonify({"error": "Item no encontrado"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
