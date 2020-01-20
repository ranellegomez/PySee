import pytesseract as pt
from PIL import Image, ImageEnhance
import tkinter as tk
from tkinter import filedialog
import random


class Scanner:
    """Contains the various methods to to convert images to text of different languages."""

    def img_to_english(self, images):
        for img in images:
            ocr_readable_img = Image.open(img)
            print(ocr_readable_img)

    def img_to_spanish(self, images):
        for img in images:
            ocr_readable_img = Image.open(img)
            print(pt.image_to_string(ocr_readable_img, lang='spa'))

    def img_to_french(self, images):
        for img in images:
            ocr_readable_img = Image.open(img)
            print(pt.image_to_string(ocr_readable_img, lang='fra'))

    def img_to_german(self, images):
        for img in images:
            ocr_readable_img = Image.open(img)
            print(pt.image_to_string(ocr_readable_img, lang='deu'))

    def img_to_japanese(self, images):
        for img in images:
            ocr_readable_img = Image.open(img)
            print(pt.image_to_string(ocr_readable_img, lang='jpn'))

    def img_to_chinese(self, images):
        for img in images:
            ocr_readable_img = Image.open(img)
            print(pt.image_to_string(ocr_readable_img, lang='chi_sim'))

if __name__ == '__main__':
    obj = Scanner()

    while True:
        selection = input('Which language would you like to convert your image to text?\' 1. English 2. Spanish 3. '
                          'French 4. German 5. Japanese 6. Chinese 7. Exit\n')
        root = tk.Tk()
        root.withdraw()
        image_selection = tk.filedialog.askopenfilenames()

        if selection not in "1234567":
            print('Invalid choice.')
            continue
        elif selection == '1':
            obj.img_to_english(image_selection)
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
