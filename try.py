from flask import Flask, jsonify, request

app = Flask(__name__)

mensajes ={}

# Testing Route
#@app.route('/ping', methods=['GET'])
#def ping():
#    return jsonify({'response': 'pong!'})

# Get Data Routes
@app.route('/allmensajes')
def getProducts():
    # return jsonify(products)
    return jsonify({'mensajes': mensajes})


@app.route('/mensaje/<string:x>',methods=['GET'])
def getProduct(x):
	if x in mensajes:
		return jsonify(mensajes[x])
	else:
         return jsonify([{'status': 'No hay mensaje'}])

# Create Data Routes
@app.route('/mensaje', methods=['POST'])
def sentProduct():
    try:
            mensaje: request.json["mensaje"]
            topic = request.json['topic']
            mensajes[topic].append({'topic': topic,"mensaje":mensaje})
            return jsonify({"status":"ok"})
    except:
            return jsonify({"status":"fail"})

# DELETE Data Route
#@app.route('/products/<string:product_name>', methods=['DELETE'])
#def deleteProduct(product_name):
#    productsFound = [product for product in products if product['name'] == product_name]
#    if len(productsFound) > 0:
#        products.remove(productsFound[0])
#        return jsonify({
#            'message': 'Product Deleted',
#            'products': products
#        })


if __name__ == '__main__':
    app.run(debug=True, port=4000)