from flask import Flask, jsonify, request
from ssl import SSLContext, PROTOCOL_TLSv1_2, CERT_NONE, OP_NO_SSLv2, OP_NO_SSLv3
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import datetime
import logging
from pathlib import Path

app = Flask(__name__)

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_cert_paths():
    """Retorna os caminhos dos certificados."""
    cert_dir = Path("certificates")
    cert_path = cert_dir / "certificate.crt"
    key_path = cert_dir / "private.key"
    
    if not cert_path.exists() or not key_path.exists():
        raise FileNotFoundError(
            "Certificados SSL não encontrados. Certifique-se de que os arquivos "
            "certificate.crt e private.key estão na pasta 'certificates'"
        )
    
    return str(cert_path), str(key_path)

def get_cert_info():
    """Retorna informações sobre o certificado SSL."""
    with open('./certificates/certificate.crt', 'rb') as cert_file:
        cert_data = cert_file.read()
        cert = x509.load_pem_x509_certificate(cert_data, default_backend())
        
        return {
            "issuer": cert.issuer.rfc4514_string(),
            "subject": cert.subject.rfc4514_string(),
            "valid_from": cert.not_valid_before.isoformat(),
            "valid_until": cert.not_valid_after.isoformat(),
            "serial_number": cert.serial_number,
            "version": cert.version.name
        }

@app.route('/')
def secure_route():
    logger.info("Recebida requisição na rota principal")
    return jsonify({
        "status": "Secure Connection Established",
        "protocol": "TLS 1.2",
        "secure": True
    })

@app.route('/hello')
def hello():
    """Rota de exemplo que retorna uma mensagem simples."""
    logger.info("Recebida requisição na rota /hello")
    return jsonify({
        "message": "Hello from secure server!",
        "status": "success",
        "secure": True,
        "timestamp": datetime.datetime.now().isoformat()
    })

@app.before_request
def log_request_info():
    """Log de informações sobre cada requisição."""
    logger.info(f"Nova requisição: {request.method} {request.path}")
    logger.info(f"Headers: {dict(request.headers)}")

if __name__ == '__main__':
    try:
        # Configurar contexto SSL
        context = SSLContext(PROTOCOL_TLSv1_2)
        cert_path, key_path = get_cert_paths()
        context.load_cert_chain(cert_path, key_path)
        
        # Configurações de segurança
        context.verify_mode = CERT_NONE  # Em produção, use CERT_REQUIRED
        context.options |= OP_NO_SSLv2
        context.options |= OP_NO_SSLv3
        
        logger.info("Iniciando servidor HTTPS na porta 5555...")
        logger.info(f"Informações do certificado: {get_cert_info()}")
        
        app.run(
            ssl_context=context,
            host='0.0.0.0',
            port=5555,
            debug=True
        )
    except FileNotFoundError as e:
        logger.error(f"Erro ao iniciar servidor: {e}")
        logger.error("Certifique-se de que os certificados estão na pasta 'certificates'")
    except Exception as e:
        logger.error(f"Erro ao iniciar servidor: {e}")