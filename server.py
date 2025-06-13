from flask import Flask, jsonify
from ssl import SSLContext, PROTOCOL_TLSv1_2
app = Flask(__name__)
@app.route('/')
def secure_route():
    return "Secure Connection Established"

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello from secure server!", "status": "success"})

if __name__ == '__main__':
    context = SSLContext(PROTOCOL_TLSv1_2)
    context.load_cert_chain('certificate.crt', 'private.key')
    app.run(ssl_context=context, host='0.0.0.0', port=5555)