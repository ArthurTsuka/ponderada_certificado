from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Ola esse é servidor sem o uso de https."

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Dados do backend!", "status": "success"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(
        host='172.20.10.9',
        port=5000, 
        debug=True
    )