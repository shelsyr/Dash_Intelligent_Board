import streamlit as st
from sqlalchemy import create_engine
import sweetviz as sv
import pandas as pd
import plotly.express as gr


def logearse():
        lateral = st.sidebar
        st.title('DASH INTELLIGENT BOARD')
        lateral.subheader('Por favor inicie sesion')

        lateral.write('---')

        usu = lateral.text_input('Ingrese su Usuario')
        con = lateral.text_input('Ingrese su contraseña')
        
        if lateral.button('Ingresar'):
            if usu == 'a' and con == 'b':
                lateral.success('Ha ingresado con exito')
                st.balloons()
                return True

            else:
                lateral.error('Datos invalidos')
                return False
   

def pagina_principal():
    st.sidebar.write('Bienvenido Usuario A')    
    st.sidebar.image('piña.jpg')

def datos(opc:int=0):
    db_connection_str = 'mysql+pymysql://asesoria4_LaVecinaSAS:dashinteligentboard123@cpanel4-co.conexcol.net/asesoria4_LaVecina_SAS'
    db_connection = create_engine(db_connection_str)
    df = pd.read_sql('SELECT * FROM Ventas', con=db_connection)
    return df
    
def mostrar_datos(datos:pd.DataFrame):
    st.dataframe(datos)

def grafica_barras(datos:pd.DataFrame):
    
    grafica = gr.bar(datos,x='Product line',y='Total',color='Gender')
    st.plotly_chart(grafica)

def graficaLinea(datos:pd.DataFrame):
    grafica = gr.scatter(datos, x="Rating", y="Total", color="Product line", trendline="lowess")
    st.plotly_chart(grafica)
    
if __name__ == '__main__':
    st.set_page_config(page_title='Dash Intelligent Board',page_icon='shelsy.png')
    if logearse():
        pagina_principal()
        st.write('---')
        st.write('A continuación se muestran los datos almacenados de la Tienda')
        df = datos()
        mostrar_datos(df)
        st.write('---')
        st.write('Grafica de barras sobre la categoria del producto y el total, ademas de estar separado por generos')
        grafica_barras(df)
        st.write('---')
        st.write('Grafica de puntos y lineas de tendencia sobre el Rating y el Total')
        graficaLinea(df)
        sv.config_parser.read("Override.ini")
        a = sv.compare_intra(df, df["Gender"] == "Male", ["Male", "Female"])
        a.show_html('Hombre_vs_mujer.html')
        b = sv.compare_intra(df, df["Customer type"] == "Member", ["Member", "Normal"])
        b.show_html('normal_vs_miembro.html')


        
        
        
    

    

    
