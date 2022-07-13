from flask import Flask, jsonify, request

app = Flask(__name__)

mensajes ={}
@app.route('/allmensajes')
def get_products():
    return jsonify({'mensajes': mensajes})


@app.route('/mensaje/<string:x>',methods=['GET'])
def get_product(x):
	if x in mensajes:
		return jsonify(mensajes[x])
	else:
         return jsonify([{'status': 'No hay mensaje'}])

@app.route('/mensaje', methods=['POST'])
def sent_product():
    try:
            mensaje: request.json["mensaje"]
            topic = request.json['topic']
            mensajes[topic].append({'topic': topic,"mensaje":mensaje})
            return jsonify({"status":"ok"})
    except:
            return jsonify({"status":"fail"})


if __name__ == '__main__':
    app.run(debug=True, port=4000)