import week2_review_main as w2_main
import unittest

class W2MainTest(unittest.TestCase):

    def test_square(self):
        self.assertEqual(w2_main.square(2), 4, "Squares do not match")
        self.assertEqual(w2_main.square(4), 16, "Squares do not match")

    def test_square_letter(self):
        self.assertRaises(ValueError)


