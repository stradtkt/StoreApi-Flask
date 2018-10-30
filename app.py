from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [
    {
        'name': 'Store Name',
        'items': [
            {
                'name': 'item name',
                'price': 15.99
            }
        ]
    }
]


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

@app.route('/store')
def gets_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

@app.route('/store/<string:name>/item', methods=['GET'])
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'item in store not found'})

app.run(port=5000, debug=True)