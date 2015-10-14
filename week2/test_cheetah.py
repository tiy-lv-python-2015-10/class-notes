import unittest
from class_based_tests import Cheetah


class CheetahTest(unittest.TestCase):

    def setUp(self):
        self.my_cheetah = Cheetah("chester", "carnivores",
                             "growl", "run really fast")

    def test_cheetah_noise(self):
        self.assertEqual(self.my_cheetah.get_noise(), "growl", "This is wrong")

    def test_cheetah_move(self):
        self.assertEqual(self.my_cheetah.get_move(), "run really fast",
                         "Moving incorrect")