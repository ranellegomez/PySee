import PyRead as pr
import unittest


class TestPyRead(unittest.TestCase):
    # These test cases are still being written.
    def test_english(self):
        test_img = '.../PySee/test/images/English/tnol8.jpg'
        self.assertEqual("ONE DOES NOT'SIMPLY, Pie heey 7", pr.Scanner.img_to_english(self, test_img))

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
