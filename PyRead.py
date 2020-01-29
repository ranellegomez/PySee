import pytesseract as pt
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import random
from docx import Document
from docx.shared import Inches
import os


class Utils:
    """Contains the various methods to to convert images to text of different languages."""
    def string_to_doc(self, txt, path):
        """Return a .docx file with both the original image and the transcribed text."""
        result = Document()
        result.add_heading('Results of OCR conversion', 0)
        for i in range(len(path)):
            result.add_picture(path[i], width=Inches(5.0))
            result.add_paragraph(txt[i])
        file_location_and_name = filedialog.asksaveasfilename(initialdir="/", title="Select file location and input file name.",
                                   filetypes=([("DOCs", "*.docx .doc")]))
        chosen_name = os.path.basename(file_location_and_name)
        chosen_path = os.path.dirname(file_location_and_name)
        result.save(os.path.join(chosen_path, chosen_name))

    def img_to_english(self, eng_images, file_path_eng):
        """Return an array of strings of all English OCR-translated files."""
        resultant_text = []
        for eng_img in eng_images:
            ocr_readable_eng_img = Image.open(eng_img)
            resultant_text.append(pt.image_to_string(ocr_readable_eng_img))
        Utils.string_to_doc(self, resultant_text, file_path_eng)
        return resultant_text

    def img_to_spanish(self, spa_images, file_path_spa):
        """Return an array of strings of all Spanish OCR-translated files."""
        resultant_text_spa = []
        for spa_img in spa_images:
            ocr_readable_spa_img = Image.open(spa_img)
            resultant_text_spa.append(pt.image_to_string(ocr_readable_spa_img))
        Utils.string_to_doc(self, resultant_text_spa, file_path_spa)
        return resultant_text_spa

    def img_to_french(self, fra_images, file_path_fra):
        """Return an array of strings of all French OCR-translated files."""
        resultant_text_fra = []
        for fra_img in fra_images:
            ocr_readable_fra_img = Image.open(fra_img)
            resultant_text_fra.append(pt.image_to_string(ocr_readable_fra_img))
        Utils.string_to_doc(self, resultant_text_fra, file_path_fra)
        return resultant_text_fra

    def img_to_german(self, deu_images, file_path_deu):
        """Return an array of strings of all German OCR-translated files."""
        resultant_text_deu = []
        for deu_img in deu_images:
            ocr_readable_deu_img = Image.open(deu_img)
            resultant_text_deu.append(pt.image_to_string(ocr_readable_deu_img))
        Utils.string_to_doc(self, resultant_text_deu, file_path_deu)
        return resultant_text_deu

    def img_to_japanese(self, jpn_images, file_path_jpn):
        """Return an array of strings of all Japanese OCR-translated files."""
        resultant_text_jpn = []
        for jpn_img in jpn_images:
            ocr_readable_jpn_img = Image.open(jpn_img)
            resultant_text_jpn.append(pt.image_to_string(ocr_readable_jpn_img))
        Utils.string_to_doc(self, resultant_text_jpn, file_path_jpn)
        return resultant_text_jpn

    def img_to_chinese(self, chi_sim_images, file_path_chi_sim):
        """Return an array of strings of all simplified Chinese OCR-translated files."""
        resultant_text_chi_sim = []
        for chi_sim_img in chi_sim_images:
            ocr_readable_chi_sim_img = Image.open(chi_sim_img)
            resultant_text_chi_sim.append(pt.image_to_string(ocr_readable_chi_sim_img))
        Utils.string_to_doc(self, resultant_text_chi_sim, file_path_chi_sim)
        return resultant_text_chi_sim


if __name__ == '__main__':

    obj = Utils()
    while True:
        selection = input('Which language would you like to convert your image to text? 1. English 2. Spanish 3. '
                          'French 4. German 5. Japanese 6. Simplified Chinese 7. Exit\n')
        root = tk.Tk()
        root.withdraw()
        image_selection = tk.filedialog.askopenfilenames(title='Choose your images.', filetypes=[("PNG","*.png"),("JPEGs","*.jpeg jpg"),("GIF","*.gif"),(("BMP","*.bmp"),("tiff","*.tif tiff"))])
        selection_path = image_selection

        if selection not in "1234567":
            print('Invalid choice.')
            continue
        elif selection == '1':
            obj.img_to_english(image_selection, selection_path)
        elif selection == '2':
            obj.img_to_spanish(image_selection, selection_path)
        elif selection == '3':
            obj.img_to_french(image_selection, selection_path)
        elif selection == '4':
            obj.img_to_german(image_selection, selection_path)
        elif selection == '5':
            obj.img_to_japanese(image_selection, selection_path)
        elif selection == '6':
            obj.img_to_chinese(image_selection, selection_path)
        else:
            goodbye = ['¡Adiós!', 'Goodbye!', 'じゃね。', 'Tschüss!', 'Au revoir!', '再见。']
            print(random.choice(goodbye))
            break
