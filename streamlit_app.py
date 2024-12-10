from pathlib import Path
import pandas as pd

import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)



# CSS para ocultar el header
hide_streamlit_style = """
            <style>
            /* Ocultar el header */
            #header {visibility: hidden;}
            /* Ocultar el menú de hamburguesa */
            .css-18e3th9 {visibility: hidden;}
            /* Opcional: Ocultar el footer de Streamlit */
            .ezrtsby1 {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Crear un DataFrame de ejemplo con dos columnas adicionales
data = {
    'Fecha': [1, 2, 3],
    'Nombre': ['chatbot', 'generador', 'generador'],
    'Modelo': ['gpt-4o', 'gpt-3.5', 'gpt-4'],
    'Hora inicial': ['A', 'B', 'C'],
    'Hora final': [4, 5, 6],
    'Duracion total': ['D', 'E', 'F'],
    'link repositorio': ['A', 'B', 'C'],
}
df = pd.DataFrame(data)

# Guardar el DataFrame en session state
if 'dataframe' not in st.session_state:
    st.session_state['dataframe'] = df

# Mostrar el DataFrame ocupando todo el ancho de la página
st.dataframe(st.session_state['dataframe'], use_container_width=True)

import streamlit as st
import webbrowser

ruta = Path.cwd()
file_path = (ruta / f'jacoco/index.html')
#C:/Users/SURAMERICANA/PycharmProjects/asoprojectv3/asoassistantv3/generated/riskadmissionscalculateincomesv0/target/site/jacoco/index.html

# Ruta al archivo HTML en tu proyecto
#file_path = '/target/site/jacoco/index.html'

# URL que se abrirá en una nueva pestaña (file:// es para abrir archivos locales)
url = 'file://' + str(file_path)


# Función para abrir el archivo HTML en una nueva pestaña
def open_new_tab(url):
  webbrowser.open_new_tab(url)

if st.button('mostrar'):
  open_new_tab(url)



import subprocess

# Define el comando que quieres ejecutar
command = f"xdg-open {file_path}"

# Usa subprocess para ejecutar el comando
process = subprocess.Popen(command, shell=True)
process.wait()  # Espera a que el proceso termine (opcional)
