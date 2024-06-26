from flask import Flask, jsonify, request
from flask_cors import CORS
import postgres
from utils import check_keys

app = Flask(__name__)

CORS(app)




# listagem das lojas
@app.route('/stores', methods=['GET'])
def get_stores():
    response, code = postgres.get_data('fast_food_stores')
    return jsonify(response), code


# visualização de uma loja
@app.route('/store/<int:id>', methods=['GET'])
def get_store(id):
    response, code = postgres.get_data('fast_food_stores', id)
    return jsonify(response), code

# criação de uma loja
@app.route('/store', methods=['POST'])
def create_store():
    data = request.json
    check = check_keys(data, "all")
    if check:
        return jsonify({'error': check}), 400
    response, code = postgres.insert_data('fast_food_stores', data)
    return jsonify({'message': response}), code

# atualização de uma loja
@app.route('/store/<int:id>', methods=['PUT'])
def update_store(id):
    data = request.json
    fields = ['establishedyear', 'location', 'owner', 'numberofemployees']
    if not data:
        return jsonify({'error': 'No data provided', 'fields': fields}), 400
    if "storeid" in data.keys():
        return jsonify({'error': 'storeid cannot be updated', "fields": fields }), 400
    response, code = postgres.update_data('fast_food_stores', id, data)
    return jsonify(response), code

# remoção de uma loja
@app.route('/store/<int:id>', methods=['DELETE'])
def delete_store(id):
    response, code = postgres.delete_data('fast_food_stores', id)
    return jsonify({'message': response}), code



if __name__ == '__main__':
    app.run(debug=True)
