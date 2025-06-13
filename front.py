import requests
import streamlit as st


def get():
    url = "https://10.128.1.78:5555/hello"
    cert = ('certificate.crt', 'private.key')
    response = requests.get(url=url,cert=cert, verify=False)
    return response.json()

def page1():
    st.title("Troca de mensagens")
    mensagem = st.chat_input("Escreva algo")
    if mensagem:
        st.write(mensagem)


def page2():
    st.title("testar get")
    st.write(get())

pg = st.navigation([
    st.Page(page1, title="Mensagem", icon="🔥"),
    st.Page(page2, title="Get", icon="🥰"),
])

pg.run()