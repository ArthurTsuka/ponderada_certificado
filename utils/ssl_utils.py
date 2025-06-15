import requests
import logging
import OpenSSL.crypto
from pathlib import Path
import os

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_certificate_info(cert_path):
    """Extrai informações do certificado SSL."""
    try:
        with open(cert_path, 'rb') as cert_file:
            cert_data = cert_file.read()
            cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert_data)
            
            return {
                "subject": dict(cert.get_subject().get_components()),
                "issuer": dict(cert.get_issuer().get_components()),
                "serial_number": cert.get_serial_number(),
                "not_before": cert.get_notBefore().decode(),
                "not_after": cert.get_notAfter().decode(),
                "has_expired": cert.has_expired()
            }
    except Exception as e:
        logger.error(f"Erro ao ler certificado: {e}")
        return None

def get_cert_paths():
    """Retorna os caminhos dos certificados."""
    # Tenta encontrar os certificados em diferentes locais possíveis
    possible_paths = [
        # Caminho relativo ao diretório atual
        Path("certificates"),
        # Caminho relativo ao diretório do script
        Path(__file__).parent.parent / "certificates",
        # Caminho absoluto (se fornecido via variável de ambiente)
        Path(os.getenv("SSL_CERT_DIR", "certificates"))
    ]
    
    for base_path in possible_paths:
        cert_path = base_path / "certificate.crt"
        key_path = base_path / "private.key"
        if cert_path.exists() and key_path.exists():
            return str(cert_path), str(key_path)
            
    raise FileNotFoundError("Certificados SSL não encontrados. Certifique-se de que os arquivos certificate.crt e private.key estão na pasta 'certificates'.")

def get(endpoint='/'):
    """Faz uma requisição HTTPS para o servidor."""
    try:
        url = f"https://localhost:5555{endpoint}"
        cert_path, key_path = get_cert_paths()
        
        response = requests.get(
            url=url,
            cert=(cert_path, key_path),
            verify=False,  # Em produção, isso deve ser True
            timeout=10
        )
        return response.json()
    except FileNotFoundError as e:
        logger.error(f"Erro com certificados: {e}")
        return {"error": str(e)}
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro na requisição: {e}")
        return {"error": str(e)} 