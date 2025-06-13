import requests
import streamlit as st


def get():
    url = "https://10.128.1.78:5555/hello"
    s = requests.Session()
    s.cert = 'certificate.crt'
    response = requests.get(url=url, cert="certificate.crt")
    return response.status_code

def page1():
    st.title("Troca de mensagens")
    st.chat_input("Escreva algo")

def page2():
    st.title("testar get")
    st.write(get())

pg = st.navigation([
    st.Page(page1, title="Mensagem", icon="🔥"),
    st.Page(page2, title="Get", icon="🥰"),
])

pg.run()