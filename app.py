from flask import Flask, jsonify,request
import os,base64

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    image_name = request_data['name']
    image = request_data['image']

    ls_f2 = bytes(image, encoding="utf8")
    imgdata = base64.b64decode(ls_f2)
    file = open(r'E:\新建文件夹 (2)\flask\1001.jpg', 'wb')
    file.write(imgdata)
    file.close()

    return "s"


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


@app.route('/store')
def get_stores():
    return jsonify({"stores": stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_date = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_date['name'],
                'price': request_date['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'item': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=5000)
