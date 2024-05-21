import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv(r"C:\Users\THINKPAD L14\Documents\Visual Studio Code\Proyectos\Proyecto_Sprint_5\vehicles_us.csv") # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
disp_checkbox = st.checkbox('Construir grafica de dispersion')
        
if hist_button: # al hacer clic en el botón
        # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
        # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
        # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_checkbox: #al hacer click en el boton
    #escribir un mensaje
    st.write('Creacion de una grafica de dispersion para el conjunto de anuncios de venta de coches')

    # crear grafica de dispersion
    fig = px.scatter(car_data, x = "odometer", y = "price")

    # mostrar garfico 
    st.plotly_chart(fig, use_container_width=True)