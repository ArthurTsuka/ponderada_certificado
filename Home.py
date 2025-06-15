import streamlit as st
from utils.ssl_utils import get_certificate_info
from pathlib import Path

# Configuração da página
st.set_page_config(
    page_title="Demonstração SSL/TLS",
    page_icon="🔒",
    layout="wide"
)

st.title("🔒 Demonstração de Segurança SSL/TLS")

st.markdown("""
### Como funciona o SSL/TLS?

1. **Handshake TLS**
   - O cliente envia um "Client Hello"
   - O servidor responde com um "Server Hello" e seu certificado
   - Ambos concordam com os parâmetros de criptografia

2. **Verificação do Certificado**
   - O certificado do servidor é verificado
   - A identidade do servidor é confirmada

3. **Estabelecimento da Conexão Segura**
   - Uma chave de sessão é gerada
   - Toda comunicação subsequente é criptografada
""")

# Mostrar informações do certificado
st.subheader("📜 Informações do Certificado")
cert_path = Path(__file__).parent / 'certificates' / 'certificate.crt'
cert_info = get_certificate_info(cert_path)
if cert_info:
    st.json(cert_info)
else:
    st.error("Não foi possível ler o certificado. Certifique-se de que os certificados foram gerados corretamente.") 