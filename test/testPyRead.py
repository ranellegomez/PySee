import PyRead as pr
from PIL import Image
import sys
import os
import unittest


class TestPyRead(unittest.TestCase):
    # These test cases are still being written.
    def test_english(self):
        curr_directory = sys.path[0]
        favorite_path = os.path.join(curr_directory, 'images/English/favoritethings.png')
        favorite = Image.open(favorite_path)
        expected = """Staying up for the 61B discussion signup, looking at increased grade bins, writing code: these
are a few of my favorite things."""
        print(pr.Scanner.img_to_english(self, favorite))
        self.assertEqual(expected, pr.Scanner.img_to_english(self, favorite))

    def test_spanish(self):
        curr_directory = sys.path[0]
        menudo_path = os.path.join(curr_directory, 'images/Spanish/menudo.png')
        menudo = Image.open(menudo_path)
        expected = 'Me gusta comer menudo a menudo.'
        print(pr.Scanner.img_to_spanish(self, menudo))
        self.assertEqual(expected, pr.Scanner.img_to_spanish(self, menudo))

        marta_path = os.path.join(curr_directory, 'images/Spanish/marta.png')
        marta = Image.open(marta_path)
        expected_2 = 'Marta tiene dos marcapasos pero solo tiene un corazón.'
        print(pr.Scanner.img_to_spanish(self, marta))
        self.assertEqual(expected_2, pr.Scanner.img_to_spanish(self, marta))

    def test_french(self):
        self.assertEqual(True, False)


    def test_german(self):
        self.assertEqual(True, False)

    def test_japanese(self):
        self.assertEqual(True, False)

    def test_chinese(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
