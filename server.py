from flask import Flask
from ssl import SSLContext, PROTOCOL_TLSv1_2
app = Flask(__name__)
@app.route('/')
def secure_route():
    return "Secure Connection Established"

if __name__ == '__main__':
    context = SSLContext(PROTOCOL_TLSv1_2)
    context.load_cert_chain('certificate.crt', 'private.key')
    app.run(ssl_context=context, port=443)