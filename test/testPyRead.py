import PyRead as pr
from PIL import Image
import sys
import os
import unittest


class TestPyRead(unittest.TestCase):
    # These test cases are still being written.
    def test_english(self):
        curr_directory = sys.path[0]
        test_img = os.path.join(curr_directory, 'images/English/favoritethings.png')
        image = Image.open(test_img)
        expected = """Staying up for the 61B discussion signup, looking at increased grade bins, writing code: these
are a few of my favorite things."""
        print(pr.Scanner.img_to_english(self, image))
        self.assertEqual(expected, pr.Scanner.img_to_english(self, image))

    def test_spanish(self):
        self.assertEqual(True, False)

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
