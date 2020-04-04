import unittest
from src.lab4 import *


class TestLab4(unittest.TestCase):
    def testADJ(self):
        self.assertEqual(lab4('Красивый, веселый, красный!'), (3, 0, 0))

    def testADVERB(self):
        self.assertEqual(lab4('Они мигом погасли'), (0, 2, 0))

    def testVERB(self):
        self.assertEqual(lab4('Он улыбнулся. Ткнул пальцем.'), (0, 0, 4))

    def testJim(self):
        self.assertEqual(lab4('Пришло лето, и ветер был летний — теплое дыхание мира, неспешное и ленивое.'), (1, 1, 2))


if __name__ == '__main__':
    unittest.main()
