import streamlit as st
import pandas as pd
from PIL import Image
import requests
import datetime
import time

icon = Image.open('seven.png')
st.set_page_config(
    page_title ="Seven Barbershop",
    page_icon= icon,
    layout="wide"
)
log = pd.read_csv("log.csv")


response = requests.get("https://ipinfo.io/json")
ip_info = response.json()
data = {
    "Timestamp": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    "IP": [ip_info.get("ip")],
    "City": [ip_info.get("city")],
    "Region": [ip_info.get("region")],
    "Country": [ip_info.get("country")],
    "Location": [ip_info.get("loc")],
    "Org": [ip_info.get("org")],
    "Postal": [ip_info.get("postal")],
    "Timezone": [ip_info.get("timezone")],
    "Click": "First Login"
}
df = pd.DataFrame(data)
df3= pd.concat([log, df], ignore_index=True)
df3.to_csv("log.csv",index=False)

# CSS para dimensionar e estilizar os botões
button_style = """
<style>
.stButton button {
    width: 100%;
    margin: auto;
    display: block;
    color: white;
    background: black;
}
</style>
"""

# Aplica o CSS
st.markdown(button_style, unsafe_allow_html=True)

st.image('Barberia seven.png')

st.header("Seja bem vindo à página da Seven Barbershop!")
st.write("Com mais de 4 anos no mercado, a Seven Barbershop está localizada na Avenida Dante Siani, nº 1433, no bairro Jardim Santa Marina em Jacareí-SP. Nossa barbearia oferece uma experiência personalizada em cuidados com a aparência. Com serviços como corte de cabelo, barbaterapia, alisamento de cabelo e desenho das sobrancelhas, garantimos qualidade e estilo. Nossos profissionais são especialistas em tendências modernas e clássicas, utilizando produtos de alta qualidade Fox for Men.")

with st.expander("Nosso serviços e valores"):
    comb, cort = st.columns(2)
    comb.image("combos.jpg")
    cort.image("cortes.jpg")

#Imagens
erick, matheus = st.columns([2,2])

erick.image("erick.png",caption = "Erick Ribeiro - Contato: (12) 98174-6346")
if erick.button("Agendar com Erick"):
    url = "https://wa.me/5512981746346?text=Ol%C3%A1%2C%20gostaria%20de%20agendar%20um%20hor%C3%A1rio"
    # Use JavaScript to redirect
    js = f"window.open('{url}');"
    html = f"<script>{js}</script>"
    st.components.v1.html(html)
    st.success("Se você não foi redirecionado, por favor, habilite os pop-ups ou clique nesse link: https://abrir.link/zrfIn")
    response = requests.get("https://ipinfo.io/json")
    ip_info = response.json()
    data = {
        "Timestamp": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "IP": [ip_info.get("ip")],
        "City": [ip_info.get("city")],
        "Region": [ip_info.get("region")],
        "Country": [ip_info.get("country")],
        "Location": [ip_info.get("loc")],
        "Org": [ip_info.get("org")],
        "Postal": [ip_info.get("postal")],
        "Timezone": [ip_info.get("timezone")],
        "Click": "Erick"
    }
    df = pd.DataFrame(data)
    df3= pd.concat([log, df], ignore_index=True)
    df3.to_csv("log.csv",index=False)

matheus.image("matheus.png",caption = "Matheus Henrique - Contato: (12) 99770-3132")

if matheus.button("Agendar com Matheus"):
    url = "https://wa.me/5512997703132?text=Ol%C3%A1%2C%20gostaria%20de%20agendar%20um%20hor%C3%A1rio"
    js = f"window.open('{url}');"
    html = f"<script>{js}</script>"
    st.components.v1.html(html)
    st.success("Se você não foi redirecionado, por favor, habilite os pop-ups ou clique nesse link: https://abrir.link/iMACX")
    response = requests.get("https://ipinfo.io/json")
    ip_info = response.json()
    data = {
        "Timestamp": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "IP": [ip_info.get("ip")],
        "City": [ip_info.get("city")],
        "Region": [ip_info.get("region")],
        "Country": [ip_info.get("country")],
        "Location": [ip_info.get("loc")],
        "Org": [ip_info.get("org")],
        "Postal": [ip_info.get("postal")],
        "Timezone": [ip_info.get("timezone")],
        "Click": "Matheus"
    }
    df = pd.DataFrame(data)
    df3= pd.concat([log, df], ignore_index=True)
    df3.to_csv("log.csv",index=False)
st.table(df3)


