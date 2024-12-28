import os
from PIL import Image
import streamlit as st
from text_extractor import TEXTExtractor

# Application Streamlit
st.title("Extracteur de texte")

uploaded_file = st.file_uploader("Chargez un fichier PDF, PNG, JPG", type=["pdf", "png", "jpg"])

if uploaded_file:
    # Sauvegarder temporairement le fichier
    temp_file_path = os.path.join("temp", uploaded_file.name)
    os.makedirs("temp", exist_ok=True)
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Initialiser l'extracteur 
    extractor = TEXTExtractor(temp_file_path, output_folder=os.path.join("temp", "images"))

    if uploaded_file.type == "application/pdf":
        # st.write("PDF détecté !")
        # Convertir le PDF en images
        with st.spinner("Conversion en cours..."):
            image_paths = extractor.convert_pdf_to_images()
        st.success("Conversion terminée !")

        # Extraire le texte des images
        with st.spinner("Extraction de texte en cours..."):
            extracted_text = extractor.extract_text_from_images(image_paths)
    else:
        # Extraire le texte directement de l'image
        image_paths = [temp_file_path]
        with st.spinner("Extraction de texte en cours..."):
            extracted_text = extractor.extract_text_from_images(image_paths)

    # Afficher le texte extrait
    st.text_area("Texte extrait :", extracted_text, height=400)
