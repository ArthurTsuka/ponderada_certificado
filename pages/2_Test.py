import streamlit as st
import requests
from utils.ssl_utils import get, get_cert_paths

st.title("🔒 Teste de Conexão Segura")

# Adicionar status do servidor
server_status = st.empty()
try:
    cert_path, key_path = get_cert_paths()
    response = requests.get(
        "https://localhost:5555/",
        cert=(cert_path, key_path),
        verify=False,
        timeout=2
    )
    server_status.success("✅ Servidor está online")
except FileNotFoundError as e:
    server_status.error(f"❌ Erro com certificados: {str(e)}")
except requests.exceptions.RequestException:
    server_status.error("❌ Servidor está offline. Certifique-se de que o servidor está rodando com 'python server.py'")

col1, col2 = st.columns(2)

with col1:
    if st.button("Testar Conexão Segura"):
        with st.spinner("Estabelecendo conexão segura..."):
            response = get('/')
            
        if "error" in response:
            st.error(f"Erro na conexão: {response['error']}")
        else:
            st.success("Conexão segura estabelecida!")
            st.json(response)

with col2:
    if st.button("Enviar Requisição de Teste"):
        with st.spinner("Enviando requisição..."):
            response = get('/hello')
            
        if "error" in response:
            st.error(f"Erro na conexão: {response['error']}")
        else:
            st.success("Resposta recebida com sucesso!")
            st.json(response) 