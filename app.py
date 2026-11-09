import streamlit as st
import pandas as pd

st.title("Sistemade Calificaciones")
st.write("Consulte y registre las materias con sus respectivas notas")

st.markdown("### Mis materias")

datos = {
    "Materia":["Lógica","Cálculo","Álgebra","Introducción","Filosofía","Inglés"],
    "Calificación":[3.7,5.0,5.0,4.8,4.7,4.8]
}
tabla = pd.DataFrame(datos)
st.dataframe(tabla)

promedio = tabla["Calificación"].mean()
st.write("El promedioes de: ", round(promedio,2))

st.markdown("### Una nueva materia")
nueva_materia = st.text_input("Ingrese el nombre de la materia: ")
nueva_calificacion = st.slider(
    "Seleccionelacalificación de la nueva materia:",
    min_value=0.0,
    max_value=5.0,
    value=3.0,
    step=0.1)

if st.button("Agregar materia"):

    if nueva_materia != "":
        materia = {
            "Materia":nueva_materia,
            "Calificación": nueva_calificacion
        }
        nueva_fila = pd.DataFrame([materia])
        nueva_tabla = pd.concat([tabla, nueva_fila],ignore_index=True)

        st.success("Materia agregada correctamente")

        st.dataframe(nueva_tabla)
        promedio_nuevo = nueva_tabla["Calificación"].mean()
        st.write("El promedio es: ", round(promedio_nuevo,2))
    else:
        st.warning("debes escribir el nombre de la materia")





