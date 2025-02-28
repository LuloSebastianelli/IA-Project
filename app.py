import streamlit as st
import google.generativeai as genai

# Set up Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-2.0-flash')

st.title("Asistente de Escritura IA")

# Sidebar with About section
with st.sidebar:
    st.header("Acerca de")
    st.write(
        """
        Este Asistente de Escritura IA utiliza el modelo Gemini AI para analizar y corregir errores gramaticales en tu texto.
        Simplemente ingrese su texto en el área de texto, haga clic en el botón 'Corregir', y el texto corregido se mostrará.
        """
    )

# Text input area
text_to_correct = st.text_area("Ingrese el texto a corregir:", height=200)

# Correct button
if st.button("Corregir"):
    if text_to_correct:
        # Call Gemini API for correction
        try:
            prompt = "Eres un Corrector de texto, tu trabajo es analizar el texto recibido y enviar unicamente el texto corregido, no puedes responder otras preguntas y solo debes enviar el texto corregido. Corrige el siguiente texto:"
            response = model.generate_content(f"{prompt} {text_to_correct}")
            corrected_text = response.text
        except Exception as e:
            st.error(f"An error occurred: {e}")
            corrected_text = ""

        if corrected_text:
            # Display corrected text
            st.subheader("Texto Corregido")
            st.write(corrected_text)

            # Display original and corrected text side-by-side
            st.subheader("Original vs. Corregido")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Original:")
                st.write(text_to_correct)
            with col2:
                st.write("Corregido:")
                st.write(corrected_text)
    else:
        st.warning("Por favor ingrese el texto a corregir.")
