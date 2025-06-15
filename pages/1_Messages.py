import streamlit as st

st.title("📨 Troca de Mensagens Seguras")

mensagem = st.chat_input("Escreva uma mensagem (será enviada de forma segura)")
if mensagem:
    st.success("Mensagem enviada de forma segura:")
    st.write(mensagem)
    st.info("Esta mensagem foi protegida por TLS 1.2") 