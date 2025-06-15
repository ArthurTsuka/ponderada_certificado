from flask import Flask, request, jsonify
import ssl
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def secure_route():
    return f"Secure Connection Established via HTTPS!\nTime: {datetime.now().isoformat()}"

@app.route('/api/data', methods=['POST'])
def handle_data():
    data = request.get_json()
    print('HTTPS Server received:', data)
    
    return jsonify({
        'received': data,
        'encrypted': True,
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    # Criar contexto SSL
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('certificate.crt', 'private.key')
    
    print("Starting Flask HTTPS Server...")
    print("Certificate: certificate.crt")
    print("Private Key: private.key")
    print("Server running on https://localhost:8444")
    
    # Usar porta 8444 para Flask para não conflitar com o Node.js
    app.run(host='localhost', port=8444, ssl_context=context, debug=True) 