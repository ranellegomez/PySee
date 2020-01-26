import pytesseract as pt
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import collections
import random
from docx import Document
from docx.shared import Inches


class Utils:
    """Contains the various methods to to convert images to text of different languages."""

    def string_to_doc(self, txt, path):
        """Returns a .docx file with both the original image and the transcribed text."""
        result = Document()
        result.add_heading('Results of OCR conversion', 0)
        for i in range(len(path)):
            result.add_picture(path[i], width=Inches(5.0))
            result.add_paragraph(txt[i])
        result.save('images_and_texts.docx')

    def img_to_english(self, eng_images, file_path=None):
        resultant_text = []
        for eng_img in eng_images:
            ocr_readable_eng_img = Image.open(eng_img)
            resultant_text.append(pt.image_to_string(ocr_readable_eng_img))
        Utils.string_to_doc(self, resultant_text, file_path)
        return resultant_text

    def img_to_spanish(self, spa_images, file_path=None):
        resultant_text_spa = []
        for spa_img in spa_images:
            ocr_readable_spa_img = Image.open(spa_img)
            resultant_text_spa.append(pt.image_to_string(ocr_readable_spa_img))
        if file_path is not None:  # Added for unit testing when no file_path is passed.
            Utils.string_to_doc(self, resultant_text_spa, file_path)
        return resultant_text_spa

        if not isinstance(spa_images, collections.Iterable):
            converted_spa_img = pt.image_to_string(spa_images, lang='spa')
            print(converted_spa_img)
            return converted_spa_img
        for spa_img in spa_images:
            ocr_readable_spa_img = Image.open(spa_img)
            converted_spa_txt = pt.image_to_string(ocr_readable_spa_img, lang='spa')
            print(converted_spa_txt)
            return converted_spa_txt

    def img_to_french(self, fra_images):
        if not isinstance(fra_images, collections.Iterable):
            converted_fra_img = pt.image_to_string(fra_images, lang='fra')
            print(converted_fra_img)
            return converted_fra_img
        for fra_img in fra_images:
            ocr_readable_fra_img = Image.open(fra_img)
            converted_fra_txt = pt.image_to_string(ocr_readable_fra_img, lang='fra')
            print(converted_fra_txt)
            return converted_fra_txt

    def img_to_german(self, deu_images):
        if not isinstance(deu_images, collections.Iterable):
            converted_deu_img = pt.image_to_string(deu_images, lang='deu')
            print(converted_deu_img)
            return converted_deu_img
        for deu_img in deu_images:
            ocr_readable_deu_img = Image.open(deu_img)
            converted_deu_txt = pt.image_to_string(ocr_readable_deu_img, lang='deu')
            print(converted_deu_txt)
            return converted_deu_txt

    def img_to_japanese(self, jpn_images):
        if not isinstance(jpn_images, collections.Iterable):
            converted_jpn_img = pt.image_to_string(jpn_images, lang='jpn')
            print(converted_jpn_img)
            return converted_jpn_img
        for jpn_img in jpn_images:
            ocr_readable_jpn_img = Image.open(jpn_img)
            converted_jpn_txt = pt.image_to_string(ocr_readable_jpn_img, lang='jpn')
            print(converted_jpn_txt)
            return converted_jpn_txt

    def img_to_chinese(self, chi_sim_images):
        if not isinstance(chi_sim_images, collections.Iterable):
            converted_chi_sim_img = pt.image_to_string(chi_sim_images, lang='chi_sim')
            print(converted_chi_sim_img)
            return converted_chi_sim_img
        for chi_sim_img in chi_sim_images:
            ocr_readable_chi_sim_img = Image.open(chi_sim_img)
            converted_chi_sim_txt = pt.image_to_string(ocr_readable_chi_sim_img, lang='chi_sim')
            print(converted_chi_sim_txt)
            return converted_chi_sim_txt


if __name__ == '__main__':

    obj = Utils()
    while True:
        selection = input('Which language would you like to convert your image to text? 1. English 2. Spanish 3. '
                          'French 4. German 5. Japanese 6. Simplified Chinese 7. Exit\n')
        root = tk.Tk()
        root.withdraw()
        image_selection = tk.filedialog.askopenfilenames()
        selection_path = image_selection

        if selection not in "1234567":
            print('Invalid choice.')
            continue
        elif selection == '1':
            obj.img_to_english(image_selection, selection_path)
        elif selection == '2':
            obj.img_to_spanish(image_selection)
        elif selection == '3':
            obj.img_to_french(image_selection)
        elif selection == '4':
            obj.img_to_german(image_selection)
        elif selection == '5':
            obj.img_to_japanese(image_selection)
        elif selection == '6':
            obj.img_to_chinese(image_selection)
        else:
            goodbye = ['¡Adiós!', 'Goodbye!', 'じゃね。', 'Tschüss!', 'Au revoir!', '再见。']
            print(random.choice(goodbye))
            break
