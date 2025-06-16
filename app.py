from flask import Flask, jsonify, request # Importe 'request' se for usar métodos HTTP diferentes de GET
import os # Para lidar com caminhos de arquivos de forma robusta
import ssl

app = Flask(__name__)


@app.route('/')
def home():

    return "Ola esse servidor esta seguro."

@app.route('/api/data', methods=['GET'])
def get_data():

    data = {"message": "Dados seguros do backend!", "status": "success"}
    return jsonify(data)

if __name__ == '__main__':
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server-cert.pem", keyfile="server.key")
    
    app.run(
        host='172.20.10.9',
        port=4443,
        ssl_context=context,
        debug=True
    )