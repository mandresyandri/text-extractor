import os
import fitz
import pytesseract
from PIL import Image

# OOP : EXTRACTION RESSOURCE TEXTE D'UN PDF
# VERSION : 28.12.24
class TEXTExtractor:
    def __init__(self, pdf_file, output_folder="output_images"):
        self.pdf_file = pdf_file
        self.output_folder = output_folder

    def convert_pdf_to_images(self):
        # Convertit un PDF en une série d'images PNG avec PyMuPDF
        os.makedirs(self.output_folder, exist_ok=True)
        pdf_document = fitz.open(self.pdf_file)
        image_paths = []

        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            pix = page.get_pixmap()
            output_path = os.path.join(self.output_folder, f"page_{page_number + 1}.png")
            pix.save(output_path)
            image_paths.append(output_path)
        
        return image_paths

    def extract_text_from_images(self, image_paths):
        # Extrait le texte de toutes les images avec pytesseract
        extracted_text = ""
        for image_path in image_paths:
            text = pytesseract.image_to_string(image_path, lang="fra", config="--psm 1")
            extracted_text += f"\n--- {os.path.basename(image_path)} ---\n{text}\n"
        return extracted_text